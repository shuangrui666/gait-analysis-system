"""Rebuild descriptive features for running/upstairs/downstairs Phyphox archives."""
from pathlib import Path
import argparse, hashlib, re, zipfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfiltfilt

ROOT=Path(__file__).resolve().parents[1]

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--inventory",default=str(ROOT/"data/metadata/dataset_inventory.csv"))
    p.add_argument("--sha256-map",default=str(ROOT/"data/metadata/dataset_sha256_mapping.csv"))
    p.add_argument("--zip-dir",default=str(ROOT/"data/raw"))
    p.add_argument("--output-dir",default=str(ROOT/"analysis/running_stairs"))
    a=p.parse_args()
    inv=pd.read_csv(a.inventory).fillna("")
    hashes=pd.read_csv(a.sha256_map)
    byhash={}
    for f in Path(a.zip_dir).glob("*.zip"):
        byhash[hashlib.sha256(f.read_bytes()).hexdigest()]=f
    out=Path(a.output_dir);out.mkdir(parents=True,exist_ok=True)
    feats=[];rolling=[];traces={}
    for _,r in inv[inv.motion_type.isin(["running","upstairs","downstairs"])].iterrows():
        h=hashes.loc[hashes.dataset_id==r.dataset_id,"sha256"]
        if h.empty or str(h.iloc[0]).lower() not in byhash: raise RuntimeError(f"SHA-256 archive missing: {r.dataset_id}")
        path=byhash[str(h.iloc[0]).lower()]
        with zipfile.ZipFile(path) as z:
            raw=next(n for n in z.namelist() if n.lower().endswith("raw data.csv"))
            d=pd.read_csv(z.open(raw))
            meta_name=next((n for n in z.namelist() if n.lower().endswith("meta/time.csv")),None)
            meta=pd.read_csv(z.open(meta_name)) if meta_name else pd.DataFrame()
        tc=next(c for c in d if c.lower().startswith("time"))
        axes=[]
        for ax in "xyz":
            c=next((c for c in d if re.search(rf"acceleration\s*{ax}\s*\(",c,re.I)),None)
            if c is None:c=next(c for c in d if re.search(rf"linear acceleration\s*{ax}",c,re.I))
            axes.append(c)
        t=pd.to_numeric(d[tc],errors="coerce").to_numpy(float)
        xyz=d[axes].apply(pd.to_numeric,errors="coerce").to_numpy(float)
        ok=np.isfinite(t)&np.isfinite(xyz).all(axis=1);t=t[ok];xyz=xyz[ok]
        dt=np.diff(t);dt=dt[dt>0]
        fs=1/np.median(dt);duration=t[-1]-t[0]
        mag=np.linalg.norm(xyz,axis=1)
        sos=butter(3,.5,btype="highpass",fs=fs,output="sos")
        dyn=np.linalg.norm(sosfiltfilt(sos,xyz,axis=0),axis=1)
        pause=np.nan
        if not meta.empty and "event" in meta:
            q=meta[meta.event.astype(str).str.upper()=="PAUSE"]
            if len(q):pause=float(q.iloc[-1]["experiment time"])
        feats.append(dict(dataset_id=r.dataset_id,motion_type=r.motion_type,phone_placement=r.phone_placement,
            sensor_type=r.sensor_type,expected_rate_hz=float(r.sampling_rate_hz),measured_rate_hz=fs,
            n_samples=len(t),duration_csv_s=duration,duration_meta_pause_s=pause,sha256_verified=True,
            magnitude_mean_m_s2=np.mean(mag),magnitude_std_m_s2=np.std(mag,ddof=1),
            magnitude_p95_m_s2=np.percentile(mag,95),magnitude_max_m_s2=np.max(mag),
            dynamic_rms_0p5hz_m_s2=np.sqrt(np.mean(dyn**2)),dynamic_p95_0p5hz_m_s2=np.percentile(dyn,95),
            median_dt_ms=np.median(dt)*1000,max_gap_ms=np.max(dt)*1000))
        traces[r.dataset_id]=(t-t[0],dyn,r.phone_placement,r.sensor_type,fs)
        w=int(2*fs);hop=int(.25*fs)
        for i in range(0,len(t)-w+1,hop):
            s=dyn[i:i+w]
            rolling.append(dict(dataset_id=r.dataset_id,motion_type=r.motion_type,phone_placement=r.phone_placement,
                sensor_type=r.sensor_type,window_start_s=t[i]-t[0],window_end_s=t[i+w-1]-t[0],
                dynamic_rms_2s_m_s2=np.sqrt(np.mean(s**2)),dynamic_p95_2s_m_s2=np.percentile(s,95)))
    f=pd.DataFrame(feats);w=pd.DataFrame(rolling)
    s=f.groupby(["motion_type","phone_placement","sensor_type","expected_rate_hz"]).agg(
        dataset_count=("dataset_id","count"),mean_duration_s=("duration_csv_s","mean"),
        mean_dynamic_rms_m_s2=("dynamic_rms_0p5hz_m_s2","mean"),
        sd_dynamic_rms_m_s2=("dynamic_rms_0p5hz_m_s2","std"),
        mean_dynamic_p95_m_s2=("dynamic_p95_0p5hz_m_s2","mean")).reset_index()
    f.to_csv(out/"running_upstairs_downstairs_dataset_features.csv",index=False)
    s.to_csv(out/"running_upstairs_downstairs_stratified_summary.csv",index=False)
    w.to_csv(out/"running_upstairs_downstairs_rolling_features.csv",index=False)
    for motion in ["running","upstairs","downstairs"]:
        sub=f[f.motion_type==motion];fig,axs=plt.subplots(len(sub),1,figsize=(12,max(3,2*len(sub))),squeeze=False)
        for ax,(_,r) in zip(axs[:,0],sub.iterrows()):
            t,y,place,sensor,fs=traces[r.dataset_id];step=max(1,len(t)//5000)
            ax.plot(t[::step],y[::step],lw=.55);ax.set_title(f"{r.dataset_id} | {place} | {sensor} | {fs:.0f} Hz",fontsize=8);ax.set_ylabel("m/s²");ax.grid(alpha=.2)
        axs[-1,0].set_xlabel("Time (s)");fig.tight_layout();fig.savefig(out/f"{motion}_dynamic_traces.png",dpi=160,bbox_inches="tight");plt.close(fig)
    print(f"Analyzed {len(f)} datasets; SHA-256 verified for all {int(f.sha256_verified.sum())}.")
    print(s.to_string(index=False))

if __name__=="__main__":main()

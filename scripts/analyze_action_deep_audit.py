"""Deep audit for the 17 running/upstairs/downstairs Phyphox ZIP datasets.
Run from repository root after installing requirements-analysis.txt:
python scripts/analyze_action_deep_audit.py
"""
from pathlib import Path
import zipfile, hashlib, re, io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'data'/'raw'
OUT=ROOT/'analysis'/'action_deep_audit'
FIG=OUT/'figures'
FIG.mkdir(parents=True,exist_ok=True)
TARGET={'ED8469D047C2','FF5A8008EED4','39F370E32ED6','A60734EC48AD','73B38ED61891','7FA3D57EB383','4251BB07119C','C350D50D5DDB','1A9020CA0A15','8039443C14A4','993885A48BCB','512E984EE639','253AAF5F2DD2','7909BB9AD07A','CF9602FC1477','8D5B23384548','98BDF65C41C4'}
quality=[]; axis_rows=[]; traces=[]
manifest=pd.read_csv(ROOT/'data'/'metadata'/'dataset_sha256_mapping.csv',dtype={'dataset_id':str}).set_index('dataset_id')
for path in sorted(RAW.glob('*.zip')):
    m=re.search(r'GAIT-[A-F0-9]+',path.name)
    if not m or m.group(0).replace('GAIT-','') not in TARGET: continue
    ds=m.group(0); action='running' if 'running' in path.name else ('upstairs' if 'upstairs' in path.name else 'downstairs')
    placement='handheld' if 'handheld' in path.name else 'pocket'
    sha=hashlib.sha256(path.read_bytes()).hexdigest()
    if ds not in manifest.index or sha.lower()!=str(manifest.loc[ds,'sha256']).lower(): raise ValueError(f'SHA mismatch: {ds}')
    with zipfile.ZipFile(path) as z:
        df=pd.read_csv(io.BytesIO(z.read('Raw Data.csv')))
        pd.read_csv(io.BytesIO(z.read('meta/time.csv')))
    t=df.iloc[:,0].to_numpy(float); dt=np.diff(t); med=float(np.median(dt)); hz=1/med
    cols=[c for c in df.columns if re.search(r'Acceleration [xyz]',c)]
    if len(cols)!=3: raise ValueError(f'Unexpected axis columns: {ds}')
    X=df[cols].apply(pd.to_numeric,errors='coerce').to_numpy(float)
    sensor='Linear' if all('Linear' in c for c in cols) else 'Total'
    mag=np.linalg.norm(X,axis=1)
    row={'dataset_id':ds,'action':action,'placement':placement,'sensor_type':sensor,'n_samples':len(df),'duration_s':t[-1]-t[0],'estimated_sampling_hz':hz,'median_interval_s':med,'min_interval_s':dt.min(),'max_interval_s':dt.max(),'interval_dev_gt5_n':int((np.abs(dt-med)/med>.05).sum()),'interval_dev_gt20_n':int((np.abs(dt-med)/med>.20).sum()),'missing_cells':int(df.isna().sum().sum()),'duplicate_rows':int(df.duplicated().sum()),'timestamp_monotonic':bool((dt>0).all()),'mag_mean':mag.mean(),'mag_std':mag.std(ddof=1),'mag_min':mag.min(),'mag_max':mag.max(),'mag_p95':np.percentile(mag,95),'mag_rms':np.sqrt(np.mean(mag**2)),'sha256':sha}
    quality.append(row)
    for i,ax in enumerate('xyz'):
        v=X[:,i]; axis_rows.append({'dataset_id':ds,'action':action,'placement':placement,'sensor_type':sensor,'sampling_rate_hz':hz,'axis':ax,'mean':v.mean(),'std':v.std(ddof=1),'min':v.min(),'max':v.max(),'p05':np.percentile(v,5),'p95':np.percentile(v,95)})
    traces.append((ds,action,placement,sensor,t,X))
q=pd.DataFrame(quality).sort_values(['action','dataset_id']); a=pd.DataFrame(axis_rows)
q.to_csv(OUT/'action_dataset_quality_and_magnitude.csv',index=False)
a.to_csv(OUT/'action_three_axis_statistics.csv',index=False)
s=q.groupby(['action','placement','sensor_type']).agg(dataset_count=('dataset_id','count'),duration_mean_s=('duration_s','mean'),mag_std_mean=('mag_std','mean'),mag_rms_mean=('mag_rms','mean'),mag_p95_mean=('mag_p95','mean')).reset_index()
s.to_csv(OUT/'action_stratified_magnitude_summary.csv',index=False)
for action in ('running','upstairs','downstairs'):
    subset=[x for x in traces if x[1]==action]
    fig,axs=plt.subplots(3,1,figsize=(14,10),sharex=True)
    for i,ax in enumerate(axs):
        for ds,_,place,sensor,t,X in subset:
            stride=max(1,len(t)//5000)
            ax.plot(t[::stride]-t[0],X[::stride,i],lw=.65,label=f'{ds} ({place},{sensor})')
        ax.set_ylabel(f'{"XYZ"[i]} (m/s²)'); ax.grid(True,alpha=.25)
        if i==0: ax.legend(fontsize=6,ncol=2)
    axs[-1].set_xlabel('Elapsed time (s)')
    fig.suptitle(f'{action.title()} raw three-axis waveforms')
    fig.tight_layout(); fig.savefig(FIG/f'{action}_three_axis_waveforms.png',dpi=160); plt.close(fig)
print(f'Completed {len(q)} datasets; SHA-256 matched for all; outputs: {OUT}')

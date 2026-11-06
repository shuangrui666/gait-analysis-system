"""Reproducible baseline analysis of Phyphox ZIP archives.

Run from repository root: python scripts/analyze_phyphox_archives.py
Source ZIP files are read-only. Outputs go to analysis/generated/.
"""
from pathlib import Path
import argparse
import hashlib
import io
import math
import re
import zipfile

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
META = ROOT / "data" / "metadata"
OUT = ROOT / "analysis" / "generated"


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def normalized(s):
    return re.sub(r"[^a-z0-9]", "", str(s).lower())


def read_zip(path):
    with zipfile.ZipFile(path) as z:
        csvs = [n for n in z.namelist() if n.lower().endswith(".csv")]
        preferred = [n for n in csvs if Path(n).name.lower() == "raw data.csv"]
        if preferred:
            name = preferred[0]
        elif len(csvs) == 1:
            name = csvs[0]
        else:
            raise ValueError(f"Cannot select Raw Data.csv from {csvs}")
        raw = z.read(name)
    frame = pd.read_csv(io.BytesIO(raw))
    cols = list(frame.columns)

    def choose_time():
        for c in cols:
            n = normalized(c)
            if n in ("time", "times", "timestamp", "timestamps"):
                return c
        return None

    def choose_axis(axis):
        # Match an axis token in common Phyphox labels such as
        # "Acceleration x (m/s^2)" and "Linear Acceleration x".
        pattern = re.compile(r"(?<![a-z])" + re.escape(axis) + r"(?![a-z])", re.I)
        for c in cols:
            label = str(c).lower()
            if pattern.search(label) and ("acceleration" in label or label.strip() == axis):
                return c
        return None

    tc = choose_time()
    axes = [choose_axis(a) for a in "xyz"]
    if tc is None or any(c is None for c in axes):
        raise ValueError(f"Unrecognized columns: {cols}")
    data = pd.DataFrame({
        "time_s": pd.to_numeric(frame[tc], errors="coerce"),
        "x": pd.to_numeric(frame[axes[0]], errors="coerce"),
        "y": pd.to_numeric(frame[axes[1]], errors="coerce"),
        "z": pd.to_numeric(frame[axes[2]], errors="coerce"),
    })
    n_raw = len(data)
    data = data.dropna().copy()
    data["magnitude"] = np.sqrt(data.x**2 + data.y**2 + data.z**2)
    return data, name, n_raw


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--motion", default="walking,static")
    parser.add_argument("--no-plots", action="store_true")
    args = parser.parse_args()

    inventory = pd.read_csv(META / "dataset_inventory.csv").fillna("")
    hashes = pd.read_csv(META / "dataset_sha256_mapping.csv").fillna("")
    expected = dict(zip(hashes.dataset_id, hashes.sha256.str.lower()))
    motions = {x.strip() for x in args.motion.split(",") if x.strip()}
    inventory = inventory[inventory.motion_type.isin(motions)]
    OUT.mkdir(parents=True, exist_ok=True)
    audit, features, curves = [], [], {"total": [], "linear": []}

    for _, row in inventory.iterrows():
        did = row.dataset_id
        path = RAW / row.repository_filename
        base = {"dataset_id": did, "repository_filename": row.repository_filename,
                "motion_type": row.motion_type, "phone_placement": row.phone_placement,
                "sensor_type": row.sensor_type}
        if not path.exists():
            audit.append({**base, "file_exists": False, "sha256_match": False,
                          "status": "missing_archive"})
            continue
        digest = sha256(path)
        match = digest == expected.get(did, "")
        try:
            df, member, raw_n = read_zip(path)
            dt = np.diff(df.time_s.to_numpy())
            pos = dt[dt > 0]
            med = float(np.median(pos)) if len(pos) else math.nan
            mag = df.magnitude.to_numpy()
            features.append({**base, "rows": len(df),
                "duration_s": float(df.time_s.iloc[-1] - df.time_s.iloc[0]),
                "estimated_hz": 1 / med if med > 0 else math.nan,
                "magnitude_mean": float(np.mean(mag)),
                "magnitude_sd": float(np.std(mag, ddof=1)),
                "magnitude_min": float(np.min(mag)),
                "magnitude_max": float(np.max(mag)),
                "magnitude_p95": float(np.percentile(mag, 95)),
                "magnitude_p99": float(np.percentile(mag, 99))})
            audit.append({**base, "file_exists": True, "sha256_match": match,
                "sha256_actual": digest, "csv_member": member, "raw_rows": raw_n,
                "valid_rows": len(df), "invalid_rows": raw_n-len(df),
                "nonpositive_dt_count": int(np.sum(dt <= 0)),
                "gaps_gt_1_5x_count": int(np.sum(dt > 1.5*med)) if med > 0 else 0,
                "estimated_hz": 1/med if med > 0 else math.nan,
                "status": "parsed_sha_match" if match else "parsed_sha_mismatch"})
            curves.setdefault(str(row.sensor_type).lower(), []).append((did, df))
        except Exception as e:
            audit.append({**base, "file_exists": True, "sha256_match": match,
                          "status": "parse_error", "detail": str(e)})

    pd.DataFrame(audit).to_csv(OUT / "archive_quality_audit.csv", index=False)
    pd.DataFrame(features).to_csv(OUT / "record_level_features.csv", index=False)
    if not args.no_plots:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        for sensor, records in curves.items():
            fig, ax = plt.subplots(figsize=(11, 5))
            for did, df in records:
                ax.plot(df.time_s, df.magnitude, lw=.65, label=did)
            ax.set(title=f"{sensor.title()} acceleration magnitude (full records)",
                   xlabel="Time (s)", ylabel="Magnitude (m/s²)")
            ax.legend(fontsize=6)
            ax.grid(alpha=.25)
            fig.tight_layout()
            fig.savefig(OUT / f"{sensor}_magnitude_overview.png", dpi=150)
            plt.close(fig)
    print(f"Processed {len(inventory)} inventory entries; inspect audit status before analysis.")


if __name__ == "__main__":
    main()

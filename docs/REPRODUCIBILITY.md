# Reproducible analysis guide

## Input data location

The scripts expect the 39 uniquely identified original ZIP archives in `data/raw/`, with filenames matching `repository_filename` in `data/metadata/dataset_inventory.csv`. The SHA-256 lookup is read from `data/metadata/dataset_sha256_mapping.csv`. The current GitHub repository tree contains 39 ZIP files in `data/raw/`.

## Environment

Recommended: Python 3.10 or newer. The analysis uses NumPy, pandas and Matplotlib.

From the repository root on Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-analysis.txt
python scripts/analyze_phyphox_archives.py
```

If PowerShell blocks activation, run the script with the virtual-environment interpreter directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-analysis.txt
.\.venv\Scripts\python.exe scripts/analyze_phyphox_archives.py
```

## What the script does

1. Reads dataset rows from `data/metadata/dataset_inventory.csv`.
2. Opens each selected original ZIP under `data/raw/` without extracting or modifying it.
3. Locates `Raw Data.csv` (or the only CSV in the archive), identifies time and X/Y/Z acceleration columns, and drops rows with non-numeric/missing values for numeric calculations.
4. Calculates SHA-256 and compares it with `data/metadata/dataset_sha256_mapping.csv`.
5. Calculates full-record magnitude statistics and timestamp quality indicators.
6. Writes generated outputs under `analysis/generated/`; optional overview plots are separated by sensor type.

Default scope of `analyze_phyphox_archives.py` is walking and static records:

```powershell
python scripts/analyze_phyphox_archives.py
```

To analyze all motion types with the baseline pipeline:

```powershell
python scripts/analyze_phyphox_archives.py --motion walking,static,running,upstairs,downstairs,mixed_stairs,downhill
```

The dedicated running/stairs analyses are separate scripts and produce their own tables and figures:

```powershell
python scripts/analyze_running_stairs.py
python scripts/analyze_action_deep_audit.py
```

These dedicated scripts require the original ZIPs in `data/raw/`; they write into `analysis/running_stairs/` and `analysis/action_deep_audit/` respectively. Review their reports for sensor/placement stratification and interpretation limits.

To skip plots:

```powershell
python scripts/analyze_phyphox_archives.py --no-plots
```

## Output files

- `archive_quality_audit.csv`: file presence, SHA-256 match, CSV row parsing and timestamp checks.
- `record_level_features.csv`: full-record descriptive features for each successfully parsed dataset.
- `total_magnitude_overview.png` / `linear_magnitude_overview.png`: full-record plots separated by sensor type.

## Important interpretation rules

- The script does not determine whether a person actually performed the labeled action.
- It does not decide whether a dataset is `selected`, `excluded` or `pending_verification`.
- It does not automatically trim phone placement/removal transitions or infer a stable walking interval.
- Total acceleration and Linear acceleration are kept in separate output plot files and must be analyzed as separate sensor strata.
- Full-record features include any start/end transition present in the raw recording. Do not interpret them as stable-gait-only features.
- SHA-256 mismatch, parse errors, missing files, non-monotonic timestamps or large gaps require investigation before using the corresponding record.

## Reproducibility and limitations

The script is a transparent baseline pipeline, not a validated gait classifier. It does not calculate cadence, step count, frequency-domain features, infer video synchronization, train a model, or report classification accuracy. Generated outputs are derived artifacts and should be committed only after reviewing the audit status and comparing results with the existing manual audit records.

# Raw Experimental Data

## 1. Purpose

This directory stores the original acceleration datasets exported from Phyphox.

It serves as the source of truth for subsequent data verification, preprocessing, feature extraction, and analysis.

## 2. Data Preservation Rules

1. Preserve original exported ZIP files without modifying their contents.
2. Do not overwrite original datasets with processed or cleaned versions.
3. Keep the original filenames recorded in `dataset_inventory.csv`.
4. Record standardized repository filenames separately.
5. Retain unsuccessful, inconsistent, and exploratory datasets for experimental traceability.
6. Do not classify a dataset as suitable for formal analysis before completing quality checks.

## 3. Dataset Organization

Original datasets will be stored in this directory.

Files should be organized using verified movement type, phone placement, sensor type, and collection information.

When metadata is uncertain, do not guess. Keep the original filename until verification is complete.

## 4. Data Verification

Before a dataset is used for formal analysis, verify:

- Movement category
- Phone placement
- Sensor type
- Sampling rate
- Recording duration
- Data completeness
- Potential measurement disturbances

## 5. Relationship with Other Directories

- `data/metadata/`: Dataset inventory and field definitions.
- `data/interim/`: Temporary intermediate data.
- `data/processed/`: Processed datasets.
- `data/selected/`: Datasets selected for formal analysis.

## 6. Current Status

Original datasets have not yet been fully inventoried and verified.

The dataset inventory will be updated progressively as each original file is examined.

## 7. Standardized Repository Filenames (2026-11-02)

The 39 ZIP entries have been matched one-to-one with the 39 rows in `data/metadata/dataset_inventory.csv`.

- All 39 ZIP paths are now named according to the corresponding `repository_filename` values in the inventory.
- `GAIT-C350D50D5DDB` is confirmed by the data collector as an upstairs trial. Its standardized filename is `GAIT-C350D50D5DDB_2026-10-29_upstairs_pocket_total.zip`.
- An experimental video exists for this collection period, but the exact video-to-dataset correspondence has not yet been established. The review matrix therefore keeps video linkage pending; this does not undo the action-label confirmation.
- The original filename remains in the `original_filename` field. The standardized name remains in `repository_filename`.
- The original SHA-256 mapping is retained in `data/metadata/dataset_sha256_mapping.csv`; `representative_filename` continues to identify the source/original filename.
- A per-dataset rename ledger is maintained at `data/metadata/filename_rename_log.csv`.

For the 38 path changes, the Git tree entries were redirected to the exact pre-existing blob SHAs. This preserves the stored ZIP blob content; no ZIP was extracted, recompressed, or rewritten. The SHA-256 values in the mapping table were not recalculated from a remote ZIP download during this operation.

## 8. Current Directory Status

There are 39 ZIP files in this directory, all using the standardized English filenames recorded in the inventory. All 39 have matching inventory rows. For `GAIT-C350D50D5DDB`, the action label is confirmed by the data collector; its exact video association remains pending.

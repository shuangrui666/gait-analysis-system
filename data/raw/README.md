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

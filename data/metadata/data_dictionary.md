# Dataset Data Dictionary

## 1. Purpose

This document defines the fields, naming conventions, and data classification rules used in `dataset_inventory.csv`.

The purpose is to ensure that all gait acceleration datasets are documented consistently, accurately, and traceably.

## 2. Field Definitions

| Field | Description | Example |
|---|---|---|
| dataset_id | Unique identifier for each dataset | GAIT-0001 |
| original_filename | Original filename before renaming | 静止含g.zip |
| repository_filename | Standardized filename used in the repository | 20261030_static_desktop_unknown_01.zip |
| collection_date | Actual data collection date | 2026-10-30 |
| motion_type | Movement or activity category | walking |
| phone_placement | Physical phone placement during collection | pocket |
| sensor_type | Acceleration sensor data type | total |
| sampling_rate_hz | Sampling rate in Hz | 500 |
| duration_seconds | Recording duration in seconds | 20.95 |
| experiment_id | Related experiment identifier | EXP-001 |
| data_status | Current data quality and verification status | pending_verification |
| analysis_usage | Whether the dataset is used in formal analysis | not_confirmed |
| notes | Additional information, limitations, or uncertainties | Sensor type requires verification |

## 3. Controlled Vocabulary

### 3.1 Motion Type

| Value | Meaning |
|---|---|
| static | Standing still or remaining stationary |
| walking | Normal walking |
| running | Running |
| upstairs | Walking upstairs |
| downstairs | Walking downstairs |
| downhill | Walking downhill |
| unknown | Movement category not yet verified |

### 3.2 Phone Placement

| Value | Meaning |
|---|---|
| handheld | Phone held in the hand |
| pocket | Phone placed in a pocket |
| desktop | Phone placed on a desk or table |
| unknown | Placement not yet verified |

### 3.3 Sensor Type

| Value | Meaning |
|---|---|
| total | Acceleration including gravity |
| linear | Linear acceleration with gravity removed |
| unknown | Sensor type not yet verified |

Sensor type must be determined from the actual Phyphox configuration and exported data fields. It must not be inferred from the filename alone.

### 3.4 Data Status

| Value | Meaning |
|---|---|
| exploratory | Preliminary experimental data |
| candidate | Potentially suitable for formal analysis |
| selected | Passed quality checks and selected for analysis |
| excluded | Not suitable for the intended analysis, but retained |
| pending_verification | Important metadata or quality information remains unverified |

### 3.5 Analysis Usage

| Value | Meaning |
|---|---|
| selected | Included in formal analysis |
| not_selected | Not included in formal analysis |
| not_confirmed | Analysis decision has not yet been made |

## 4. Data Recording Rules

1. Every dataset must have a unique `dataset_id`.
2. Original filenames must be preserved in `original_filename`.
3. Standardized filenames must not replace or erase original filenames.
4. Unknown information must be recorded as `unknown`, not guessed.
5. Collection dates must reflect actual collection dates.
6. Sensor types must be verified using the original data or collection settings.
7. Excluded datasets must be retained with a clear explanation.
8. Dataset status and analysis usage must be updated when verification is completed.

## 5. Data Traceability

Each dataset should be traceable from its original file to its standardized repository filename, experiment record, quality assessment, and final analysis.

Changes to dataset classification or usage should be documented rather than silently overwritten.

## 6. Maintenance

This document should be updated whenever new metadata fields, classification categories, or data management rules are introduced.

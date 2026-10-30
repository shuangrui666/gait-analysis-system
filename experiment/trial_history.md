# Experimental Trial History
# 实验迭代历史

> **Project:** Gait Analysis System  
> **Topic:** 多姿态步态加速度特征采集与对比  
> **Document status:** Initial version  
> **Purpose:** To document the evolution of the experimental design, identified limitations, and subsequent improvements.

---

## 1. Overview

This document records the development and iteration of the experimental methodology used in Topic 08.

The experiment initially focused on collecting acceleration data under different movement conditions. During the preliminary collection process, several differences in acquisition conditions were identified.

These findings motivated subsequent adjustments to phone placement, sensor configuration, and data organization.

This document distinguishes between completed activities, identified issues, and planned improvements. It does not imply that all standardization steps have been completed.

## 2. Iteration History

### Stage 1 — Preliminary Handheld Data Collection

**Status:** Completed

**Initial approach**

The Android smartphone was held by hand while acceleration data were collected using Phyphox.

The preliminary data covered several movement conditions, including static states, walking, running, and stair-related activities.

**Purpose**

- Explore the feasibility of collecting gait-related acceleration data.
- Become familiar with Phyphox data acquisition.
- Obtain initial measurements under different movement conditions.

**Limitations identified**

- Phone placement was not consistent with later pocket-placement measurements.
- Data were collected across multiple dates.
- Sensor types need to be checked individually.
- The acquisition conditions were not sufficiently standardized for direct comparison.

**Follow-up direction**

Retain the original measurements as exploratory data and investigate a more consistent phone-placement method.

### Stage 2 — Initial Static Measurement on a Desk

**Status:** Completed

**Approach**

The smartphone was placed on a desk while Phyphox recorded acceleration data.

**Purpose**

Obtain a stationary reference measurement.

**Limitation identified**

A phone resting on a desk does not have the same measurement conditions as a phone carried in a trouser pocket.

The two conditions should therefore be distinguished during data organization and analysis.

**Improvement decision**

Keep desktop static data separately and avoid labeling it as pocket-placement static data.

### Stage 3 — Pocket-Placement Static Measurement

**Status:** Completed

**Approach**

The smartphone was placed inside a trouser pocket while the participant stood naturally in place without walking. Acceleration data were recorded continuously using Phyphox.

**Purpose**

Obtain static measurements under a phone-placement condition closer to the intended pocket-placement movement experiments.

**Improvement**

The phone placement and human activity condition were made explicit:

- Phone placement: Trouser pocket
- Human activity: Standing still
- Movement: No walking

**Remaining verification**

- Original data filename
- Collection date
- Sensor type
- Sampling rate
- Acquisition duration
- Associated video evidence, if available

**Data handling decision**

Classify this dataset separately under `data/raw/static/pocket/` after its original file has been identified.

### Stage 4 — Pocket-Placement Movement Data Collection

**Status:** Partially completed; individual datasets require verification

**Approach**

Pocket-placement data were collected for some movement conditions.

The available historical files include walking and stair-related measurements. Other files include downhill walking and measurements with changing phone-holding posture.

**Purpose**

Explore acceleration characteristics under different movement conditions and investigate the feasibility of a more consistent phone-placement method.

**Issues requiring verification**

- Whether all pocket-placement recordings used the same sensor type.
- Whether phone placement was consistent across recordings.
- Whether acquisition parameters were consistent.
- Whether the movement speed and route were sufficiently comparable.
- Whether the beginning of a recording contains placement-related disturbances.

**Follow-up direction**

Verify each original dataset before deciding whether it can be used for formal comparisons.

### Stage 5 — Acquisition Standardization and Data Verification

**Status:** In progress

**Objective**

Establish consistent acquisition conditions for formal data collection and comparison.

**Conditions to verify or standardize**

| Variable | Intended requirement |
|---|---|
| Smartphone | Use the same Android phone where possible |
| Acquisition software | Phyphox |
| Phone placement | Trouser pocket |
| Walking speed | Normal speed for the normal-walking category |
| Sensor type | Use the same verified sensor type |
| Sampling rate | Use a consistent configured rate |
| Acquisition duration | Record and document actual duration |
| Motion category | Clearly distinguish each movement condition |

**Verification tasks**

1. Identify the sensor type used in every dataset.
2. Check original CSV fields and acquisition settings.
3. Record collection dates and durations.
4. Identify datasets with inconsistent placement or acquisition conditions.
5. Preserve exploratory data separately from standardized data.
6. Record any additional measurements required.

**Expected outcome**

A documented and traceable dataset collection suitable for quality assessment and subsequent analysis.

## 3. Key Issues Identified

| Issue | Impact | Current handling |
|---|---|---|
| Different phone placements | Measurement conditions differ | Separate handheld, desktop, and pocket datasets |
| Multiple collection dates | Acquisition batches may differ | Record dates and batches individually |
| Sensor type uncertainty | Acceleration measurements may not be comparable | Verify original CSV fields and settings |
| Different movement conditions | Motion categories may be confused | Use explicit movement labels |
| Recording start disturbance | Initial measurements may contain placement-related effects | Inspect raw signals before deciding whether to exclude segments |
| Incomplete evidence association | Experimental traceability is reduced | Build an evidence index |

## 4. Data Retention Strategy

All original measurements should be retained.

Datasets are organized according to their actual acquisition conditions rather than being silently discarded when they do not meet the intended standardized protocol.

The project distinguishes between:

- **Exploratory data:** Measurements collected during preliminary experiments.
- **Candidate data:** Measurements that may be suitable for formal analysis but still require verification.
- **Selected data:** Measurements that have passed the defined quality checks.
- **Excluded data:** Measurements retained for traceability but not used in a particular formal analysis.

Final classification will be documented in `data/metadata/dataset_inventory.csv`.

## 5. Current Project Status

The project has completed preliminary handheld measurements, desktop static measurement, and pocket-placement static measurement.

Some pocket-placement movement measurements have also been collected.

The complete dataset inventory, sensor verification, acquisition-condition assessment, and formal selection of analysis datasets remain in progress.

## 6. Next Steps

1. Complete the inventory of all original data files.
2. Verify the acquisition date, movement category, phone placement, and sensor type for each file.
3. Associate data files with their experiment records.
4. Identify datasets requiring additional verification or repeated measurement.
5. Finalize the standardized acquisition protocol.
6. Perform data quality checks before formal feature extraction and comparison.

---

**Record principle:** Each iteration must be supported by actual experimental records or data. Planned improvements must not be presented as completed experimental results.

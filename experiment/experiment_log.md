# Experiment Log
# 课题08实验日志

> **Document status:** Initial version  
> **Project:** Gait Analysis System  
> **Topic:** 多姿态步态加速度特征采集与对比  
> **Record policy:** All records must reflect actual experimental activities. Unverified information must be explicitly marked.

---

## 1. Purpose

This document maintains the chronological record of experimental activities for Topic 08.

It covers:

- Experimental preparation and data acquisition
- Sensor and phone-placement conditions
- Raw data file references
- Video and other experimental evidence
- Observations, problems, and corrective actions
- Experimental decisions and protocol changes

The purpose is to make the experimental process traceable, reproducible, and auditable.

## 2. Record Management Rules

1. Record activities according to their actual occurrence dates.
2. Do not combine data collected on different dates or under different conditions into one experimental record without justification.
3. Preserve original raw data files. Never overwrite original measurements with processed results.
4. Record the actual phone placement, sensor type, sampling rate, and acquisition duration whenever known.
5. Distinguish confirmed facts, observations, interpretations, and unverified information.
6. Use `To be verified` when information has not yet been confirmed.
7. Link each experimental record to its corresponding raw data and evidence files whenever possible.
8. Record failed attempts and protocol changes instead of silently discarding them.
9. Do not claim that an experiment was completed unless it was actually performed.
10. Assign final experiment IDs only after the collection dates and experimental batches have been checked.

## 3. Known Experimental Activities

The following activities have been confirmed from the current project history. Their dates, file associations, and final experiment IDs still need to be verified.

### 3.1 Early Handheld Data Collection

- Record ID: Pending assignment
- Collection dates: Multiple dates; exact dates to be verified
- Experimental stage: Preliminary exploration
- Acquisition software: Phyphox
- Phone placement: Handheld
- Sensor type: To be verified for each dataset
- Sampling rate: To be verified
- Collection environment: To be verified

**Motion categories involved**

- Static
- Walking
- Running
- Stair-related activities

**Raw data references**

The early handheld collection includes multiple original ZIP files. The exact file-to-date and file-to-activity mapping will be documented in `data/metadata/dataset_inventory.csv`.

**Known limitation**

The early datasets were collected across multiple dates. Phone placement and sensor types were not fully consistent across all files.

**Data handling decision**

Retain these datasets as preliminary or exploratory data. Do not automatically combine them with later standardized pocket-placement data.

### 3.2 Static Measurement — Desktop Placement

- Record ID: Pending assignment
- Collection date: To be verified
- Experimental stage: Preliminary static measurement
- Acquisition software: Phyphox
- Phone placement: On a desk
- Human activity: Not applicable to the phone's placement condition
- Sensor type: To be verified
- Sampling rate: To be verified

**Purpose**

To collect acceleration measurements while the phone was stationary on a desk.

**Raw data reference**

`静止含g.zip`

**Known condition**

The phone was placed on a desk during this measurement. This dataset must not be labeled as a pocket-placement static measurement.

**Data handling decision**

Keep this dataset separately from pocket-placement static data. It may be useful as a reference for stationary sensor behavior, but its different placement condition must be considered during analysis.

### 3.3 Static Measurement — Pocket Placement

- Record ID: Pending assignment
- Collection date: To be verified
- Experimental stage: Follow-up static measurement
- Acquisition software: Phyphox
- Phone placement: Inside a trouser pocket
- Human activity: Standing naturally in place without walking
- Sensor type: To be verified
- Sampling rate: To be verified

**Purpose**

To collect acceleration measurements with the phone inside a trouser pocket while the participant remains stationary.

**Experimental procedure**

1. Place the phone inside the trouser pocket.
2. Stand naturally in place.
3. Remain stationary without walking.
4. Record acceleration data continuously using Phyphox.

**Raw data reference**

To be linked after the corresponding original file is identified.

**Evidence reference**

To be linked if a corresponding recording or other evidence is available.

**Known distinction**

This is a completed pocket-placement static measurement. It is a different experimental condition from the desktop static measurement described in Section 3.2.

**Data handling decision**

Classify this measurement under `data/raw/static/pocket/` after identifying its original file. Do not substitute the desktop static dataset for it.

## 4. Standardized Data Collection Records

Future standardized collection activities should be recorded using the template below.

### EXP-XXX: [Activity Name]

- Experiment date: YYYY-MM-DD
- Experiment stage: Preliminary / Standardized / Follow-up
- Acquisition software: Phyphox
- Phone model: To be recorded
- Phone placement: To be recorded
- Motion category: To be recorded
- Sensor type: To be verified
- Sampling rate: To be recorded
- Acquisition duration: To be recorded
- Collection environment: To be recorded
- Operator: To be recorded if relevant

#### 4.1 Objective

Describe the purpose of this experimental activity.

#### 4.2 Experimental Conditions

Describe the phone placement, movement conditions, sensor configuration, and other relevant variables.

#### 4.3 Procedure

Record the actual steps performed, in chronological order.

#### 4.4 Raw Data

List the original filenames and their repository paths.

#### 4.5 Evidence

List associated video filenames, photographs, or other evidence. If no evidence exists, state `Not available`.

#### 4.6 Observations

Record directly observed facts. Do not mix interpretations with observations.

#### 4.7 Problems and Limitations

Record unexpected events, inconsistent conditions, measurement errors, or other limitations.

#### 4.8 Results and Interpretation

Summarize only findings supported by the available data. Mark unverified interpretations clearly.

#### 4.9 Conclusion and Next Actions

Record the conclusions and any follow-up actions required.

## 5. Data and Evidence Traceability

Each experimental record should be linked to the following items when available:

| Item | Repository location |
|---|---|
| Original measurements | `data/raw/` |
| Dataset metadata | `data/metadata/dataset_inventory.csv` |
| Experimental videos | `evidence/videos/` |
| Evidence index | `evidence/evidence_index.csv` |
| Protocol changes | `experiment/protocol_changes.md` |
| Trial history | `experiment/trial_history.md` |
| Troubleshooting | `experiment/troubleshooting.md` |

The dataset inventory is the authoritative index for original data filenames and their verified metadata.

## 6. Quality and Reproducibility Requirements

Before a dataset is used for formal comparison, verify as many of the following items as applicable:

- Motion category is correctly identified.
- Phone placement is known.
- Sensor type is confirmed from the data or acquisition configuration.
- Sampling rate is checked.
- Acquisition duration is recorded.
- Relevant collection conditions are documented.
- Data integrity is checked.
- Any excluded or invalid segments are documented.
- The original raw file is preserved.

Datasets with incompatible or unknown conditions must not be treated as directly comparable without an explicit justification.

## 7. Revision History

| Version | Date | Description |
|---|---|---|
| 0.1 | To be recorded | Initial experiment log structure created |

---

**Documentation principle:** This log records what actually happened, not what was intended to happen. Any correction must preserve the distinction between original records and later verified information.

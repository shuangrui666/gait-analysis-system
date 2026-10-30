# Experimental Troubleshooting
# 实验问题排查记录

> **Project:** Gait Analysis System  
> **Topic:** 多姿态步态加速度特征采集与对比  
> **Document status:** Initial version

---

## 1. Purpose

This document records problems identified during data acquisition, data organization, and experimental preparation.

Each issue should include its description, potential impact, investigation, corrective action, and verification status.

Unverified causes must be treated as hypotheses rather than confirmed conclusions.

## 2. Issue Records

### ISSUE-001: Inconsistent Phone Placement

- Status: Identified
- Severity: To be assessed
- Related stage: Preliminary data collection

**Description**

Early measurements included handheld phone placement, while later measurements included trouser-pocket placement.

**Potential impact**

Different phone placements may change the measured acceleration signals and reduce the comparability of datasets.

**Investigation**

Review the original filenames, acquisition records, and available evidence to identify the placement condition of each dataset.

**Corrective action**

Classify datasets according to their actual placement conditions. Keep handheld and pocket-placement measurements separate.

**Verification**

Pending dataset-by-dataset inspection.

---

### ISSUE-002: Different Static Measurement Conditions

- Status: Identified
- Severity: To be assessed
- Related stage: Static data acquisition

**Description**

Two static measurement conditions were used:

1. Smartphone placed on a desk.
2. Smartphone placed in a trouser pocket while the participant stood still.

**Potential impact**

The two conditions involve different physical constraints and should not be treated as identical measurements.

**Corrective action**

Store the two datasets separately under their corresponding placement categories.

**Verification**

The distinction between desktop and pocket-placement measurements has been confirmed. Original file associations still need to be checked.

---

### ISSUE-003: Unverified Acceleration Sensor Types

- Status: Investigation required
- Severity: To be assessed
- Related stage: Data verification

**Description**

Historical datasets may include total acceleration with gravity and linear acceleration with gravity removed.

**Potential impact**

Mixing different sensor outputs may lead to misleading comparisons and feature calculations.

**Investigation**

Inspect original CSV headers, Phyphox experiment configuration, and available acquisition records.

**Corrective action**

Record the verified sensor type for each dataset. Use `unknown` until verification is complete.

**Verification**

Pending individual dataset inspection.

---

### ISSUE-004: Possible Initial Recording Disturbance

- Status: Potential issue requiring inspection
- Severity: To be assessed
- Related stage: Pocket-placement data acquisition

**Description**

For some measurements, recording may have started before the phone was placed inside the trouser pocket.

**Potential impact**

Movement during phone placement may introduce transient acceleration signals at the beginning of a recording.

**Investigation**

Inspect the initial signal segments and compare them with the corresponding experimental procedure or video evidence, if available.

**Corrective action**

If an invalid initial segment is confirmed, document the exclusion boundary and processing method. Preserve the original data.

**Verification**

Pending signal inspection. Do not assume that every recording contains this disturbance.

---

### ISSUE-005: Incomplete Dataset Metadata

- Status: Open
- Severity: To be assessed
- Related stage: Data management

**Description**

Some historical files still require confirmation of collection date, sensor type, placement, and acquisition parameters.

**Potential impact**

Incomplete metadata reduces traceability and may prevent reliable comparison or reproduction.

**Corrective action**

Create and maintain `data/metadata/dataset_inventory.csv` to record the verified information for every dataset.

**Verification**

Pending completion of the dataset inventory.

---

## 3. Issue Status Definitions

| Status | Meaning |
|---|---|
| Identified | A problem has been observed or reported |
| Investigation required | The cause or impact needs further inspection |
| In progress | Investigation or corrective action is underway |
| Resolved | A corrective action has been completed |
| Verified | The correction has been checked and supported by evidence |
| Closed | The issue has been resolved, verified, and documented |

## 4. Troubleshooting Record Requirements

For each new issue, record:

1. Issue ID.
2. Date identified.
3. Related experiment or dataset ID.
4. Problem description.
5. Potential impact.
6. Investigation method.
7. Corrective action.
8. Verification evidence.
9. Current status.

## 5. Revision History

| Version | Date | Description |
|---|---|---|
| 0.1 | To be recorded | Initial troubleshooting record created |

---

**Troubleshooting principle:** Do not mark an issue as resolved merely because a corrective action has been proposed. Verification must be based on actual inspection or experimental evidence.

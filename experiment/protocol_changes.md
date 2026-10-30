# Experimental Protocol Changes
# 实验方案变更记录

> **Project:** Gait Analysis System  
> **Topic:** 多姿态步态加速度特征采集与对比  
> **Document status:** Initial version

---

## 1. Purpose

This document records changes to the experimental protocol, including the original conditions, identified limitations, reasons for modification, and the resulting decisions.

The purpose is to ensure that changes to experimental conditions are transparent, traceable, and scientifically justified.

A planned change must not be described as an implemented change until it has actually been performed.

## 2. Protocol Change Records

### PC-001: Addition of Pocket-Placement Static Measurement

- Change status: Implemented
- Change date: To be verified
- Related experiment: To be assigned
- Related data: Original filename to be identified

**Original condition**

The smartphone was placed on a desk during the initial static measurement.

**Identified limitation**

A phone resting on a desk does not represent the same measurement condition as a phone carried in a trouser pocket.

**Modification**

A separate static measurement was performed with the smartphone inside a trouser pocket while the participant stood naturally in place without walking.

**Reason for modification**

To obtain static acceleration measurements under a phone-placement condition closer to the intended pocket-placement movement experiments.

**Resulting decision**

Desktop static measurements and pocket-placement static measurements must be stored and identified separately.

**Verification still required**

- Original data filename
- Collection date
- Sensor type
- Sampling rate
- Acquisition duration
- Associated evidence, if available

---

### PC-002: Standardization of Phone Placement

- Change status: Partially implemented
- Change date: To be verified
- Related experiments: To be assigned

**Original condition**

Early measurements included handheld phone placement. Later measurements included pocket placement.

**Identified limitation**

Different phone placements can affect the recorded acceleration signals and make direct comparisons less reliable.

**Modification direction**

Use trouser-pocket placement for the intended standardized movement measurements.

**Reason for modification**

To reduce variation caused by inconsistent phone placement.

**Current limitation**

Historical measurements collected by hand must remain classified as exploratory data unless their conditions are independently assessed.

**Next action**

Verify the placement condition of each original dataset and document any exceptions.

---

### PC-003: Verification of Acceleration Sensor Type

- Change status: Verification in progress
- Change date: To be verified
- Related datasets: Historical datasets

**Identified issue**

Historical datasets may contain different acceleration measurements, including total acceleration with gravity and linear acceleration with gravity removed.

**Required action**

Check the original Phyphox configuration and CSV column names for each dataset.

**Standardization direction**

Select a consistent sensor type for formal comparisons and document the exact configuration.

**Important note**

Sensor type must not be inferred solely from an original filename. Unverified datasets must be labeled as unknown until checked.

---

## 3. Change Management Rules

Every protocol change should include:

1. A unique change ID.
2. The original experimental condition.
3. The identified problem or limitation.
4. The reason for modification.
5. The actual modification or proposed direction.
6. The implementation status.
7. Related experiment IDs and dataset IDs.
8. Any remaining verification tasks.

## 4. Change Status Definitions

| Status | Meaning |
|---|---|
| Proposed | A change has been suggested but not implemented |
| In progress | Implementation or verification is ongoing |
| Implemented | The change has actually been performed |
| Verified | The changed condition has been checked and documented |
| Rejected | The proposed change was not adopted |

## 5. Revision History

| Version | Date | Description |
|---|---|---|
| 0.1 | To be recorded | Initial protocol change record created |

---

**Change management principle:** Every change must have a documented reason and an accurate implementation status. Historical data must never be silently relabeled to make it appear that the new protocol was used.

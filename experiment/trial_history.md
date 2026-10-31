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

## 2026-10-31：原始数据重复文件调查（第一阶段）

### 1. 问题背景

在课题八实验数据采集和文件整理过程中，由于多次复制、导出和保存，产生了大量带有“副本”“(1)”“(2)”等后缀的 ZIP 文件。

此前曾根据文件名判断并删除部分疑似重复文件。由于没有逐个核对文件内容，无法保证删除操作的准确性。发现这一风险后，已从 Windows 回收站恢复此前删除的 ZIP 文件。

### 2. 原始数据归档

建立独立的数据管理目录，将原始 ZIP 文件复制到 `01_raw_original` 文件夹。

当前归档数量：102 个 ZIP 文件。

原始文件仍保留在原存储位置，没有对归档文件执行删除或修改。

### 3. SHA-256 校验

使用 Windows PowerShell 的 `Get-FileHash` 命令，对 102 个 ZIP 文件计算 SHA-256 校验值，并生成：

`02_archive_manifest/sha256_manifest.csv`

初步统计结果：

| 项目 | 结果 |
|---|---:|
| 原始 ZIP 文件总数 | 102 |
| 不同内容组数 | 39 |
| 存在重复的文件组数 | 16 |
| 重复组内文件总数 | 79 |
| 理论多余副本数 | 63 |

### 4. 典型重复组调查：静止2

进一步调查发现，一个重复组包含 19 个 ZIP 文件。

- 基础文件名：`静止2.zip`
- 文件数量：19
- 文件大小：均为 250798 字节
- SHA-256：`3FBAB2CC336671DC0FF3C60C813F0E69584E676B989CBD2F649ECDABD60008CE`

这 19 个文件的 SHA-256 完全相同，确认它们的文件内容一致。

文件名主要区别是不断增加的“副本”和数字后缀。

### 5. 初步结论

该组 19 个文件属于同一份文件内容的多个副本，不能视为 19 次独立实验采集。

结合已有实验记录，该文件对应桌面静止采集数据。后续应以原始实验记录和数据元信息核对其具体实验属性。

### 6. 当前处理决定

1. 暂时保留全部 102 个原始 ZIP 文件。
2. 不根据文件名直接删除副本。
3. 已生成 SHA-256 校验清单和重复文件审查表。
4. 暂定 `静止2.zip` 为代表文件，但尚未执行物理删除。
5. 后续继续调查其余 15 个重复组。

### 7. 工程反思

本次调查发现，原有文件管理方式缺少统一归档和可靠的重复文件识别机制。

后续采用“原始数据保护—哈希校验—重复审查—备份确认—处理记录”的流程，提高数据完整性和实验可追溯性。

**当前状态：第一阶段调查完成，剩余重复组调查及备份验证待完成。**

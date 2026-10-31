# Experimental Trial History
# 实验迭代历史

> **Project:** Gait Analysis System  
> **Topic:** 多姿态步态加速度特征采集与对比  
> **Document status:** Revised working version  
> **Purpose:** To document the actual experimental process, trial-and-error experiences, identified limitations, methodological adjustments, and verification status.

---

## 1. Overview

本文档记录课题八“多姿态步态加速度特征采集与对比”从初期数据采集到实验方法逐步调整的过程。

实验初期，采集者对 Phyphox 的传感器类型、手机放置方式、采样率及数据管理方法还不熟悉，因此早期数据存在采集条件不统一、动作分类不够明确等情况。

在实际采集、数据整理以及与 AI 工具交流的过程中，逐渐发现这些问题，并对后续采集方法和数据管理方式进行了调整。

本文档遵循以下原则：

1. 记录真实发生过的实验过程，不隐瞒早期试错。
2. 区分已经完成的调整和仍处于计划阶段的调整。
3. 不将新增数据自动视为改进效果已经得到验证。
4. 保留早期探索数据，以便追溯实验方法的变化。
5. 对无法确认的日期、文件和参数标注为待核实。

## 2. Iteration History

### Stage 1 — Preliminary Handheld Data Collection
### 第一阶段：初期手持手机采集

**Date / Batch:** 2026-10-24，初期采集批次  
**Status:** Completed

**1. Initial method — 当时采用的方法**

使用 Android 手机和 Phyphox 采集不同运动状态下的加速度数据。

初期采用手持手机的方式，采集了静止、慢走、跑步以及上下楼梯等运动数据。采集过程中，手臂可以自然摆动，手机姿势也可能随动作发生变化。

部分已知文件包括：

- `上下楼梯1。(1).zip`
- `上下楼梯2。(1).zip`
- `上下楼梯3。(1).zip`
- `慢走三。(1).zip`
- `快跑一。(1).zip`
- `快跑2`、`快跑3`

**2. Identified problems — 发现的问题**

- 手持采集时，手机姿势和摆动可能发生变化。
- 不同采集批次的手机放置条件不一致。
- 部分数据使用总加速度传感器，部分使用线性加速度传感器。
- 部分数据采样率为 100Hz，部分为 500Hz。
- 部分上下楼梯数据包含上楼和下楼两个动作。

**3. Why it was considered a problem — 为什么认为这是问题**

通过实际采集和后续与 AI 的讨论，逐渐认识到：

- 手机姿势和位置变化会影响加速度信号。
- 不同手机放置条件下的数据不宜直接视为相同实验条件。
- 总加速度与线性加速度包含的物理成分不同。
- 不同采样率会影响时间分辨率和后续特征计算。
- 上楼和下楼属于不同运动条件，混合记录会增加动作分类难度。

因此，早期数据可以用于探索，但不宜在没有区分采集条件的情况下直接用于正式比较。

**4. Adjustments — 做出的调整**

- 保留早期手持数据，作为探索性数据。
- 开始考虑采用裤袋放置方式，减少不同实验之间的手机放置差异。
- 后续整理数据时，分别标注手持、桌面和裤袋条件。
- 对传感器类型、采样率和动作类别进行单独核查。

**5. Re-collection — 是否重新采集**

已进行后续裤袋方式的重新采集。后续批次包括走路、跑步、上楼梯和下楼梯等动作。

**6. Verification — 改进效果是否经过数据验证**

目前可以确认后续已经采集了新的裤袋数据，但尚不能仅凭采集方式变化认定数据质量已经提高。

仍需通过原始信号、采集参数和数据质量检查进行验证。

---

### Stage 2 — Static Measurement on a Desk
### 第二阶段：桌面静止实验

**Date / Batch:** 2026-10-22、2026-10-27，具体文件对应关系待核实  
**Status:** Completed

**1. Initial method — 当时采用的方法**

将手机放置在桌面上，使用 Phyphox 记录静止状态下的加速度数据。

已确认的文件包括：

- `静止2.zip`：2026-10-22 08:58:32，手机全程放在桌面上，总加速度，500Hz，20.88 秒。
- `静止含g.zip`：2026-10-27 11:18:57，手机全程放在桌面上，总加速度，500Hz，20.95 秒。

**2. Identified problems — 发现的问题**

后续实验还出现了手机放在裤袋中的静止测量。桌面静止和裤袋静止容易在文件整理时被混淆。

**3. Why it was considered a problem — 为什么认为这是问题**

桌面放置和裤袋放置具有不同的固定方式及测量环境。

即使人体都处于静止状态，手机与人体之间的相对位置和约束条件也不同，因此不能把两种数据不加区分地归为同一种采集条件。

**4. Adjustments — 做出的调整**

- 明确区分 `desktop` 和 `pocket` 两种手机放置方式。
- 将桌面静止数据保留为独立实验条件。
- 不将桌面静止数据误标为裤袋静止数据。

**5. Re-collection — 是否重新采集**

后续存在裤袋静止实验，但其原始文件名、日期和具体参数仍需核对。

**6. Verification — 改进效果是否经过数据验证**

已明确桌面静止与裤袋静止的实验条件区别，但两种数据的信号差异尚未完成系统对比。

---

### Stage 3 — Pocket-Placement Static Measurement
### 第三阶段：裤袋静止实验

**Date / Batch:** 具体日期及文件待核实  
**Status:** Completed; metadata verification pending

**1. Initial method — 当时采用的方法**

将手机放入裤袋，在人体保持站立、不进行走路动作的情况下，使用 Phyphox 采集加速度数据。

**2. Identified problems — 发现的问题**

初期桌面静止数据不能代表手机放在裤袋中的静止状态，因此需要补充另一种实验条件。

**3. Why it was considered a problem — 为什么认为这是问题**

本项目后续需要研究手机放在裤袋中时的步态加速度特征。桌面静止数据与裤袋静止数据的测量条件不同，不能直接互相替代。

**4. Adjustments — 做出的调整**

增加裤袋静止测量，并明确记录：

- Phone placement: Pocket
- Human activity: Standing still
- Motion: Static

**5. Re-collection — 是否重新采集**

已完成裤袋静止测量，但需要通过原始 ZIP 文件进一步确认具体采集批次。

**6. Verification — 改进效果是否经过数据验证**

目前完成了实验条件的区分，尚需核实原始文件、传感器类型、采样率、持续时间及相关证据。

---

### Stage 4 — Transition from Handheld to Pocket Placement
### 第四阶段：从手持采集转向裤袋采集

**Date / Batch:** 2026-10-28 至 2026-10-29，裤袋采集批次  
**Status:** Re-collection completed; comparative verification pending

**1. Initial method — 当时采用的方法**

初期使用手持方式采集运动数据，后来开始尝试将手机放入裤袋中进行运动采集。

**2. Identified problems — 发现的问题**

- 手持手机时，手机姿势和摆动可能不稳定。
- 不同动作之间的手机放置条件需要尽可能保持一致。
- 手持数据和裤袋数据不适合在不区分条件的情况下直接比较。

**3. Why it was considered a problem — 为什么认为这是问题**

最初对步态加速度采集方法不够熟悉。

在实际采集过程中，逐渐观察到手持手机时手机姿势和摆动可能发生变化。与此同时，本项目需要比较不同动作下的加速度特征，因此需要尽量控制手机放置条件。

通过与 AI 工具讨论，也进一步认识到手机放置方式会影响加速度数据的可比性，并了解到裤袋放置可以作为本项目较统一的采集方式。

这一调整来自实际观察、实验需求和 AI 辅助讨论，而不是一开始就确定好的实验方案。

**4. Adjustments — 做出的调整**

逐渐采用裤袋放置作为后续主要采集方式。

后续采集时，将手机放入裤袋，记录走路、跑步、上楼梯和下楼梯等动作。

同时保留此前的手持数据，不将其直接删除或伪装成裤袋数据。

**5. Re-collection — 是否重新采集**

已重新采集相关动作的裤袋数据。

已知后续采集批次包括：

- 2026-10-28：走路、下楼梯、下坡等裤袋数据。
- 2026-10-29：走路、跑步、上楼梯和下楼梯等裤袋数据。

具体文件与动作的对应关系以原始 ZIP 文件和数据清单为准。

**6. Verification — 改进效果是否经过数据验证**

已经完成从手持方式到裤袋方式的后续重新采集。

但是，重新采集只证明采集方式发生了调整，并不直接证明改进效果。

后续还需要检查手机放置是否一致、原始信号是否存在明显异常，以及不同采集批次之间是否具有可比性。

---

### Stage 5 — Sensor Type and Sampling Rate Differences
### 第五阶段：传感器类型和采样率不统一

**Date / Batch:** 主要涉及 2026-10-24 及后续采集批次  
**Status:** Issue identified; verification and standardization in progress

**1. Initial method — 当时采用的方法**

初期使用 Phyphox 采集数据时，使用过不同的加速度传感器输出和不同采样率。

已知早期数据中存在：

- Total acceleration（总加速度，含重力分量）
- Linear acceleration（线性加速度，去除重力分量）
- 100Hz
- 500Hz

**2. Identified problems — 发现的问题**

不同文件的传感器类型和采样率不一致。

**3. Why it was considered a problem — 为什么认为这是问题**

总加速度和线性加速度的物理含义不同，不能不加区分地混合比较。

采样率不同会导致时间分辨率不同，也可能影响后续信号处理、特征提取和数据对齐。

如果不记录这些差异，可能会将传感器配置造成的差异误认为动作本身的差异。

**4. Adjustments — 做出的调整**

- 决定逐个检查原始数据的传感器类型。
- 将总加速度和线性加速度分别标注。
- 记录各文件实际采样率。
- 后续正式采集计划使用统一的传感器类型和采样率。

**5. Re-collection — 是否重新采集**

后续 2026-10-28 至 2026-10-29 的多个裤袋采集文件使用总加速度、500Hz 配置。

但是否所有正式候选数据都满足统一配置，仍需逐个核查。

**6. Verification — 改进效果是否经过数据验证**

已经发现并记录配置差异，也有后续采用相同配置采集的数据。

尚未完成全部文件的传感器和采样率核查，也尚未完成不同配置数据的系统对比。

---

### Stage 6 — Motion Category Classification
### 第六阶段：动作分类与采集条件区分

**Date / Batch:** 主要涉及 2026-10-24 及后续采集批次  
**Status:** Classification issue identified; inventory verification in progress

**1. Initial method — 当时采用的方法**

初期采集上下楼梯数据时，部分记录包含上楼和下楼两个方向的动作。

后续逐渐开始分别采集上楼梯和下楼梯数据。

此外，项目还涉及下坡行走。

**2. Identified problems — 发现的问题**

- 部分早期上下楼梯记录包含混合动作。
- 上楼和下楼没有始终分开采集。
- 下坡行走容易与下楼梯混淆。

**3. Why it was considered a problem — 为什么认为这是问题**

上楼梯、下楼梯和下坡行走是不同的运动条件，运动过程和加速度特征可能存在差异。

如果把不同动作混在同一类别中，可能影响后续数据标注、特征比较和动作识别分析。

**4. Adjustments — 做出的调整**

- 后续分别采集上楼梯和下楼梯。
- 将下坡行走单独标记。
- 对早期混合动作数据保留原始记录，并标记为混合动作或待核实，不强行归入单一动作类别。

**5. Re-collection — 是否重新采集**

后续已经分别采集裤袋条件下的上楼梯和下楼梯数据，也采集了下坡行走数据。

**6. Verification — 改进效果是否经过数据验证**

已经有分开采集的数据文件，但仍需逐个核对动作标签、采集过程和原始信号，才能确认数据是否适合正式比较。

---

### Stage 7 — Recording Start and Phone Placement Procedure
### 第七阶段：录制启动与手机放置流程探索

**Date / Batch:** 后续采集流程探索，具体日期待核实  
**Status:** Procedure exploration; signal verification pending

**1. Initial method — 当时采用的方法**

采集时曾考虑先启动 Phyphox 录制，再将手机放入口袋。

同时探索过通过电脑远程控制 Phyphox 的方法，并考虑使用平板记录实验过程。

**2. Identified problems — 发现的问题**

开始录制后再将手机放入口袋，可能导致录制开始阶段出现手机位置和姿态变化。

通过电脑远程控制也未能完全解决启动录制时的操作问题。

**3. Why it was considered a problem — 为什么认为这是问题**

手机放入口袋的过程中可能产生额外运动信号。如果不检查原始数据，可能无法区分这些信号是实际步态还是放置手机时产生的干扰。

**4. Adjustments — 做出的调整**

将录制开始阶段的信号检查纳入后续数据质量检查。

不直接假设开头一定存在异常，也不在没有检查的情况下随意删除开头数据。

**5. Re-collection — 是否重新采集**

是否因为该问题专门重新采集，目前没有足够记录确认。

**6. Verification — 改进效果是否经过数据验证**

尚未完成录制启动阶段的系统性信号检查。

后续应结合原始加速度时间序列，判断是否存在明显的放置过程干扰，并记录处理依据。

---

### Stage 8 — Original Data Duplication and Recovery
### 第八阶段：原始数据重复文件调查与恢复

**Date / Batch:** 2026-10-31，数据管理批次  
**Status:** First-stage investigation completed; further review pending

**1. Initial method — 当时采用的方法**

在课题八实验数据采集和文件整理过程中，多次复制、导出和保存 ZIP 文件，产生了大量带有“副本”“(1)”“(2)”等后缀的文件。

此前曾根据文件名判断并删除部分疑似重复文件。

**2. Identified problems — 发现的问题**

仅凭文件名无法确认两个 ZIP 文件的内容是否相同。

在没有核对文件内容的情况下删除文件，存在误删唯一实验数据的风险。

**3. Why it was considered a problem — 为什么认为这是问题**

实验原始数据是后续分析和结果复核的依据。

如果误删唯一的数据文件，可能造成实验记录不完整，降低项目的可追溯性和可重复检查能力。

**4. Adjustments — 做出的调整**

发现风险后，从 Windows 回收站恢复此前删除的 ZIP 文件。

随后建立独立的数据管理目录：

- `01_raw_original`
- `02_archive_manifest`
- `03_duplicate_review`
- `04_extracted_working`
- `05_processed`
- `06_backup`

将原始 ZIP 文件复制到 `01_raw_original`，保留原存储位置的文件，不直接修改或删除原始数据。

使用 Windows PowerShell 的 `Get-FileHash -Algorithm SHA256` 计算文件哈希值，并生成：

- `02_archive_manifest/sha256_manifest.csv`
- `03_duplicate_review/duplicate_review.csv`
- `03_duplicate_review/duplicate_group_summary.csv`

**5. Re-collection — 是否重新采集**

本阶段属于数据管理和文件恢复，不涉及重新采集运动数据。

**6. Verification — 改进效果是否经过数据验证**

已完成 102 个 ZIP 文件的 SHA-256 计算和第一阶段重复文件统计。

初步统计如下：

| 项目 | 数量 |
|---|---:|
| 原始 ZIP 文件总数 | 102 |
| 不同内容组数 | 39 |
| 存在重复的文件组数 | 16 |
| 重复组内文件总数 | 79 |
| 理论多余副本数 | 63 |

其中一个重复组包含 19 个文件：

- 代表文件名：`静止2.zip`
- 文件大小：250798 字节
- SHA-256：`3FBAB2CC336671DC0FF3C60C813F0E69584E676B989CBD2F649ECDABD60008CE`

该组 19 个文件的 SHA-256 完全一致，说明文件内容逐字节相同，不能视为 19 次独立实验采集。

结合已有实验记录，该组暂时对应桌面静止采集数据，具体实验属性仍以原始元数据核对为准。

**当前处理决定：**

1. 保留全部 102 个原始 ZIP 文件。
2. 不根据文件名直接删除疑似副本。
3. 暂定 `静止2.zip` 为该组代表文件。
4. 尚未执行物理删除。
5. 其余重复组仍需继续调查。
6. 备份验证尚未完成。

**Engineering reflection — 工程反思**

这次经历说明，原始数据管理不能只依靠文件名和人工判断。

后续采用“原始数据保护—哈希校验—重复审查—备份确认—处理记录”的流程，提高数据完整性和可追溯性。

## 3. Key Issues and Current Handling

| Issue | Potential impact | Current handling | Verification status |
|---|---|---|---|
| Handheld and pocket placement mixed | Measurement conditions differ | Separate placement labels; retain early data | Comparative verification pending |
| Desktop and pocket static measurements mixed | Different stationary conditions | Separate `desktop` and `pocket` | Metadata verification pending |
| Different sensor types | Different physical measurements | Verify total and linear acceleration separately | In progress |
| Different sampling rates | Different time resolution | Record actual sampling rates; plan standardization | In progress |
| Mixed stair directions | Ambiguous motion labels | Separate upstairs and downstairs categories | File-level verification pending |
| Downhill confused with downstairs | Incorrect motion classification | Use separate motion labels | File-level verification pending |
| Recording start disturbance | Possible transient signal | Inspect raw signals before excluding segments | Pending |
| Incomplete evidence association | Reduced traceability | Build an evidence index | In progress |
| Duplicate ZIP files | Risk of counting copies as independent experiments | SHA-256 review and preservation | First stage completed |

## 4. Data Retention Strategy

All original measurements should be retained.

Datasets are classified according to their actual acquisition conditions rather than being silently discarded when they do not meet the intended standardized protocol.

The project distinguishes between:

- **Exploratory data:** Measurements collected during preliminary experiments.
- **Candidate data:** Measurements that may be suitable for formal analysis but still require verification.
- **Selected data:** Measurements that have passed the defined quality checks.
- **Excluded data:** Measurements retained for traceability but not used in a particular formal analysis.
- **Pending verification:** Measurements whose metadata or experimental conditions are not yet confirmed.

Duplicate files with identical SHA-256 values should not be counted as independent experimental samples.

No original ZIP file should be physically deleted until the duplicate review, backup verification, and representative-file confirmation have been completed.

Final classification will be documented in:

`data/metadata/dataset_inventory.csv`

## 5. Current Project Status

截至本文档更新时：

**Completed**

- Preliminary handheld data collection.
- Desktop static measurements.
- Pocket static measurement.
- Subsequent pocket-placement collection for walking, running, upstairs, and downstairs.
- Initial distinction between handheld, desktop, and pocket conditions.
- Recovery of previously deleted ZIP files from Windows Recycle Bin.
- SHA-256 calculation for 102 ZIP files.
- First-stage duplicate file analysis.

**In progress**

- Complete inventory of original data files.
- Verification of sensor types and sampling rates.
- Verification of movement categories and phone placement.
- Identification of datasets suitable for formal comparison.
- Evidence association and experiment-batch documentation.
- Further duplicate-group review and backup verification.

**Not yet verified**

- Whether all candidate datasets satisfy the same acquisition protocol.
- Whether the new pocket-placement data show improved signal consistency.
- Whether the recording start procedure introduces measurable disturbances.
- Whether the selected datasets pass formal data-quality checks.

## 6. Next Steps

1. Complete the metadata inventory for all original ZIP files.
2. Verify each file's date, motion category, phone placement, sensor type, sampling rate, and duration.
3. Associate each dataset with its experiment batch and evidence.
4. Separate exploratory data from candidate data.
5. Complete duplicate-group review and backup verification.
6. Finalize the standardized acquisition protocol.
7. Inspect raw acceleration signals before selecting analysis segments.
8. Perform data-quality checks before feature extraction and comparison.
9. Update `data/metadata/dataset_inventory.csv` after metadata verification is complete.

## 7. Record Principles

Every iteration should record the following seven items:

1. Date and experiment batch.
2. Method used at that time.
3. Problem identified.
4. Reason the issue was considered a problem.
5. Adjustment made.
6. Whether data were collected again after the adjustment.
7. Whether the improvement was verified using data.

If a detail cannot be confirmed, mark it as **Pending verification** rather than inventing a value.

A planned adjustment must not be described as a completed adjustment. A completed re-collection must not automatically be described as a verified improvement.

---

**Record principle:** This document preserves the actual experimental learning process, including early mistakes, methodological changes, data-management problems, and unresolved issues. Experimental credibility depends on traceable evidence, not on presenting the process as error-free.

# Gait Analysis System

**多姿态步态加速度特征采集与对比**

A reproducible experimental project for gait acceleration data collection, signal processing, feature extraction, and motion pattern comparison.

---

## 1. Project Overview（项目概述）

### 1.1 项目背景

本项目以智能手机内置加速度传感器为数据采集工具，使用 Phyphox 记录人体在不同运动状态下的加速度信号。

通过对采集数据进行整理、质量检查、预处理、特征提取和可视化，探索不同运动状态下加速度信号的变化规律及其特征差异。

### 1.2 研究目标

- 采集不同运动状态下的加速度数据。
- 建立规范、可追溯的实验数据管理流程。
- 检查不同采集条件对数据质量的影响。
- 分析不同运动状态下的加速度信号特征。
- 提取具有分析价值的时域和频域特征。
- 探索不同运动状态的特征对比与区分方法。

### 1.3 研究问题

本项目重点关注以下问题：

1. 不同运动状态下的加速度信号具有哪些变化特征？
2. 手机放置位置和姿态是否会影响采集结果？
3. 包含重力加速度的数据与去除重力影响的数据有什么区别？
4. 哪些时域和频域特征有助于区分不同运动状态？
5. 如何通过规范的数据采集与处理提高实验结果的可靠性？

---

## 2. Experimental Categories（实验类别）

计划研究的运动状态包括：

| 类别 | 英文名称 | 实验说明 |
|---|---|---|
| 静止 | Static | 人体保持静止 |
| 正常行走 | Normal Walking | 平地正常速度行走 |
| 快跑 | Running | 按实验方案规定的速度跑步 |
| 上楼梯 | Stair Ascent | 沿楼梯向上行走 |
| 下楼梯 | Stair Descent | 沿楼梯向下行走 |

注：以上是计划研究的类别。实际数据是否齐全、是否符合正式实验条件，需要结合数据登记表核实。

---

## 3. Experimental Tools（实验工具）

### 3.1 数据采集与分析工具

- Android Smartphone：加速度数据采集设备。
- Phyphox：传感器数据采集软件。
- Python：数据处理、特征提取和可视化。
- GitHub：项目版本管理、实验文档和数据归档。

### 3.2 AI-assisted Tools（AI辅助工具）

本项目使用以下 AI 工具辅助实验与工程实践：

- ChatGPT
- DeepSeek
- Qwen
- WorkBuddy

AI 工具主要用于实验方案讨论、技术问题排查、资料整理、代码辅助和文档编写。

AI 生成的内容均需要人工核查。实验事实、数据结果和最终结论以实际实验及验证结果为准。

相关使用记录与对话档案见 `ai_collaboration/`。

---

## 4. Experimental Workflow（实验工作流程）

本项目采用以下工作流程：

1. Requirements Analysis：任务要求分析
2. Experimental Design：实验方案设计
3. Data Collection：实验数据采集
4. Data Quality Assessment：数据质量检查
5. Data Preprocessing：数据预处理
6. Feature Extraction：特征提取
7. Data Visualization：数据可视化
8. Comparative Analysis：特征对比分析
9. Result Evaluation：结果评估
10. Final Report：实验报告整理

---

## 5. Experimental Iteration（实验迭代）

本项目保留从初步实验到方案改进的完整过程。

实验过程中产生的初步数据、异常数据、失败尝试和后续补测数据均根据实际情况分类归档。


flowchart TD
    A["初步手持采集"] --> B["发现手机放置方式不一致"]
    B --> C["尝试裤袋采集"]
    C --> D["发现传感器类型不一致"]
    D --> E["进一步统一采集条件"]
    E --> F["正式数据采集与分析"]


重点记录：

- 不同实验轮次的采集方式。
- 手机放置位置和姿态的调整。
- 传感器类型和采集参数的变化。
- 实验过程中发现的问题。
- 实验方案的修改原因。
- 数据筛选和排除的依据。

早期数据不会因为不符合后续实验规范而被随意删除，而是保留其原始文件和实验背景。

详细记录见 `experiment/`。

---

## 6. Data Management（数据管理）

项目采用分层数据管理方式：

| 数据目录 | 内容 |
|---|---|
| `data/raw/` | 原始采集数据 |
| `data/interim/` | 中间处理数据 |
| `data/processed/` | 经过规范处理的数据 |
| `data/selected/` | 正式分析选用的数据 |
| `data/metadata/` | 数据登记表、采集条件及元数据 |

### 数据管理原则

1. 原始数据尽可能保持不变。
2. 保留原始文件名和数据来源。
3. 不同动作、手机放置方式和传感器类型分别标注。
4. 处理后的数据应能追溯到原始文件。
5. 正式分析数据应有明确的筛选依据。
6. 异常数据和未采用数据应记录原因。
7. 不将不同采集条件的数据未经评估直接混合分析。

---

## 7. AI Collaboration Records（AI协作记录）

为保证 AI 辅助过程透明、可追溯，本项目单独保存 AI 协作档案。

记录内容包括：

- AI 工具名称及可获取的模型版本。
- 对话日期和任务目的。
- 用户提示词及 AI 回复。
- AI 输出的使用情况。
- 人工核验与修改过程。
- 最终方案是否采纳及其原因。

完整档案见 `ai_collaboration/`。

AI 输出不直接作为实验结论或未经验证的技术依据。

---

## 8. Project Documentation（项目文档）

### 8.1 项目设计

- [项目概述](docs/project_overview.md)
- [任务要求](docs/requirements.md)
- [实验设计](docs/experimental_design.md)
- [数据采集规范](docs/data_collection_protocol.md)
- [数据字典](docs/data_dictionary.md)
- [数据质量标准](docs/data_quality_criteria.md)

### 8.2 实验过程

- [实验日志](experiment/experiment_log.md)
- [实验迭代历史](experiment/trial_history.md)
- [问题与解决记录](experiment/troubleshooting.md)
- [实验方案变更记录](experiment/protocol_changes.md)
- [关键决策记录](experiment/decision_log.md)

### 8.3 AI协作

- [AI协作档案](ai_collaboration/README.md)
- [AI工具登记表](ai_collaboration/ai_tools_registry.md)

### 8.4 数据与分析

- [数据登记表](data/metadata/dataset_inventory.csv)
- [最终实验报告](docs/final_report.md)

---

## 9. Reproducibility and Quality Control（可复现性与质量控制）

为了提高实验过程的可追溯性和分析结果的可靠性，本项目逐步建立以下规范：

- 记录实验设备和软件环境。
- 记录采集条件和实验操作。
- 保留原始数据及其元数据。
- 记录数据清洗和特征提取步骤。
- 对分析代码进行必要的测试。
- 保留实验方案变更和重要决策记录。
- 区分探索性分析与正式分析。

项目最终分析应尽可能能够从原始数据、处理代码和实验记录中复现。

---

## 10. Project Status（项目状态）

当前阶段：

**实验历史整理与数据规范化。**

后续计划：

- 完善历史实验记录。
- 整理所有原始数据。
- 核实各数据文件的采集条件。
- 统一正式实验采集规范。
- 开展数据预处理和特征分析。
- 形成实验结果和最终报告。

项目状态将根据实际进展持续更新。

---

## 11. Project Principles（项目原则）

本项目遵循以下原则：

- Scientific Integrity：尊重实验事实。
- Data Traceability：保证数据可追溯。
- Reproducibility：重视实验可复现性。
- Transparency：如实记录失败与改进。
- Human Verification：人工核验 AI 辅助内容。
- Version Control：通过 Git 提交记录管理项目变化。

---

**Project Name:** Gait Analysis System  
**Course Topic:** 课题08  
**Project Type:** Experimental Data Collection and Analysis  
**Status:** In Progress

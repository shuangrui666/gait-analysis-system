# Gait Analysis System｜课题08

**多姿态步态加速度特征采集与对比**

本仓库用于整理 Phyphox 手机加速度实验的原始数据登记、实验过程、证据索引、数据质量审查和后续分析代码。当前处于**历史数据整理与规范化阶段**；登记为候选的数据不等于已通过最终质量验收。

## 当前仓库结构（以 main 分支实际文件为准）

```text
.
├── data/
│   ├── metadata/
│   │   ├── data_dictionary.md
│   │   ├── dataset_inventory.csv
│   │   ├── dataset_review_flags.csv
│   │   ├── dataset_sha256_mapping.csv
│   │   └── evidence_index.csv
│   └── raw/
│       └── README.md
├── docs/
│   └── audit/
│       ├── README.md
│       ├── AUDIT_LOG.md
│       ├── DATA_INCLUSION_REVIEW.md
│       ├── DATA_LABEL_CORRECTIONS.md
│       ├── ANOMALY_REVIEW.md
│       ├── EVIDENCE_LINKAGE_REVIEW.md
│       ├── DECISION_HISTORY.md
│       ├── INVENTORY_CONSISTENCY_REPORT.md
│       └── analysis_inclusion_review_v1_1.csv
├── evidence/
│   ├── README.md
│   ├── evidence_index.csv
│   ├── video_evidence_manifest.csv
│   └── videos/
│       └── .gitkeep
└── experiment/
    ├── experiment_log.md
    ├── protocol_changes.md
    ├── trial_history.md
    └── troubleshooting.md
```

## 数据登记与追溯

| 文件 | 用途 |
|---|---|
| [数据集总清单](data/metadata/dataset_inventory.csv) | 原始文件名、仓库命名、动作、放置方式、传感器类型、采样率、时长和状态 |
| [数据审查标记](data/metadata/dataset_review_flags.csv) | 数据质量与复核提示；标记不自动等于排除 |
| [SHA-256映射](data/metadata/dataset_sha256_mapping.csv) | 原始数据文件哈希与重复文件溯源 |
| [数据字典](data/metadata/data_dictionary.md) | 字段定义与数据术语 |
| [元数据证据索引](data/metadata/evidence_index.csv) | 数据与证据关联线索 |
| [原始数据目录说明](data/raw/README.md) | 原始数据存放和管理约定 |

**重要：** inventory 中的 `candidate`、`exploratory` 或 `pending_verification` 是当前管理状态，不代表最终纳入结论。正式分析前必须结合原始 ZIP 内部记录、采集条件和质量检查再次确认。Total（含重力）与 Linear（去重力）数据应分别处理；不同手机放置方式也不应未经评估直接混合。

## 实验过程与证据

- [实验日志](experiment/experiment_log.md)
- [实验试验与迭代历史](experiment/trial_history.md)
- [方案变更记录](experiment/protocol_changes.md)
- [问题排查记录](experiment/troubleshooting.md)
- [证据目录说明](evidence/README.md)
- [视频证据清单（29条记录）](evidence/video_evidence_manifest.csv)
- [证据索引](evidence/evidence_index.csv)

视频清单是元数据索引，不代表视频二进制文件已经提交到 GitHub。当前 `evidence/videos/` 仅保留目录占位文件；如需提交视频，应另行核对文件大小、隐私和 Git LFS 方案。视频与数据无法可靠一一对应时，保持未确认状态，不按文件名或排序臆测配对。

## 数据审计

审计材料现已纳入 main：

- [审计档案入口](docs/audit/README.md)
- [审计日志](docs/audit/AUDIT_LOG.md)
- [数据纳入审查](docs/audit/DATA_INCLUSION_REVIEW.md)
- [标签修正记录](docs/audit/DATA_LABEL_CORRECTIONS.md)
- [异常复核](docs/audit/ANOMALY_REVIEW.md)
- [视频与数据关联审查](docs/audit/EVIDENCE_LINKAGE_REVIEW.md)
- [决策历史](docs/audit/DECISION_HISTORY.md)
- [清单一致性报告](docs/audit/INVENTORY_CONSISTENCY_REPORT.md)
- [纳入审查矩阵 v1.1](docs/audit/analysis_inclusion_review_v1_1.csv)

审查矩阵中的最终纳入状态仍为未定（`not_final`）；不得把候选数据描述为已通过最终验收。

## AI辅助工具与学术诚信

项目过程中使用过 ChatGPT、DeepSeek、Qwen、WorkBuddy 辅助讨论、排查、整理和文档编写。AI 输出应由人工结合原始数据核验；未保存的对话原文不应补写成虚构的逐字记录。实验事实与结论以原始数据和可复核过程为准。

## 当前状态与下一步

1. 继续核对39组数据的原始 ZIP 与哈希映射。
2. 复核动作、手机放置方式、Total/Linear、采样率和时长。
3. 根据统一标准完成数据质量检查，明确最终纳入/排除理由。
4. 在条件统一后补充正式采集数据。
5. 再开展预处理、时域/频域特征提取和动作对比。

## 项目原则

- 保留原始数据和历史试验记录。
- 不将探索性数据伪装成正式数据。
- 不根据猜测填补实验事实。
- 任何修订都应保留版本历史和可追溯依据。
- 区分 AI 建议、人工判断和数据证据。

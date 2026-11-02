# 课题八审查档案

本目录记录《多姿态步姿态加速度特征采集与对比》的资料整理、传感器数据核验、视频证据盘点、异常提示审查与分析纳入审查。它是审计轨迹，不替代原始数据、实验报告或最终分析。

## 文件
- AUDIT_LOG.md：审核阶段时间线
- DATA_INCLUSION_REVIEW.md：39组分析角色审查
- DATA_LABEL_CORRECTIONS.md：标签冲突与修正依据
- ANOMALY_REVIEW.md：质量检查与异常提示
- EVIDENCE_LINKAGE_REVIEW.md：29段视频及关联限制
- DECISION_HISTORY.md：关键决策和状态
- analysis_inclusion_review_v1_1.csv：逐组审查矩阵（非最终纳入名单）
- INVENTORY_CONSISTENCY_REPORT.md：与本地清单及GitHub main的核对结果

## 证据等级
1. 原始文件证据：ZIP内部CSV、device/time元数据、视频和哈希。
2. 用户确认：用户明确说明的动作、位置和采集过程。
3. 审核建议：规则或统计检查给出的建议，需人工终审。
4. 未知：证据不足时保持空白/待核，不补造。

## 原则
原始文件不覆盖、不因标签删除；Total与Linear分开；手持、裤袋、桌面分层；候选不等于正式纳入；视频候选关联不等于确认关联；不编造逐字AI聊天记录。

本档案根据现存本地文件与可检索对话上下文重建。早期对话并非全部以逐字日志保存，因此不声称是完整聊天逐字稿。
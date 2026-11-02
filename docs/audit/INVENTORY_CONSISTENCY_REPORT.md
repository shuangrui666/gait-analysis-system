# 清单一致性核对报告

核对日期：2026-11-02
核对对象：本地 project_stage 与 GitHub main 分支现存文件；审查矩阵为本分支 docs/audit/analysis_inclusion_review_v1_1.csv。

## 本地核对结果
- 审查矩阵39行、39个唯一dataset_id。
- 与本地 data/metadata/dataset_inventory.csv 的39个dataset_id完全一致：无缺失、无额外ID、无重复ID。
- 共同字段 motion_type、phone_placement、sensor_type、sampling_rate_hz、data_status 逐行一致。
- 本地inventory的analysis_usage均为not_confirmed，因此39组均保留final_inclusion_status=not_final；本矩阵没有擅自改写正式纳入状态。
- 传感器汇总：Total 34组，Linear 5组。

## 审查矩阵修订
- 将GAIT-4C170BA77C6C从primary_candidate_not_final修正为transition_contaminated_review：用户已确认录制开始后才放入裤袋，故不能作为全程稳定裤袋主分析样本。
- 将角色建议与过程风险、动作标签复核状态、视频关联状态拆成独立字段，避免一个单标签掩盖多种风险。
- 更新后角色建议计数：主分析候选未终审8；过渡风险复核10；手持探索7；Linear辅助4；桌面静止Total基线3；裤袋静止候选复核2；待人工复核2；下坡探索1；裤袋静止单独复核1；桌面静止Linear辅助1。合计39。

## GitHub main 分支核对
- main分支README.md可读取。
- main分支data/metadata/dataset_inventory.csv存在，但文件仅186字节，只有CSV表头，没有39组数据行。
- 以下路径在main分支未找到：data/metadata/dataset_review_flags.csv、data/metadata/dataset_sha256_mapping.csv、evidence/video_evidence_manifest.csv。
- 因此本次审查矩阵不能声称已与GitHub main的完整39组清单核对；一致性核对依据是本地39组inventory。远端main的清单和证据索引仍待同步/修复。

## 限制
- 逐组建议角色不是正式纳入/排除决定。
- 视频关联只标记候选池或未确认，不代表同步确认。
- 没有可恢复的逐字对话时，不声称此档案是完整聊天逐字稿。
- 此分支只增加审计文档；未改动main，也未上传原始ZIP或29段视频。

## 复核结论
本分支的39组审查矩阵与本地inventory通过ID和关键分类字段一致性检查。GitHub main仍缺少完整清单和相关索引，不能视为完整数据归档。
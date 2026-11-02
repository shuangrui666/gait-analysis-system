# 39组数据分析纳入审查

## 总体
39组唯一数据集，原始CSV约386,438行；Total 34组约500Hz，Linear 5组约100Hz。条件含裤袋、手持、桌面；动作含静止、走路、跑步、上楼、下楼、混合楼梯、下坡。基础结构检查未发现时间戳缺失/非递增、加速度缺失行或完全重复行；这不代表动作纯度、放置稳定性和实验设计全部合格。

逐组审查矩阵：[`analysis_inclusion_review_v1_1.csv`](analysis_inclusion_review_v1_1.csv)。矩阵将建议角色、过程风险、动作标签复核、视频关联和最终纳入状态分开记录。

## 建议角色分布（v1.1修订）
| 角色 | 数量 | 当前处理 |
|---|---:|---|
| primary_candidate_not_final | 8 | 符合初步主分析框架，仍需逐组终审 |
| transition_contaminated_review | 10 | 开始后放入/结束前取出等风险，检查波形边界 |
| exploratory_handheld_separate | 7 | 手持独立探索，不直接混入裤袋组 |
| auxiliary_linear_separate | 4 | Linear单独分析，不与Total合并 |
| baseline_candidate_separate | 3 | 桌面静止Total基线候选 |
| static_pocket_candidate_review | 2 | 用户确认裤袋静止，复核波动 |
| pending_manual_review | 2 | 原始登记/动作分类待核 |
| exploratory_downhill | 1 | 下坡独立探索，不并入楼梯 |
| separate_static_pocket_review | 1 | 用户确认裤袋静止，有离群提示需复核 |
| auxiliary_static_linear | 1 | 桌面静止Linear辅助参考 |

合计39。角色是建议，不是最终纳入名单。原始analysis_usage均为not_confirmed。

## 关键解释
- 主分析候选：动作明确、裤袋、Total、约500Hz等条件初步匹配；仍需确认动作执行、稳定放置和可比窗口。
- 过渡风险：不得把整段直接视为稳定裤袋样本；裁剪必须有波形边界、索引、脚本和理由，原始文件保留。
- 手持：独立放置条件。用户确认部分walking为正常速度，但无速度测量值。
- Linear/Total：物理含义不同，分开分析。
- 桌面静止与裤袋静止：不同条件，不能互换。
- mixed_stairs不可拆为纯上/下楼；下坡当前仅1组，独立探索。

## 特别数据集
- GAIT-2DB4E6C4072D：用户确认采集前已放稳左裤袋，期间站立不动；稳健离群仅是数值复核提示，保留数据。
- GAIT-7909BB9AD07A：原登记Linear/100Hz，ZIP内部Raw Data/device/time支持Total/约500Hz，已按文件证据修正。
- GAIT-8D5B23384548：用户此前口头称含g，但ZIP内部device/time支持Linear/约100Hz，按文件证据修正并保留冲突。
- GAIT-CF9602FC1477：用户确认下楼、左裤袋；ZIP内部为Total/约500Hz，采集时间约2026-10-29 09:56:56–09:57:16（UTC+08:00）。
- GAIT-C350D50D5DDB：左裤袋上楼，动作分类待核。
- GAIT-4C170BA77C6C：walking已确认，但开始后才放入裤袋，v1.1已归入过渡风险复核，不列入主分析候选。
- GAIT-06C3EF47B18A：walking已确认，速度未确认，采集中手机姿势变化，手持探索。
- GAIT-0904195532AE、GAIT-8E1FDD066074：用户确认左裤袋静止，需复核波动。

## 正式纳入前检查
冻结规则版本；逐组核验动作、位置、传感器、采样率、采集过程和质量状态；过渡数据确定可复现裁剪边界；记录最终决定和证据；检查时长与特征可比性；由项目负责人确认最终名单。
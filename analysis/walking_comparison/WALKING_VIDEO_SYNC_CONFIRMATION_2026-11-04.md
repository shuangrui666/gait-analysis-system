# 走路视频—Phyphox同步关系补充核验（用户确认版）

- 更新日期：2026-11-04
- 适用视频：EV-001、EV-011、EV-012、EV-014、EV-015、EV-024、EV-029
- 用户确认原话：**“视频和传感器数据是同一次实验同步拍摄的。”**
- 记录原则：用户确认作为实验过程来源记录；不把用户确认扩展成尚未提供的逐文件映射或精确时间偏移。

## 1. 本次确认解决了什么

此前将7段走路视频视为“动作/放置方式候选证据”，且同步关系未确认。现在用户明确确认视频与Phyphox传感器数据是在同一次实验中同步拍摄。因此，这7段视频不再视为独立补拍或无关演示素材；其与本轮走路采集存在**用户确认的同步实验关系**。

本次状态更新：
- session_sync_status = user_confirmed_synchronous
- evidence_role = synchronized_process_evidence
- dataset_linkage_status = candidate_pool_unresolved

## 2. 为什么还不能把每段视频直接绑定到某个Dataset ID

“同一次实验同步拍摄”确认了视频与传感器采集属于同步实验过程，但当前证据尚未给出：
- 每个EV文件对应哪个Phyphox导出文件；
- 若一段视频跨越多个Phyphox分段，具体覆盖哪些Dataset ID；
- 视频开始时刻与各CSV的Phyphox elapsed-time零点之间的偏移量；
- 视频帧中是否出现可识别的Phyphox开始/停止动作、设备时间或其他同步标记。

因此不能仅按文件名、视频时长、数据时长或“3段手持视频对3组手持数据”的数量相等来配对。

## 3. 按已核实的实验条件建立候选池

| 视频 | 已有画面标签 | 可进入的候选数据池 | 精确Dataset映射 |
|---|---|---|---|
| EV-001 | walking / left_trouser_pocket | GAIT-2FA81A7DC0BB、GAIT-387D48DED7C0、GAIT-4A7E3EAEC369、GAIT-4C170BA77C6C、GAIT-4F5177C0E51D、GAIT-5C02C71A19EB、GAIT-A8B03FC23EA3、GAIT-E084D341D878 | 未确定 |
| EV-011 | walking / left_trouser_pocket | 同上 | 未确定 |
| EV-014 | walking / left_trouser_pocket | 同上 | 未确定 |
| EV-015 | walking / left_trouser_pocket | 同上 | 未确定 |
| EV-012 | walking / handheld | GAIT-1A988B796ED4、GAIT-642C922009F2、GAIT-06C3EF47B18A | 未确定 |
| EV-024 | walking / handheld | 同上 | 未确定 |
| EV-029 | walking / handheld | 同上 | 未确定 |

候选池只按已有动作与手机放置标签建立。GAIT-387D48DED7C0虽属裤袋候选，但其Linear 100Hz配置必须单独分析；GAIT-06C3EF47B18A属于手持姿势变化数据，不应与固定手持条件直接合并。

## 4. 视频与信号区间的联合判定规则

后续确定每个Dataset的最终有效区间时，必须同时满足：
1. 视频画面可辨认实际行走，而不是仅出现准备、站立或拿手机；
2. 能够通过视频中的开始/停止操作、可见时钟、动作标记或用户确认的采集顺序，建立视频时间与CSV时间的对应关系；
3. 视频确认的行走片段与CSV中持续动态/周期性信号相符；
4. 手机放入/取出、起步、停止、转身、楼梯/转场等边界单独标记；
5. 视频与CSV不一致时保留冲突，不以任一方强行覆盖。

如果无法获得时间偏移量，视频只能确认组级动作/放置方式及“该次实验确有行走”，不能把画面中的第N秒直接写成CSV的第N秒。

## 5. 11组数据当前最终区间状态

本轮不将候选区间直接升级为confirmed。现有CSV信号候选仍按WALKING_RAW_DATA_VERIFICATION_ROUND2.md记录。由于视频—CSV时间零点偏移和逐视频—数据文件映射尚未证实，11组仍保持pending_verification。

特别说明：
- GAIT-642C922009F2：23.2515s峰值保留为局部事件；不因单个峰值排除整组。
- GAIT-A8B03FC23EA3：两段候选之间的低动态区不拼接。
- GAIT-4A7E3EAEC369：两段候选之间的低动态区不拼接。
- GAIT-387D48DED7C0：Linear 100Hz单独处理。
- GAIT-06C3EF47B18A：姿势变化后的区间仅作探索性分析。

## 6. 关闭最后映射缺口所需的最小信息

只需确认视频是否能看到Phyphox开始/停止记录的操作，或是否存在可读的时间/同步标记。若画面没有这些信息，则需要用户提供各视频与数据文件的采集先后顺序/分段关系；不需要重新上传已经存在的原始CSV。

本文件记录了用户确认的同步实验关系，但不伪造视频—Dataset一对一映射、视频帧时间偏移或最终稳定步行区间。

# Walking Experiment — Trial History and Protocol Iterations

## Purpose

This is a reconstructed, evidence-bounded history from the current inventory, audit CSVs, and user-confirmed details. It is not a verbatim laboratory notebook or a complete timestamped chronology.

## Iteration history

| Stage | Observed situation | Risk / limitation | Handling decision |
|---|---|---|---|
| Initial exploration | Walking records were collected with the phone handheld. | Hand posture and orientation may vary; placement differs from pocket trials. | Retain as exploratory handheld stratum; do not pool with pocket records. |
| Placement adjustment | Collection expanded to phone in the left trouser pocket. | Recording may begin before phone is fully placed, or end after it is removed. | Mark transition risk; identify stable portions from signal and evidence. |
| Sensor-channel discovery | Both Total (gravity included) and Linear (gravity removed) exports appear in inventory. | Sensor definitions and nominal sampling rates differ. | Separate Total ~500 Hz and Linear ~100 Hz; do not pool raw signals. |
| Evidence audit | Several videos can be associated with groups by activity and placement. | No unique ID or synchronized timestamps establish individual ZIP-to-video links. | Keep group-level candidate association only. |
| Current review | Two left-pocket Total 500 Hz raw ZIPs were reopened and recalculated. | Nine other inventory entries were not reopened at raw CSV level in this pass. | Mark all records pending verification until consistent raw-data and quality checks are complete. |

## Known collection conditions

- `GAIT-1A988B796ED4` and `GAIT-642C922009F2`: user-confirmed normal-speed walking while handheld; filenames say “慢走”, but the user's clarification takes precedence. Numeric speed was not measured.
- `GAIT-06C3EF47B18A`: walking with changes in phone holding posture; keep separate.
- `GAIT-4C170BA77C6C`: user-confirmed walking; phone was placed in the pocket after recording began, so the start may contain a placement transition.
- Several pocket records have inventory notes indicating placement after recording began and removal before it ended. Verify each record before defining stable segments.
- `GAIT-387D48DED7C0`: left-pocket Linear acceleration, nominal 100 Hz; auxiliary independent stratum.

## Protocol decisions for subsequent trials

1. Use one defined placement (left trouser pocket) and document phone orientation and pocket side.
2. Select one sensor channel per comparison stratum; do not mix Total and Linear.
3. Use consistent recording duration and sampling configuration where the app/device allows; record actual timestamps and observed rate.
4. Start recording only after the phone is secured in the pocket, or mark a visible/synchronized start event; avoid handling during the measured interval.
5. Record normal walking speed as a qualitative instruction unless speed is measured; do not infer exact speed from a filename.
6. Preserve original ZIPs and record SHA-256; store derived data separately.
7. Record failures, interruptions, placement changes, and retests rather than silently discarding them.

## Open questions

- Recover and verify the nine remaining raw ZIPs/CSVs in the walking inventory.
- Determine whether candidate intervals contain stops, turns, or placement changes.
- Establish a repeatable stable-segment rule before final feature comparisons.
- Improve video-to-sensor synchronization if exact action boundaries are required.
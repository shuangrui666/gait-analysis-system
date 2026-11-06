# Walking Group — Stage-wise Data Inclusion Review

**Review version:** 1.0 (stage review; not final inclusion).

## Decision vocabulary

- `selected`: evidence and quality criteria are satisfied for the stated analysis stratum.
- `excluded`: a documented reason makes the dataset unsuitable for that stated analysis. Keep the original and record the reason.
- `pending_verification`: evidence is incomplete or a material condition/quality issue remains unresolved.

## Analysis-role classification

See [`walking_final_role_classification.csv`](walking_final_role_classification.csv) for the 11-row role table. The role labels (primary candidate, auxiliary comparison, auxiliary sensor stratum, exploratory reference) describe intended analysis use only; they do not change the formal inclusion status.

## Current decision table

All 11 walking records remain `pending_verification`. The available evidence does not support a final selected/excluded decision for every record.

| Dataset ID | Placement | Sensor / nominal rate | Stage status | Reason / review note |
|---|---|---|---|---|
| `GAIT-1A988B796ED4` | handheld | total 500 Hz | `pending_verification` | Speed not numerically measured; handheld differs from pocket stratum. User confirmed normal-speed walking despite filename “慢走”. |
| `GAIT-642C922009F2` | handheld | total 500 Hz | `pending_verification` | Handheld; prior extreme-value screen flagged 3.32% for curve review. User confirmed normal-speed walking. |
| `GAIT-2FA81A7DC0BB` | pocket | total 500 Hz | `pending_verification` | Placement/removal transition risk in inventory. |
| `GAIT-387D48DED7C0` | pocket | linear 100 Hz | `pending_verification` | Linear must be analyzed separately from 500 Hz Total. |
| `GAIT-4C170BA77C6C` | pocket | total 500 Hz | `pending_verification` | Phone placed in pocket after recording began. |
| `GAIT-4F5177C0E51D` | pocket | total 500 Hz | `pending_verification` | Raw CSV reopened; stable interval/video timing not confirmed; transition risk. |
| `GAIT-4A7E3EAEC369` | pocket | total 500 Hz | `pending_verification` | Placement/removal transition risk in inventory. |
| `GAIT-E084D341D878` | pocket | total 500 Hz | `pending_verification` | Placement/removal transition risk in inventory. |
| `GAIT-A8B03FC23EA3` | pocket | total 500 Hz | `pending_verification` | Raw CSV reopened; stable interval/video timing not confirmed. |
| `GAIT-5C02C71A19EB` | pocket | total 500 Hz | `pending_verification` | Placement/removal transition risk in inventory. |
| `GAIT-06C3EF47B18A` | handheld | total 500 Hz | `pending_verification` | Phone posture changed during collection; speed not quantified. |

## Strata and handling rules

1. **Primary candidate stratum:** left-trouser-pocket, Total acceleration, nominal 500 Hz. Keep records separate until raw archive identity, placement, transition handling, and quality are verified.
2. **Linear acceleration:** `GAIT-387D48DED7C0` is 100 Hz and must be analyzed separately. Do not pool its raw samples or features with Total records as if they were the same signal.
3. **Handheld:** `GAIT-1A988B796ED4`, `GAIT-642C922009F2`, and `GAIT-06C3EF47B18A` are exploratory placement records, not pooled into the pocket main group. The first two were user-confirmed as normal-speed walking despite “慢走” in filenames; numeric speed was not measured.
4. **Placement transitions:** where the phone was put into the pocket after recording began or removed before recording ended, mark transition risk. Do not define a stable segment by an arbitrary fixed crop without trace/evidence review.
5. **Outliers:** do not exclude a record based only on a large peak. Inspect the raw trace and document the reason.

## Minimum criteria before changing a status to selected

- Original ZIP identified; SHA-256 recorded; metadata and raw CSV parsed.
- Action, placement, sensor channel, and sampling rate supported by user confirmation or source evidence.
- Stable interval defined by a documented rule and checked against the waveform.
- Missingness, timestamp gaps, clipping/saturation, extreme values, and transition effects assessed.
- Video relation accurately classified as confirmed, candidate, or unlinked.
- Feature calculations reproducible with code and parameters.

## Why no records are excluded yet

Current evidence identifies risks and stratification needs, but a complete, consistently applied exclusion protocol has not been demonstrated for all records. A record may be exploratory or unsuitable for the primary comparison without being deleted or globally excluded from every possible analysis. Revisit this table after remaining raw archives are verified.
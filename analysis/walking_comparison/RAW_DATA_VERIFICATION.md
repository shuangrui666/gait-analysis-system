# Walking Group — Raw Data Verification

**Status:** partial raw-archive verification. This does not mean all 11 walking datasets were opened at CSV level.

## Scope and method

The available local source set was inspected. Each available ZIP was opened and its `Raw Data.csv`, `meta/device.csv`, and `meta/time.csv` were read. SHA-256 was calculated over the complete ZIP bytes. Inventory metadata was cross-checked against `experimental_condition_review_v2.csv`. Original archives were not modified.

## Raw ZIPs actually verified

| Dataset ID | Local archive | Rows | CSV time span (s) | Median-rate estimate (Hz) | ZIP SHA-256 |
|---|---|---:|---:|---:|---|
| `GAIT-A8B03FC23EA3` | `走路有g口袋(1).zip` | 11,736 | 23.470 | 500.00 | `a8b03fc23ea3120e4bcbf525322458747efba56bdafd88d2dd36921288ff3c32` |
| `GAIT-4F5177C0E51D` | `走路口袋(2).zip` | 17,283 | 34.564 | 500.00 | `4f5177c0e51deeab0f66b008e55a90da3bb7869aa8c33c40981b9503652bb623` |

Both archives contain exactly `Raw Data.csv`, `meta/device.csv`, and `meta/time.csv`. Both report device model `TLR-AL00` / brand `HUAWEI`, Phyphox `1.1.10`. The exported acceleration columns are `Acceleration x/y/z` and `Absolute acceleration`.

| Dataset ID | First sample (s) | Last sample (s) | Median Δt (s) | Min Δt (s) | Max Δt (s) | Magnitude mean | SD | Min | Max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `GAIT-A8B03FC23EA3` | 0.006079 | 23.476079 | 0.002000 | 0.001897 | 0.002103 | 10.3269 | 2.8226 | 2.3639 | 25.2331 |
| `GAIT-4F5177C0E51D` | 0.009184 | 34.573184 | 0.002000 | 0.001836 | 0.002164 | 10.9591 | 3.9796 | 1.6959 | 30.9411 |

Magnitude values are in m/s². Median sample interval is 0.002 s (approximately 500 Hz). CSV span is last timestamp minus first timestamp and may differ slightly from START/PAUSE elapsed time.

## Duplicate archive handling

`走路有g口袋(1).zip` and `走路有g口袋(1)_2.zip` have identical SHA-256 `a8b03fc23ea3120e4bcbf525322458747efba56bdafd88d2dd36921288ff3c32`. `走路口袋(2).zip` and `走路口袋(2)_2.zip` have identical SHA-256 `4f5177c0e51deeab0f66b008e55a90da3bb7869aa8c33c40981b9503652bb623`. Each pair is one unique archive, not two independent trials.

## Remaining raw-file gap

The condition inventory lists 11 walking Dataset IDs. Only `GAIT-A8B03FC23EA3` and `GAIT-4F5177C0E51D` could be mapped to and opened as original raw ZIPs in this pass. For the other nine IDs, inventory and waveform/audit references exist, but their source ZIP/CSV contents were not independently reopened here. Their row counts, SHA-256, device metadata, timestamps, and sampling intervals remain **unverified at raw-archive level**.

## Integrity and interpretation limits

- SHA-256 verifies byte identity, not correctness of an experimental label.
- The approximately 500 Hz rate is derived from timestamps.
- No filtering, resampling, or gravity removal was applied.
- Full-record statistics may include phone placement/removal transitions; they are not statistics of a verified steady walking interval.
- No raw archive was overwritten, renamed, or deleted.
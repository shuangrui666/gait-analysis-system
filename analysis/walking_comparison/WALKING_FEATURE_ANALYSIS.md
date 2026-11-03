# Walking Group — Signal and Feature Analysis

## Scope

This report contains reproducible full-record calculations for the two raw CSVs available in this pass. It does not claim full feature analysis of all 11 inventory entries. Both verified records are left-pocket, Total acceleration, approximately 500 Hz. Linear acceleration (100 Hz) and handheld records are excluded from this direct comparison.

## Calculation procedure

1. Read `Time (s)` and the three axis columns from `Raw Data.csv`.
2. Calculate magnitude as `sqrt(x² + y² + z²)` in m/s².
3. Calculate full-record mean, sample standard deviation (`ddof=1`), minimum, maximum, P95, and P99.
4. Calculate local variability in 1.0-second windows advanced by 0.5 seconds; use sample standard deviation within each window.
5. Do not automatically remove transitions or interpret low variability as a confirmed stop.

No smoothing, band-pass filtering, gravity subtraction, peak-based step counting, or frequency-domain gait estimation is included.

## Full-record features

| Feature | `GAIT-A8B03FC23EA3` | `GAIT-4F5177C0E51D` |
|---|---:|---:|
| Samples | 11,736 | 17,283 |
| Timestamp span (s) | 23.470 | 34.564 |
| Median sampling rate (Hz) | 500.00 | 500.00 |
| Magnitude mean (m/s²) | 10.3269 | 10.9591 |
| Magnitude sample SD (m/s²) | 2.8226 | 3.9796 |
| Magnitude minimum (m/s²) | 2.3639 | 1.6959 |
| Magnitude maximum (m/s²) | 25.2331 | 30.9411 |
| Magnitude P95 (m/s²) | 15.7176 | 19.5613 |
| Magnitude P99 (m/s²) | 19.3478 | 23.9720 |
| 1-s window SD median (m/s²) | 2.8431 | 4.0415 |
| 1-s window SD P95 (m/s²) | 3.8214 | 4.9699 |

## Signal-level candidate intervals

### `GAIT-A8B03FC23EA3`

The prior waveform review described candidate dynamic intervals around 3.5–9.5 s and 11.5–20 s, with relative reduction around 9.5–11.5 s and after about 20 s. These are visual/signal-level candidates, not ground-truth walking labels. The raw-file summary does not establish the cause of the lower-variability region. Retain these intervals for manual review; do not silently concatenate them into a confirmed walking segment.

### `GAIT-4F5177C0E51D`

The prior waveform review described a sustained dynamic interval around 3.5–31 s and a reduction after about 31 s. This is a signal-level candidate only. Inventory notes indicate phone placement/removal transitions may be present, so the beginning and end are not clean gait boundaries without synchronized evidence.

## Comparison limits

The larger full-record standard deviation and maximum in `GAIT-4F5177C0E51D` do not establish faster walking, better data quality, or more steps. Duration, transitions, orientation, and individual variation may affect these values. The two records are not a controlled repeated-measures comparison with verified identical segmentation.

## Next stage

Recover and verify the remaining raw archives; define a transparent stable-segment rule; document filtering parameters; then compute axis-level and magnitude-level time/frequency features with identical settings within the Total 500 Hz stratum. Analyze Linear 100 Hz separately. Any cadence estimate must document its algorithm, parameters, and manual validation.
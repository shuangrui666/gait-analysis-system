# AI Collaboration Log — Walking Group Review

## Record scope

This entry documents the current AI-assisted review of the walking dataset. It is a concise reconstruction of work performed in this session, not a verbatim transcript. No unobserved prompts or responses from other AI tools are fabricated.

## Tools and roles

| Tool | Role recorded in this entry | Evidence status |
|---|---|---|
| ChatGPT | Structured the audit, inspected available source files, calculated raw-CSV statistics, distinguished sensor/placement strata, and drafted review documents. | Current session; calculations reproducible from the two source ZIPs. |
| DeepSeek | No specific walking-group output was independently available for this entry. | Not documented here. |
| Qwen | No specific walking-group output was independently available for this entry. | Not documented here. |
| WorkBuddy | No specific walking-group output was independently available for this entry. | Not documented here. |

## Tasks performed

1. Reopened the two available walking raw ZIP archives and read `Raw Data.csv`, `meta/device.csv`, and `meta/time.csv`.
2. Computed SHA-256 for each archive and identified byte-identical duplicate copies.
3. Recalculated sample count, timestamp span, median sampling interval, acceleration magnitude summary statistics, and rolling-window variability.
4. Compared results with the walking rows in `experimental_condition_review_v2.csv`.
5. Reviewed the existing group-level video linkage register and preserved its unconfirmed linkage status.
6. Drafted stage-wise inclusion statuses and documented unresolved evidence gaps.

## Human verification and adoption rules

- Dataset labels and placement details come from the existing audit inventory and user-confirmed clarifications; they are not inferred from filenames alone.
- The user confirmed that `GAIT-1A988B796ED4` and `GAIT-642C922009F2` are normal-speed handheld walking despite “慢走” in filenames.
- The user accepted group-level candidate video associations; this does not upgrade them to exact one-to-one links.
- Calculated statistics are numerical outputs from raw CSVs; candidate gait intervals remain provisional and require human/evidence review.
- AI recommendations are not treated as experimental facts or final inclusion decisions.

## Known limitations

- Only two walking raw ZIPs were available for direct CSV-level recalculation in this pass.
- Original walking video files were not available for frame-by-frame verification in this pass.
- No final `selected` or `excluded` decision is justified for all walking records yet.
- This log does not reproduce full chat transcripts. If full prompt/response evidence is required, export and archive the actual conversation records separately.

## Reproducibility note

The calculations use the three acceleration axes in each ZIP's `Raw Data.csv`. Magnitude is `sqrt(x²+y²+z²)`. Rolling variability uses 1-second windows with 0.5-second steps and sample standard deviation (`ddof=1`). No filtering, resampling, or gravity removal is applied in this entry.
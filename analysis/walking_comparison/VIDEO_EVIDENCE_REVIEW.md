# Walking Group — Video Evidence Review

## Source and scope

This review uses the existing `video_linkage_status_v2.csv` and `evidence_dataset_relationships_v2.csv` audit materials, plus the user's confirmation that the group-level candidate relationships are acceptable. Original walking videos were not available for frame-by-frame reinspection in this pass.

## Walking video candidate groups

| Evidence ID | Video file | Placement label | Candidate dataset count | Existing linkage status |
|---|---|---|---:|---|
| `EV-001` | `1036232062.mp4` | left_trouser_pocket | 8 | unlinked_insufficient_unique_evidence |
| `EV-011` | `2130554508.mp4` | left_trouser_pocket | 8 | unlinked_insufficient_unique_evidence |
| `EV-012` | `245385489.mp4` | handheld | 3 | unlinked_insufficient_unique_evidence |
| `EV-014` | `411962750.mp4` | left_trouser_pocket | 8 | unlinked_insufficient_unique_evidence |
| `EV-015` | `412917757.mp4` | left_trouser_pocket | 8 | unlinked_insufficient_unique_evidence |
| `EV-024` | `1391686904.mp4` | handheld | 3 | unlinked_insufficient_unique_evidence |
| `EV-029` | `2123841312.mp4` | handheld | 3 | unlinked_insufficient_unique_evidence |

The left-pocket candidate datasets are `GAIT-2FA81A7DC0BB`, `GAIT-387D48DED7C0`, `GAIT-4C170BA77C6C`, `GAIT-4F5177C0E51D`, `GAIT-4A7E3EAEC369`, `GAIT-E084D341D878`, `GAIT-A8B03FC23EA3`, and `GAIT-5C02C71A19EB`. The handheld candidates are `GAIT-1A988B796ED4`, `GAIT-642C922009F2`, and `GAIT-06C3EF47B18A`.

Candidate membership supports group-level association by activity and placement only. It does not identify which exact sensor ZIP corresponds to which exact video.

## What the evidence supports

- Candidate videos are categorized as walking and grouped by handheld versus left-trouser-pocket placement in the existing evidence register.
- The user accepted these group-level associations as the working correspondence.
- The evidence register explicitly labels the associations as unlinked / insufficient unique evidence.

## What it does not support

- One-to-one video-to-ZIP mapping.
- Exact walking start/end timestamps in each sensor recording.
- Confirmation that each individual sensor record is continuously walking throughout its full recording.
- Precise synchronization based only on filenames or visual similarity.

## Required evidence for stronger linkage

A confirmed mapping should use a unique trial ID visible in both records, synchronized clock/timestamp metadata, or a documented event marker that unambiguously aligns sensor trace and video. Until then, retain candidate-only / unlinked language.
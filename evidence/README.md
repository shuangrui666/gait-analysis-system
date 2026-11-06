# Evidence Archive

## Purpose

This directory stores and indexes evidence that supports the gait-analysis experiments. Evidence must be traceable to the corresponding experiment and dataset.

## Directory structure

```text
evidence/
├── README.md
├── evidence_index.csv
└── videos/
    └── .gitkeep
```

## Evidence rules

1. Keep original recordings unchanged. Do not silently edit, trim, or replace source videos.
2. Give each submitted video a stable evidence ID and record its related experiment and dataset in `evidence_index.csv`.
3. Only list a video as available when the actual file has been added and checked.
4. If a recording was not made, record the status as `not_recorded`; do not create a placeholder video or imply that evidence exists.
5. If a video exists locally but has not been uploaded, use `recorded_not_uploaded` and keep its repository path blank until upload.
6. Large video files may require Git LFS or an external storage location. If external storage is used, document the location and access limitations without exposing private credentials.
7. Do not publish personal or sensitive information visible in recordings.

## Index fields

- `evidence_id`: stable evidence identifier.
- `recording_date`: recording date, when verified.
- `experiment_id`: experiment identifier, when assigned.
- `motion_type`: action represented by the recording.
- `related_dataset_id`: matching dataset ID, when verified.
- `recording_status`: `available`, `recorded_not_uploaded`, `not_recorded`, or `pending_verification`.
- `repository_path`: repository-relative path to the actual video; blank when no repository file exists.
- `notes`: factual notes about the evidence or its limitations.

## Current archive status\n\nThe manifest records 29 video files, while the repository `videos/` directory currently contains only 3 MP4 files. A manifest row is not proof that a video is present in this repository. The source collection also contains recordings from other coursework; the collector has explicitly excluded 7 recordings from Topic 08. Do not upload unrelated coursework recordings merely to make the manifest count match. First identify the Topic 08 originals, preserve their original bytes, and record SHA-256 values. If the full set is too large for ordinary Git, use Git LFS or a documented external archive with checksums and access instructions.\n\n## Known evidence gaps

The downhill-walking recording and the cafeteria-stairs recording were not video-recorded. They must remain explicitly marked as `not_recorded` in the index. This is a documentation of the evidence gap, not a claim that video files exist.

# Changelog

## v2.1 — revision after the first review round (2026)

### Added
- `audit/notebooks/revision_r1_checks.ipynb`: one-run checks requested by the reviewers — verification that
  101 frozen values of the paper are reproduced; provenance of CVE/EPSS/KEV values (CVE pools and KEV restricted
  to the snapshot date; EPSS for CIC-IDS2017 taken retrospectively from the 2021-04-14 file); determinism and
  coverage of the port→service mapping; CTI-availability and no-EPSS control models; seven training seeds;
  UNSW-NB15 alternative chronological and cross-session splits; per-class AP.
- `audit/results/revision_r1/`: report and JSON of that run.

## v2.0 — revised manuscript (2026)

### Added
- `audit/`: evaluation-validity audit (Phase 0) — CIC-IDS2017 AM/PM timestamp correction,
  stratified temporal split, split-composition audit, equal-budget training, 1-minute block
  bootstrap with Holm correction.
- Control models for Phase III: raw destination port (numeric and categorical) and a placebo
  with CTI values permuted across services.
- Phase I conditional entropy against (protocol, destination port); Phase II gain-share on the
  equal-budget models.
- Within-service CTI experiment (Section 5.5).

### Changed
- Track B results in the paper now come from the equal-budget protocol. The v1.0 numbers came
  from early-stopped models on an as-parsed chronological split and are kept only as the
  audited baseline (Section 5.4).

### Unchanged
- CTI Context Enrichment Module, CVE/EPSS/KEV corpus, Track A, and the Zenodo data record.

## v1.0 — initial submission (September 2026)

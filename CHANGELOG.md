# Changelog

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

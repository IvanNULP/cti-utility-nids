# Evaluation-validity audit (Phase 0) and corrected Track B analyses

This folder accompanies the revised manuscript. It contains the code used to audit the
initial Track B pipeline (Section 5.4) and to produce every Track B result reported under
the valid, equal-budget protocol (Sections 5.2, 5.3 and 5.5).

## What changed relative to v1.0

| Issue found by the audit | Affects | Fix used in the revised paper |
|---|---|---|
| CIC-IDS2017 `Timestamp` uses a 12-hour clock without AM/PM | CIC-IDS2017 | `fix_ampm()`: +12 h when hour < 8 |
| Chronological 70/15/15 split leaves DDoS, PortScan and Bot out of training | CIC-IDS2017 | `stratified_temporal_split()`: same percentile rule within each (day × class) group |
| Early stopping compared F0 and F1 at different budgets (e.g. 4 vs 118 rounds) | both | every model trained for T = 500 rounds; 11–500 as sensitivity |
| Differences reported without uncertainty | both | 1-minute block bootstrap, B = 500, Holm correction |

The v1.0 pipeline is kept unchanged in the repository so that the initial figures
(ΔAP = +0.2637 on CIC-IDS2017, +0.0103 on UNSW-NB15) remain reproducible.

## Layout

```
audit/
  src/cic_timestamp_fix.py   AM/PM correction, stratified temporal split, split-composition table
  src/block_bootstrap.py     block-bootstrap ΔAP, one-sided p-value (Eq. 15), Holm adjustment
  notebooks/                 executed notebooks (see table below)
  results/                   JSON/CSV outputs of the notebooks
```

## Notebooks → paper

| Notebook | Paper |
|---|---|
| `check_cic_split.ipynb`, `check_unsw_split.ipynb` | Phase 0 split audit; Table 14 |
| `cic_control_experiments.ipynb` | Corrected timestamps, chronological split (Table 15; Figure 2a); first port/placebo controls |
| `cic_asparsed_same_budget.ipynb` | Exact reproduction of the initial pipeline, then the as-parsed split at equal budget (Table 15; Figure 2a) |
| `cic_stratified_temporal.ipynb` | Corrected CIC-IDS2017 split (Table 3); Table 10; Figure 2a |
| `unsw_fixed_rounds_check.ipynb` | UNSW-NB15 at equal budget; Table 10; Figure 2b |
| `unsw_port_cti_controls.ipynb` | Port and placebo controls on UNSW-NB15; Table 13 |
| `phase12_corrected.ipynb` | Phase I conditional entropies (Table 11); Phase II gain-share (Table 12) |
| `expB_cti_beyond_port.ipynb` | Within-service CTI design; Tables 16–17; Figure 3 |

## Fixed settings

LightGBM 4.7.0, `objective=binary`, `num_leaves=15`, `learning_rate=0.05`,
`min_data_in_leaf=50`, `seed=42`, `scale_pos_weight` from the training partition
(4.3357 for CIC-IDS2017, 28.2135 for UNSW-NB15), T = 500 rounds without early stopping.
Feature-column order must follow the frozen contract files.

## Data

CIC-IDS2017 and UNSW-NB15 are not redistributed (licence terms); obtain them from the
original providers and run the enrichment module first. Set the parquet paths at the top
of each notebook (`/srv/ids_research/data/...` on the authors' server). The notebooks are stored
with the outputs of the runs reported in the paper; comments and printed labels were translated
to English after the runs, without changing code or numbers. CSV outputs are written to the data
directory and are collected in `results/`.

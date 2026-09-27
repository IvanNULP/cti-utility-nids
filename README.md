# CTI-Utility Assessment Approach — code and data

Code and data for the paper "A CTI-Utility Assessment Approach for Integrating Vulnerability Intelligence into Flow-Based NIDS".

## Environment

Conda env `ids_research`. Python, LightGBM, PyTorch + transformers (for the SecBERT model used in Track A).

## Structure

- `step3_service_cve_mapping.ipynb` — CTI enrichment pipeline (port/protocol → service → CVE pool → EPSS/KEV).
- `step4a*`, `step4b1*` — Track A: CVE-level forecasting of future KEV inclusion.
- `step5c*`, `step5d*`, `step5e*` — Track B: flow-level detection on CIC-IDS2017 and UNSW-NB15, plus the overlap → attribution → ablation audit (Phases I–III).
- `results/` — saved model outputs and metrics used in the tables.
- `data/` — CVE/EPSS/KEV corpus and the derived CVE forecasting dataset.

Run notebooks in the order given by the step numbers. Each one is frozen — seed 42, no retuning after the reported results.

## Data

CIC-IDS2017 and UNSW-NB15 are not included here — download them from their original sources and see the paper (Section 3) for the exact preprocessing steps (deduplication for UNSW-NB15, re-extraction for CIC-IDS2017). GeNIS is included (CC-BY-4.0). The CVE/EPSS/KEV corpus is built from public sources (NVD, EPSS, CISA KEV, Exploit-DB) — see `step3_service_cve_mapping.ipynb` for how.

## License

Code license to be added before publication.

## Contact

Ivan Opirskyy, Lviv Polytechnic National University — ivan.r.opirskyi@lpnu.ua

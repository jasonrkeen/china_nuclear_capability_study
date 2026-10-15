# Copilot instructions: China Nuclear Capability Study

## Purpose
Python-based open-source analysis of China’s nuclear capability, stockpile growth, forecast scenarios, and defense-spending context using public estimates.

## Tech stack
- Python; dependencies in `requirements.txt`
- Key libraries: `pandas`, `matplotlib`, `tabulate`

## Folder structure
- `charts/` (8 files)
- `data/` (6 files)
- `presentation/` (1 files)
- `src/` (7 files)
- `README.md`
- `china_nuclear_capability_report_final.pdf`
- `final_report.md`
- `main.py`
- `requirements.txt`

## Setup, run, test
Commands documented in README.md (referenced files exist):
```bash
pip install -r requirements.txt
python main.py
```
- No automated tests exist yet; if adding them, use pytest under `tests/`.

## Conventions observed
- Functions use type hints; keep annotating new code.
- Public data sources referenced: SIPRI.
- Write paths relative to the repo root (no absolute local paths).

## Output artifacts
- A PDF report is produced; keep it in sync with model changes.
- Charts are generated with matplotlib.

## Guardrails
- Never commit secrets, API keys, tokens, or `.env` files.
- Do not commit large raw datasets or binaries; keep data fetched or documented with its source.
- Keep analysis source-backed: cite data sources and assumptions; label scenario/forecast outputs as model estimates, not facts.
- Preserve reproducibility: no unseeded randomness, no hidden manual steps.

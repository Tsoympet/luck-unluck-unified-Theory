# Unified Theory of Luck–Unluck

A complete, English-only, submission-ready package: **manuscript (Word+PDF), figures, templates, notebook, scripts, CI, OSF/Zenodo scaffolding**.

## Quick start
```bash
pip install -r requirements.txt
make smoke        # quick DM/HAC & Catoni check
make figs         # regenerate example figures (if data present)
# Optional:
make notebook     # executes the repro notebook via nbconvert
```

## Contents
- `manuscript/`: Word manuscript (+ Cover Letter & Highlights DOCX)
- `docs/`: PDF manuscript + submission checklist + OSF template
- `figures/`: Graphical Abstract, calibration ternary, power curve, equities/roulette/slots/lottery figures
- `templates/`: DM & Catoni CSV templates
- `notebooks/`: 1-click reproducibility notebook
- `scripts/`: DM/HAC & Catoni utilities; figure generator
- `data/`: place your CSVs here (see `data/README.md`)
- `CITATION.cff`, `CITATION.bib`, `LICENSE` (MIT), `CONTRIBUTING.md`
- `.github/workflows/ci.yml`, `Makefile`, `.zenodo.json`

## Preregistration & DOI
- OSF prereg template: `docs/OSF_PREREG.md` (fill with your project URL).
- Zenodo: create a GitHub release to mint a DOI; then update README and `CITATION.cff`.

## Contact
Spiros Tsoumpis — Department of Marine Engineering, Keratsini, Greece.

## Latest manuscript pointers
- **Word (latest text-only):** `manuscript/luck_unified_TEXT_ONLY_COMPLETE_FINAL_APPS_REFS_PLUS_THEORYUP.docx`
- **PDF (latest text-only):** `docs/luck_unified_TEXT_ONLY_FULL.pdf`

> Note: A figures-embedded Word/PDF is also included (`manuscript/luck_unified_TEXT_ONLY_FINAL_WITH_ALLFIGS.docx`, `docs/luck_unified_TEXT_ONLY_FINAL_WITH_ALLFIGS.pdf`) for figure-rich submission portals.

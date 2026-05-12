# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the Analysis

**Prerequisites:** Python 3.8+, `pandas`, `tabulate`

```bash
pip install pandas tabulate
```

**Run from the repo root** (the script uses a relative path `rpg_persona_data.csv`):

```bash
cd data && python ../scripts/persona_analysis.py
```

Or patch the `load_data` call to use an absolute/relative path when running from the root.

**Outputs** are written to `outputs/` — four files: `persona_profiles.json`, `persona_profiles.md`, `feature_prioritization.csv`, `feature_prioritization.md`.

## Architecture

The single script `scripts/persona_analysis.py` has five stages, each a standalone function:

1. **`load_data`** — reads `data/rpg_persona_data.csv` into a DataFrame. Required columns: `Role`, `Playstyle`, `Pain Points`, `Goals`, `Quotes`, `Preferred Games`, `Wishes Others Understood`, `Weapons`.
2. **`cluster_roles`** — produces granular role counts and maps them to high-level buckets (`DPS`, `Tank`, `Healer`, `Hybrid`) via `HIGH_LEVEL_ROLE_MAPPING`.
3. **`generate_profiles`** — for each unique `Role`, aggregates modal values and exploded list fields into a profile dict.
4. **`generate_feature_matrix`** — builds a role × feature priority table (default `"Low"`), then applies hardcoded rules (e.g. Tank → Shield Mechanics = High) and an optional `custom_logic` override dict.
5. **`save_outputs`** — writes JSON + Markdown profiles and CSV + Markdown matrix to `outputs/`.

## Customising for a New Domain

- **Features**: update the `FEATURES` list at the top of `persona_analysis.py`.
- **Role grouping**: update `HIGH_LEVEL_ROLE_MAPPING`.
- **Priority rules**: extend the `if/elif` block in `generate_feature_matrix`, or pass a `custom_logic` dict at call time to override without touching defaults.
- **Input data**: replace `data/rpg_persona_data.csv` — keep the same column headers, or update `generate_profiles` and `generate_feature_matrix` to match new column names.

## Planned Enhancements (from PRD)

- Contradiction detection between persona needs (currently not implemented)
- Streamlit GUI for non-technical users
- Notion / Google Sheets integration for live outputs
- Automated agents that re-run analysis when new survey data arrives

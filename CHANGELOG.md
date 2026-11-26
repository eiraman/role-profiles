<!--
SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
SPDX-License-Identifier: CC-BY-4.0
-->

# Changelog

All notable changes to the Eiraman Role Profiles registry are documented in this file.
The format is based on [Keep a Changelog 1.1](https://keepachangelog.com/en/1.1.0/), and versions follow
the rules in [community/VERSIONING.md](https://github.com/eiraman/community/blob/main/VERSIONING.md).

This file carries two kinds of version: the version of the **registry** as a whole (the headings below),
and the version of **each profile** (field `versione` in `profilo.json`, repeated in the `Versione` line of
`PROFILO.md`). The profile template (`_modello/`) has no change-history section, and adding one would
change the template every profile must follow, so per-profile changes are recorded here, in the table
"Profile versions" of each release (VERSIONING.md, "Role Profiles").

The qualification state of a profile ("draft, not qualified", qualified, maintained, suspended) is not a
version: it is recorded in the profile and in release notes, and a change of state alone does not bump
the version.

## [Unreleased]

### Added

- This changelog, with the per-profile version table.
- CI workflow `changelog.yml`: a pull request fails if it does not change `CHANGELOG.md`, unless it carries
  the label `no-changelog`.

## [0.1.0] - 2026-11-25

First public release of the registry, published as commits `c9af3d8` and `114f7a2` of
`github.com/eiraman/role-profiles` during the restricted launch of 25 November 2026. It was not tagged:
tagging starts with the next release (VERSIONING.md, "Tags").

### Added

- 40 Role Profiles in 7 families: Functional analysis 5, AWS 6, Azure 7, Databricks 5, FinOps 5,
  Development 7, Web design 5. Each profile has `PROFILO.md` and `profilo.json`; together they hold 350
  catalogued tasks with a Digital Seniority level. Every profile is a **draft, not qualified**.
- `_modello/`, the template every profile starts from.
- `_seniority/`: the Digital Seniority map `seniority.json` (its own field `versione`: 0.1.0), its
  explanation and the catalogue instructions.
- `controllore/`: the AI Coordinator profile (`CONTROLLORE.md`, `AVVIO.md`, `STATO.md` and the Manager
  View generator `tools/vista_manager.py`), version 0.3.0, published as a draft, not qualified, by
  decision of the Human Manager.
- Licences: CC BY 4.0 for the profile texts, Apache-2.0 for `vista_manager.py`, declared in `REUSE.toml`.
- CI: compliance checks (DCO and AI declaration, REUSE, secrets and deny-list) and the profile
  validator from the `tools` repository, pinned by commit SHA (`TOOLS_REF`, set to `558ddb2` in the
  second commit of this release).

### Changed

- Licence of the profile texts: earlier copies, distributed in the eiraman.tech kit on 25 November 2026,
  were under CC BY-NC-ND 4.0 (scripts under MIT). Those copies keep their original licence; this release
  and later ones are under CC BY 4.0 (code Apache-2.0).

### Profile versions

| Profile | Version | Date | State |
|---|---|---|---|
| `analisi-funzionale/analista-funzionale` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `analisi-funzionale/facilitatore-design-thinking` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `analisi-funzionale/technical-writer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `analisi-funzionale/tester-funzionale` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `analisi-funzionale/utente-simulato` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `aws/aws-architect` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `aws/aws-database-specialist` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `aws/aws-developer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `aws/aws-devops-engineer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `aws/aws-operations` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `aws/aws-security-engineer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `azure/azure-architect` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `azure/azure-cloud-operations` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `azure/azure-dba` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `azure/azure-developer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `azure/azure-incident-manager` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `azure/azure-release-engineer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `azure/azure-security-engineer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `databricks/databricks-analytics-engineer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `databricks/databricks-data-engineer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `databricks/databricks-governance-steward` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `databricks/databricks-ml-engineer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `databricks/databricks-platform-admin` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `finops/finops-cost-allocation-analyst` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `finops/finops-for-ai` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `finops/finops-forecast-budget` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `finops/finops-practitioner` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `finops/finops-rate-optimization` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `sviluppo/dotnet-developer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `sviluppo/go-developer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `sviluppo/java-developer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `sviluppo/python-developer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `sviluppo/shell-iac-developer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `sviluppo/sql-developer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `sviluppo/typescript-developer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `web-design/accessibility-specialist` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `web-design/frontend-developer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `web-design/ux-designer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `web-design/ux-writer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `web-design/web-designer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `controllore/` (AI Coordinator) | 0.3.0 | 2026-11-25 | draft, not qualified |

Notes on the history before this release, from the project's activity log:

- The 40 profiles were written on 25 November 2026 by seven executor agents, one per family, with
  independent reviews per family; the Digital Seniority catalogue (350 tasks) was added the same day.
  The profiles were never released before, so each starts at 0.1.0.
- The AI Coordinator profile was first written on 24 November 2026 and set to version 0.3.0 on
  25 November 2026, when the roles were renamed to "AI Coordinator" and "Human Manager". The log does not
  record whether versions 0.1.x or 0.2.x of it were ever labelled; none was released on its own.

[Unreleased]: https://github.com/eiraman/role-profiles/compare/114f7a2d656698d2057aa176f0d18139bfeca332...main
[0.1.0]: https://github.com/eiraman/role-profiles/tree/114f7a2d656698d2057aa176f0d18139bfeca332

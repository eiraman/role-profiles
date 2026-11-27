<!--
SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
SPDX-License-Identifier: CC-BY-4.0
-->

# Changelog of the local engines map

All notable changes to the local engines map are documented in this file: `motori-locali.json` (field `versione`, the version source) and `MOTORE-LOCALE.md`, the common rules, which carry the same version. The Digital Seniority map has its own file, [`CHANGELOG-seniority.md`](CHANGELOG-seniority.md). The format is based on [Keep a Changelog 1.1](https://keepachangelog.com/en/1.1.0/), and versions follow the rules in [community/VERSIONING.md](https://github.com/eiraman/community/blob/main/VERSIONING.md), section 2.2.

## [Unreleased]

## [0.1.1] - 2026-11-27

Alignment of profiles and families to the local engine map (Change Request CR-030, work package WP-30C). Bump: PATCH (0.1.0 to 0.1.1), because the map only gains a cross-reference and a format fix, with the same meaning. The engine stays «da qualificare», no task is added or assigned, no fallback changes.

### Changed

- `MOTORE-LOCALE.md`: the `Metodo` line now reads «The Eiraman Guide 1.0.0-rc.5» in place of «Guida 1.0.0-rc.5», as in the other files; a closing sentence says that every `FAMIGLIA.md` repeats the declaration in its paragraph «Motore locale», and that profiles and families not listed in the table have no task assigned to the local engine.
- `motori-locali.json`: the field `nota` gains the same cross-reference; `versione` 0.1.1.
- Consistency with the profiles: the families carry the paragraph «Motore locale» (aws, azure, databricks, finops, sviluppo, web-design, analisi-funzionale, governo); `revisore-ai` and `facilitatore-design-thinking` (engine «da qualificare», no task) state the conditions of use; the note of task T08 of `aws-operations` and `aws-security-engineer` no longer implies an assigned use.

Earlier history: see the registry [`CHANGELOG.md`](../CHANGELOG.md) (release 0.10.0, local engine, CR-021).

<!--
SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
SPDX-License-Identifier: CC-BY-4.0
-->

# Changelog

All notable changes to the common rules of the family «Azure» (`FAMIGLIA.md`) are documented in this file. The Role Profiles of the family have their own changelogs, in their folders. The format is based on [Keep a Changelog 1.1](https://keepachangelog.com/en/1.1.0/), and versions follow the rules in [community/VERSIONING.md](https://github.com/eiraman/community/blob/main/VERSIONING.md), section 2.2, applied to the family file.

## [Unreleased]

## [0.4.0] - 2026-11-27

Realignment of the family rules to The Eiraman Guide 1.0.0-rc.5 and to the use of the local engine (Change Request CR-030, work package WP-30C). Bump: MINOR (0.3.0 to 0.4.0), because the paragraph «Motore locale» adds a stated limit to the family rules (VERSIONING.md, section 2.2: «a rule, limit or task is added or broadened»), even though it restates `_seniority/MOTORE-LOCALE.md`. No rule is removed.

### Added

- The paragraph «Motore locale», the same for every family. It says that no task of the family is assigned to the local engine except those listed in `_seniority/motori-locali.json` (none); that the engine is «da qualificare» on every task and, until a task is qualified and the Human Manager has approved the engine, the task follows the catalogue row of the profile (fallback); that a refusal does not pass to another engine; and that the «modello locale» row of `motori` in each profile only states the minimum size and assigns nothing. It restates `_seniority/MOTORE-LOCALE.md` (rules 1, 3, 7, 9, 10); it introduces no new local-engine task.

### Changed

- Method: the `Metodo` line of `FAMIGLIA.md` now names The Eiraman Guide 1.0.0-rc.5 in place of «Specifica Eiraman 0.3 e Guida 1.0.0-rc.5».
- Precedence clause: «prevalgono, nell'ordine: Specifica Eiraman, mandato del progetto, questo file, il profilo del ruolo» now reads «la Guida (The Eiraman Guide), il mandato del progetto, questo file, il profilo del ruolo».
- Citations: 13 «spec §N» citation(s) remapped to Guide sections; the «Convenzione delle fonti» line now reads «Guida §N» in place of «spec §N».
- Section numbering and wording of the rules are otherwise unchanged; no rule is removed.

Remap used for the citations «spec §N» of the Italian specification 0.3, now historical: §1 → Guide §2; §2 → §4; §3 → §5; §4 → §6; §4 bis → §7 (and §7.1); §5 → §8 and §8.1 (Scope Management → §9); §6 → §9 and §9.1; §6 bis → §10; §7 → §11; §8 → §12 (and §9, §14.1); §9 → §13 and §4 (the separation between code and architecture documents is a profile rule); §10 → §14 and §14.1; §11 → §15 and §5. The target is chosen by the content of each citation, using the Guide traceability table.

Earlier history: see the registry [`CHANGELOG.md`](../CHANGELOG.md) (table «Profile versions»).

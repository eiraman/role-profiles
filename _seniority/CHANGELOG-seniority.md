<!--
SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
SPDX-License-Identifier: CC-BY-4.0
-->

# Changelog of the Digital Seniority map

All notable changes to the Digital Seniority map are documented in this file: `seniority.json`, which is the version source (field `versione`), and the two documents that explain it, `SENIORITY.md` and `ISTRUZIONI-CATALOGO.md`, which have no version of their own. The local engines map has its own file, [`CHANGELOG-motori-locali.md`](CHANGELOG-motori-locali.md). The format is based on [Keep a Changelog 1.1](https://keepachangelog.com/en/1.1.0/), and versions follow the rules in [community/VERSIONING.md](https://github.com/eiraman/community/blob/main/VERSIONING.md), section 2.2 («The Digital Seniority map follows the profile rules for its own number»).

## [Unreleased]

## [0.2.1] - 2026-11-27

Realignment of the references to The Eiraman Guide 1.0.0-rc.6 (Change Request CR-030, work package WP-30C). Bump: PATCH (0.2.0 to 0.2.1), because only source references change, with the same meaning. No level, configuration, fallback value or exception changes.

### Changed

- `seniority.json`, field `nota`: the citation «Guida 1.0.0-rc.3, §7.1, «Catalogue»» now cites 1.0.0-rc.6; `versione` 0.2.1, `data` 2026-11-27.
- `ISTRUZIONI-CATALOGO.md`, instruction 5: the line to add to section 1 of each profile now cites «Guida 1.0.0-rc.6, §7.1, «Fallback»» instead of rc.3.
- Section 10 of every `PROFILO.md` is regenerated: the generated text names the version of this map («versione 0.2.1»).
- Local engine: this map needs no new text. `SENIORITY.md` (point 8) already says that a local engine is not a level of this map and that its rules are in `MOTORE-LOCALE.md`; a task given to the local engine carries in the catalogue the level of its fallback row.

Earlier history: see the registry [`CHANGELOG.md`](../CHANGELOG.md) (table «Profile versions» and the entries of the releases 0.6.0 and later for the map).

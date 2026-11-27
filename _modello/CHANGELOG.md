<!--
SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
SPDX-License-Identifier: CC-BY-4.0
-->

# Changelog

All notable changes to the Role Profile template (`_modello/PROFILO.md` and `_modello/profilo.json`) are documented in this file. The templates `business-analyst` and `user-persona` in the subfolders have their own changelogs. The format is based on [Keep a Changelog 1.1](https://keepachangelog.com/en/1.1.0/), and versions follow the rules in [community/VERSIONING.md](https://github.com/eiraman/community/blob/main/VERSIONING.md), section 2.2. The version of the template is the field `versione` of `_modello/profilo.json`.

## [Unreleased]

## [0.2.1] - 2026-11-27

Realignment of the template to The Eiraman Guide 1.0.0-rc.6 (Change Request CR-030, work package WP-30C). Bump: PATCH (0.2.0 to 0.2.1), because only a source reference and the method line change, with the same meaning (VERSIONING.md, section 2.2). No section, heading, JSON field or validator rule is added, removed or renamed, so the format that every profile follows is unchanged and no profile fails the validator because of this change.

### Changed

- Method: the `Metodo` placeholder line of `PROFILO.md` now reads «The Eiraman Guide 1.0.0-rc.6» in place of «Specifica Eiraman 0.3»; the field `metodo` of `profilo.json` reads «The Eiraman Guide 1.0.0-rc.6; §13 (limiti dichiarati), §5 e §14 (modalità di classificazione)» in place of «Eiraman 0.3; Guida 1.0.0-rc.5 per …».
- Citation: in the instruction of section 5 (forbidden actions), «spec §3» is now «Guida §5» (the sentence already cited Guide 1.0.0-rc.6, §5, «Do»).
- `versione` of `profilo.json` 0.2.1; `data` is 2026-11-27.
- Local engine: the template needs no new text. Its `motori` example keeps the «modello locale» entry «da qualificare», as `_seniority/MOTORE-LOCALE.md` and the «Motore locale» paragraph of the family files state; a new profile that is assigned a task by `_seniority/motori-locali.json` follows the rules of that file.

Remap used for «spec §N» of the Italian specification 0.3, now historical: §3 → Guide §5.

Earlier history: see the registry [`CHANGELOG.md`](../CHANGELOG.md) (table «Profile versions»).

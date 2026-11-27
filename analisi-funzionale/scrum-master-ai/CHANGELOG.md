<!--
SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
SPDX-License-Identifier: CC-BY-4.0
-->

# Changelog

All notable changes to the Role Profile `scrum-master-ai`, «Scrum Master AI» are documented in this file. The format is based on [Keep a Changelog 1.1](https://keepachangelog.com/en/1.1.0/), and versions follow the rules in [community/VERSIONING.md](https://github.com/eiraman/community/blob/main/VERSIONING.md), section 2.2.

## [Unreleased]

## [0.3.1] - 2026-11-27

Realignment of the profile to The Eiraman Guide 1.0.0-rc.5 and to the use of the local engine (Change Request CR-030, work package WP-30C). Bump: PATCH (0.3.0 to 0.3.1), because only source references and metadata change, with the same meaning (VERSIONING.md, section 2.2: «corrected source references with the same meaning»). No rule, limit, task, deliverable or Digital Seniority level is added, removed or changed. The qualification state stays «draft, not qualified».

### Changed

- Method: `metodo` of `profilo.json` and the `Metodo` line of `PROFILO.md` now name The Eiraman Guide 1.0.0-rc.5 and the relevant sections (`§3 e §7 (regole di squadra e di contesto), §14 «Classification mode» (modalità di classificazione, rifiuti dei modelli), §7.1 «Fallback»`), in place of «Eiraman 0.3; Guida 1.0.0-rc.5 per le regole di squadra e di contesto, la modalità di classificazione e i rifiuti dei modelli (§14) e il ripiego della Seniority Digitale».
- Source: the entry «Specifica Eiraman 0.3» of `competenze_fonti` (`§2 Ruoli AI specialistici; §4 bis Squadre e Scrum agentico, Scrum of Scrums e ruolo del Coordinatore AI; §8 Log Tracker`) is now «The Eiraman Guide 1.0.0-rc.5», with the matching Guide sections. Its `url` now points to the Guide repository (it was empty).
- Source: 1 entry(ies) «The Eiraman Guide» of `competenze_fonti` naming rc.1 to rc.4 now name 1.0.0-rc.5.
- Citations: 1 «spec §N» citation(s) in `PROFILO.md` remapped to Guide sections.
- Guide versions: 1 citation(s) of Guide 1.0.0-rc.1 to rc.4 now cite 1.0.0-rc.5; every cited section and label was checked against the rc.5 text.
- Section 10 of `PROFILO.md` regenerated with `attiva_profilo.py --scrivi-catalogo`: the generated text names the version of the Digital Seniority map (now 0.2.1); no task, deliverable or level changes.
- `data` of `profilo.json` set to 2026-11-27.
- The row that named the specification 0.3 as «fonte storica» of the same rules is kept as a Guide row that states the old numbering (§2, §4 bis, §8), so that no source is lost.
- Local engine: no task of this profile is assigned to the local engine; the «modello locale» entry of `motori` stays «da qualificare», as `_seniority/MOTORE-LOCALE.md` and the «Motore locale» paragraph of the family `FAMIGLIA.md` state. No change to this profile's text.

Remap used for the citations «spec §N» of the Italian specification 0.3, now historical: §1 → Guide §2; §2 → §4; §3 → §5; §4 → §6; §4 bis → §7 (and §7.1); §5 → §8 and §8.1 (Scope Management → §9); §6 → §9 and §9.1; §6 bis → §10; §7 → §11; §8 → §12 (and §9, §14.1); §9 → §13 and §4 (the separation between code and architecture documents is a profile rule); §10 → §14 and §14.1; §11 → §15 and §5. The target is chosen by the content of each citation, using the Guide traceability table.

Earlier history: see the registry [`CHANGELOG.md`](../../CHANGELOG.md) (table «Profile versions»).

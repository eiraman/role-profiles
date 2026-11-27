<!--
SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
SPDX-License-Identifier: CC-BY-4.0
-->

# Changelog

All notable changes to the Role Profile `revisore-ai`, «Revisore AI» are documented in this file. The format is based on [Keep a Changelog 1.1](https://keepachangelog.com/en/1.1.0/), and versions follow the rules in [community/VERSIONING.md](https://github.com/eiraman/community/blob/main/VERSIONING.md), section 2.2.

## [Unreleased]

## [0.5.0] - 2026-11-27

Realignment of the profile to The Eiraman Guide 1.0.0-rc.6 and to the use of the local engine (Change Request CR-030, work package WP-30C). Bump: MINOR (0.4.0 to 0.5.0), because a limit is added to what the profile may do with the local engine (VERSIONING.md, section 2.2: «a rule, limit or task is added or broadened»). No rule is removed. The qualification state stays «draft, not qualified».

### Changed

- Method: `metodo` of `profilo.json` and the `Metodo` line of `PROFILO.md` now name The Eiraman Guide 1.0.0-rc.6 and the relevant sections (`§3 «Context Consistency and Independence» e §7 (blinding), §5 E6 (misura), §7.1 «Fallback», §8 «Question round», §14 «Classification mode» (due modalità di classificazione, rifiuti dei modelli)`), in place of «Eiraman 0.3; Guida 1.0.0-rc.3 per le regole di contesto, la misura E6 e il ripiego della Seniority Digitale; Guida 1.0.0-rc.5 per le due modalità di classificazione, i rifiuti dei modelli e il giro di domande della Scoperta».
- Source: 2 entry(ies) «The Eiraman Guide» of `competenze_fonti` naming rc.1 to rc.4 now name 1.0.0-rc.6.
- Citations: 5 «spec §N» citation(s) in `PROFILO.md` remapped to Guide sections.
- Guide versions: 12 citation(s) of Guide 1.0.0-rc.1 to rc.4 now cite 1.0.0-rc.6; every cited section and label was checked against the rc.6 text.
- Section 10 of `PROFILO.md` regenerated with `attiva_profilo.py --scrivi-catalogo`: the generated text names the version of the Digital Seniority map (now 0.2.1); no task, deliverable or level changes.
- `data` of `profilo.json` set to 2026-11-27.
- The clause «nel testo della 1.0.0-rc.3» on E6 Measurement is dropped from the source row and the source reference: rc.6 is the only text cited.
- Local engine: the sentence that made a local model «an option» now says it is an option only under the conditions of `_seniority/MOTORE-LOCALE.md` (engine «da qualificare», no task assigned to this profile; its qualification is done separately). This conditions a permitted use, hence the MINOR bump.

Remap used for the citations «spec §N» of the Italian specification 0.3, now historical: §1 → Guide §2; §2 → §4; §3 → §5; §4 → §6; §4 bis → §7 (and §7.1); §5 → §8 and §8.1 (Scope Management → §9); §6 → §9 and §9.1; §6 bis → §10; §7 → §11; §8 → §12 (and §9, §14.1); §9 → §13 and §4 (the separation between code and architecture documents is a profile rule); §10 → §14 and §14.1; §11 → §15 and §5. The target is chosen by the content of each citation, using the Guide traceability table.

Earlier history: see the registry [`CHANGELOG.md`](../../CHANGELOG.md) (table «Profile versions»).

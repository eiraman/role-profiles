<!--
SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
SPDX-License-Identifier: CC-BY-4.0
-->

# Changelog

All notable changes to the Role Profile `security-officer`, «Security Officer» are documented in this file. The format is based on [Keep a Changelog 1.1](https://keepachangelog.com/en/1.1.0/), and versions follow the rules in [community/VERSIONING.md](https://github.com/eiraman/community/blob/main/VERSIONING.md), section 2.2.

## [Unreleased]

## [0.4.1] - 2026-11-27

Realignment of the profile to The Eiraman Guide 1.0.0-rc.6 and to the use of the local engine (Change Request CR-030, work package WP-30C). Bump: PATCH (0.4.0 to 0.4.1), because only source references and metadata change, with the same meaning (VERSIONING.md, section 2.2: «corrected source references with the same meaning»). No rule, limit, task, deliverable or Digital Seniority level is added, removed or changed. The qualification state stays «draft, not qualified».

### Changed

- Method: `metodo` of `profilo.json` and the `Metodo` line of `PROFILO.md` now name The Eiraman Guide 1.0.0-rc.6 and the relevant sections (`§3 «Context Consistency and Independence» e §7 (blinding), §14 «Applicability gate» nelle due modalità di classificazione, «Risk profile», §14.2 «Running above the qualified level», §12 «Security Report», §14 «Local engines in the informative mode» (motori locali, rifiuti dei modelli), §7.1 «Fallback»`), in place of «Eiraman 0.3; Guida 1.0.0-rc.5 per le regole di contesto, il gate di applicabilità nelle due modalità di classificazione (bloccante e informativa), il profilo di rischio, la decisione di procedere sopra il livello qualificato, il Security Report, i rifiuti dei modelli, i motori locali e il ripiego della Seniority Digitale».
- Section 10 of `PROFILO.md` regenerated with `attiva_profilo.py --scrivi-catalogo`: the generated text names the version of the Digital Seniority map (now 0.2.1); no task, deliverable or level changes.
- `data` of `profilo.json` set to 2026-11-27.
- Local engine: tasks T11 and T12 are the ones listed in `_seniority/motori-locali.json`; their text is unchanged and consistent with `_seniority/MOTORE-LOCALE.md` 0.1.1 (engine «da qualificare», fallback in the catalogue row).

Remap used for the citations «spec §N» of the Italian specification 0.3, now historical: §1 → Guide §2; §2 → §4; §3 → §5; §4 → §6; §4 bis → §7 (and §7.1); §5 → §8 and §8.1 (Scope Management → §9); §6 → §9 and §9.1; §6 bis → §10; §7 → §11; §8 → §12 (and §9, §14.1); §9 → §13 and §4 (the separation between code and architecture documents is a profile rule); §10 → §14 and §14.1; §11 → §15 and §5. The target is chosen by the content of each citation, using the Guide traceability table.

Earlier history: see the registry [`CHANGELOG.md`](../../CHANGELOG.md) (table «Profile versions»).

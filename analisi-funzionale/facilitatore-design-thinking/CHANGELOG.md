<!--
SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
SPDX-License-Identifier: CC-BY-4.0
-->

# Changelog

All notable changes to the Role Profile `facilitatore-design-thinking`, «Facilitatore di Design Thinking» are documented in this file. The format is based on [Keep a Changelog 1.1](https://keepachangelog.com/en/1.1.0/), and versions follow the rules in [community/VERSIONING.md](https://github.com/eiraman/community/blob/main/VERSIONING.md), section 2.2.

## [Unreleased]

## [0.8.0] - 2026-11-27

Realignment of the profile to The Eiraman Guide 1.0.0-rc.5 and to the use of the local engine (Change Request CR-030, work package WP-30C). Bump: MINOR (0.7.0 to 0.8.0), because a limit is added to what the profile may do with the local engine (VERSIONING.md, section 2.2: «a rule, limit or task is added or broadened»). No rule is removed. The qualification state stays «draft, not qualified».

### Changed

- Method: `metodo` of `profilo.json` and the `Metodo` line of `PROFILO.md` now name The Eiraman Guide 1.0.0-rc.5 and the relevant sections (`§3 «Context Consistency and Independence» e §7 (blinding), §8 «Question round» e «Convergence», §14 «Classification mode», §7.1 «Fallback»`), in place of «Eiraman 0.3; Guida 1.0.0-rc.5 per le regole di contesto, il giro di domande e la convergenza della Scoperta (§8), la modalità di classificazione (§14) e il ripiego della Seniority Digitale».
- Source: the entry «Specifica Eiraman 0.3» of `competenze_fonti` (`§4 K1-K3, §4 bis, §5 Design Thinking affidato all'AI`) is now «The Eiraman Guide 1.0.0-rc.5», with the matching Guide sections. Its `url` now points to the Guide repository (it was empty).
- Source: 1 entry(ies) «The Eiraman Guide» of `competenze_fonti` naming rc.1 to rc.4 now name 1.0.0-rc.5.
- Citations: 12 «spec §N» citation(s) in `PROFILO.md` remapped to Guide sections.
- Guide versions: 2 citation(s) of Guide 1.0.0-rc.1 to rc.4 now cite 1.0.0-rc.5; every cited section and label was checked against the rc.5 text.
- Section 10 of `PROFILO.md` regenerated with `attiva_profilo.py --scrivi-catalogo`: the generated text names the version of the Digital Seniority map (now 0.2.1); no task, deliverable or level changes.
- `data` of `profilo.json` set to 2026-11-27.
- History: the sentence «Dalla Guida 1.0.0-rc.2 la convergenza …» now cites the Guide §8 «Convergence» without the version history; the rule is unchanged (the Facilitator leads convergence).
- Local engine: the sentence that made a local model «an option» now says it is an option only under the conditions of `_seniority/MOTORE-LOCALE.md` (engine «da qualificare», no task assigned to this profile; its qualification is done separately). This conditions a permitted use, hence the MINOR bump.

Remap used for the citations «spec §N» of the Italian specification 0.3, now historical: §1 → Guide §2; §2 → §4; §3 → §5; §4 → §6; §4 bis → §7 (and §7.1); §5 → §8 and §8.1 (Scope Management → §9); §6 → §9 and §9.1; §6 bis → §10; §7 → §11; §8 → §12 (and §9, §14.1); §9 → §13 and §4 (the separation between code and architecture documents is a profile rule); §10 → §14 and §14.1; §11 → §15 and §5. The target is chosen by the content of each citation, using the Guide traceability table.

Earlier history: see the registry [`CHANGELOG.md`](../../CHANGELOG.md) (table «Profile versions»).

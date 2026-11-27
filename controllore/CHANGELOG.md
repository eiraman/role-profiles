<!--
SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
SPDX-License-Identifier: CC-BY-4.0
-->

# Changelog

All notable changes to the AI Coordinator profile (`controllore/`: `CONTROLLORE.md`, `AVVIO.md`, `STATO.md`
and `tools/vista_manager.py`) are documented in this file. The format is based on
[Keep a Changelog 1.1](https://keepachangelog.com/en/1.1.0/), and versions follow the rules in
[community/VERSIONING.md](https://github.com/eiraman/community/blob/main/VERSIONING.md). The version source is
the `Versione` line of `CONTROLLORE.md` (decision D-VER-2: one changelog per artifact).

Versions up to 0.12.0 are recorded in the registry [CHANGELOG.md](../CHANGELOG.md), in the table "Profile
versions" of each release. This file starts with 0.13.0.

## [Unreleased]

## [0.13.0] - 2026-11-27

Scope: Change Request CR-030 of the method project, Work Package WP-30B. The profile's normative base becomes
The Eiraman Guide 1.0.0-rc.5 alone, instead of the Italian specification 0.3 plus four blocks of Guide deltas.

Bump: MINOR, marked **breaking** (profile at 0.y.z; VERSIONING.md 2.2 and 2.6). The precedence rule is
reversed: the specification 0.3 (`framework/Eiraman.md`) no longer prevails over the profile and is no longer
read; `guide/EIRAMAN-GUIDE.md` does. A rule that only the specification 0.3 set, and that neither the Guide nor
this profile carries, is no longer required. No operative rule of the profile is removed: each rule of the four
delta blocks and each rule cited to the specification is kept, mapped to the Guide or kept as a profile rule.
The profile stays **draft, not qualified**; no qualification case is added or removed.

### Changed

- `CONTROLLORE.md`, header: "Metodo: The Eiraman Guide 1.0.0-rc.5" (was "Specifica Eiraman 0.3 e The Eiraman
  Guide 1.0.0-rc.5").
- `CONTROLLORE.md` §1: the AI Coordinator applies The Eiraman Guide 1.0.0-rc.5 (canonical English text; curated
  Italian translation 1.0.0-rc.5+it.1); `guide/EIRAMAN-GUIDE.md` in the working folder, when present, prevails
  over the profile in a conflict. **Breaking** (was: the specification 0.3 in `framework/Eiraman.md` prevailed,
  except for the Guide rules listed in §1).
- `CONTROLLORE.md` §1: the four delta blocks (Guide 1.0.0-rc.2 to rc.5, "on these points this profile prevails
  over the specification 0.3") become one list of Guide rules grouped by RFC (0001, 0003, 0004, 0005), each with
  its Guide paragraph and the profile section that applies it. Every item is kept.
- `CONTROLLORE.md`: every reference to the specification 0.3 ("spec §N") is remapped to the Guide paragraph that
  carries the rule (§4, §5, §6, §7, §7.1, §8, §8.1, §9, §11, §12, §13, §14.2, §15). Where the Guide leaves a value
  to the mandate, the profile names the Guidance of the Extended Framework (`guidance/VALUES.md`, fallback SD3)
  or states its own indicative value (one page per decision record). The rule on the project that maintains the
  method, and the list of what the High Level Architectural View leaves out, are stated as profile rules.
- `CONTROLLORE.md`: "Guida 1.0.0-rc.5, §N" is written "Guida §N", since the Guide 1.0.0-rc.5 is the base.
- `CONTROLLORE.md` §7: the hostile-input rule cites Guide §11, "Hostile-input test" (was "P4", a label with no
  source in the Guide or the specification 0.3).
- `CONTROLLORE.md` §1 bis, §3 and §8: the local engine is referred to `_seniority/MOTORE-LOCALE.md` and to the
  Guide (§7 "Hard blinding", §11 "Data classes per provider", §14 "Local engines in the informative mode"), with
  its state "da qualificare" on all three tasks of the AI Coordinator. In §3, listing the local engine in the
  mandate's table of data classes per provider is stated as a registry convention (rules 4 and 9 of
  `MOTORE-LOCALE.md`), not as a Guide rule. Tasks and fallbacks are unchanged.
- `CONTROLLORE.md` §8, table "Modelli abilitati": the local engine row now also requires qualification on the
  task, states that the engine is "da qualificare" on every task, and requires approval by the Human Manager in
  both modes (blocking: registry convention), as §3 already did. This narrows the row: before, it bound the
  local engine only in the informative mode and left the blocking mode unconstrained.
- `CONTROLLORE.md` §3 and §9 (CX-05): the label "PA-6" is removed; the rule cites Guide §6, "Security and
  personal data", only.
- `CONTROLLORE.md` §3 quater: the profile has its own version and this changelog; earlier versions are in the
  registry changelog.
- `AVVIO.md`: the reference to the Guide is written "Guida §14" (was "Guida 1.0.0-rc.5, §14").
- `AVVIO.md`: the kit carries the Guide as `guide/EIRAMAN-GUIDE.md` and `guide/EIRAMAN-GUIDE.it.md`, and the
  start message reads `guide/EIRAMAN-GUIDE.md` (was the specification as `framework/Eiraman.md`).
- `STATO.md`: example `"metodo": "The Eiraman Guide 1.0.0-rc.5"` (was "Eiraman 0.3; Guida 1.0.0-rc.5"); the
  denominator rule cites Guide §12 only.

### Open points

- `CONTROLLORE.md` and `AVVIO.md` cite the curated Italian translation 1.0.0-rc.5+it.1
  (`guide/EIRAMAN-GUIDE.it.md`). It is not released yet: it ships with the next release of the `guide`
  repository, and this version depends on that release.

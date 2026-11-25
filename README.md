<!--
SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
SPDX-License-Identifier: CC-BY-4.0
-->

# Eiraman Role Profiles

> **Status: every profile in this repository is a draft, not qualified.**
> No profile has passed its qualification suite or been published by a domain reviewer.
> Do not use them in projects, at any applicability level, until they are qualified
> (see [CONTRIBUTING](https://github.com/eiraman/.github/blob/main/CONTRIBUTING.md), "Profile states").

A Role Profile tells an AI agent how to act in a specialist role, and tells the AI Coordinator
when and how to use it. This repository is the registry of the Eiraman Role Profiles.

## Layout

Each profile is a folder `<family>/<profile-id>/` with two files:

| File | For | Content |
|---|---|---|
| `PROFILO.md` | the LLM engine that takes the role | identity and purpose, core competences and methods with sources, responsibilities, allowed and forbidden actions, communication rules, document repository, declared limits, qualification suite, task catalogue (section 10, generated) |
| `profilo.json` | the AI Coordinator | task and deliverable catalogue with Digital Seniority level (SD1–SD5), enabled engines, Mode and Role per vendor, Unit Cost per engine, deterministic tools, allowed writes, qualification |

Each family folder has a `FAMIGLIA.md` with the rules shared by its profiles. A profile `id` is unique
across the registry and matches its folder name.

| Family | Folder | Profiles |
|---|---|---|
| Functional analysis | `analisi-funzionale/` | 5 |
| AWS | `aws/` | 6 |
| Azure | `azure/` | 7 |
| Databricks | `databricks/` | 5 |
| FinOps | `finops/` | 5 |
| Development | `sviluppo/` | 7 |
| Web design | `web-design/` | 5 |

Total: 40 profiles. Also included: `_modello/` (the template every profile starts from),
`_seniority/` (the Digital Seniority map, `seniority.json`, and its explanation) and `controllore/`
(the AI Coordinator profile, see below).

The profile texts are in Italian; file and section names are Italian (`PROFILO.md`, `profilo.json`,
`FAMIGLIA.md`). An English registry with English file names is an open item of the DevSecOps & Tooling
working group.

Not included: the tools (`valida_profilo.py`, `attiva_profilo.py`), which live in the
[`tools`](https://github.com/eiraman/tools) repository.

## The AI Coordinator profile (`controllore/`)

> **Status: draft, not qualified.** Qualifying it is among the first tasks of the founding maintainers.

`controllore/` holds the profile of the **AI Coordinator**, the role that runs a project on behalf of the
Human Manager. It is published as a draft so that contributors can review and qualify it. It is not a
specialist Role Profile and does not follow the `PROFILO.md` + `profilo.json` structure:

| File | Content |
|---|---|
| `CONTROLLORE.md` | the instructions the AI engine loads to act as AI Coordinator: mandate, session start, Waves, delegation, Digital Seniority, closure, escalation, Manager View, project registry, hard limits, qualification |
| `AVVIO.md` | how a Human Manager starts the AI Coordinator in a project folder |
| `STATO.md` | format of `eiraman/stato.json`, the snapshot read by the Manager View |
| `tools/vista_manager.py` | generator of the Manager View (code, Apache-2.0) |

Why it is not forced into the `PROFILO.md` structure: the ten sections of the template describe a
specialist that the AI Coordinator activates (competences with sources, task catalogue with Digital
Seniority levels, Mode and Role per vendor, Unit Cost). The AI Coordinator is the activating role itself:
it has no task catalogue to be activated from, no `profilo.json` for another coordinator to read, and its
rules are the method's own procedure rather than a profession's. A `PROFILO.md` + `profilo.json` pair would
be empty in half its fields or would duplicate the method. The validator's structural checks therefore do
not apply; its forbidden-content checks (local paths, credentials, private keys and the local deny-list)
do, and CI runs them on `controllore/` (`.github/workflows/validate-profiles.yml`). Whether the AI
Coordinator should get a profile structure of its own is an open item for the Test & Quality domain.

## Rules for writing a profile

1. Start from `_modello/`. Do not remove sections: an empty section says "not applicable" and why.
2. Every rule cites its source with a precise reference. A rule without a source is marked as a profile convention.
3. Thresholds not yet calibrated are marked "to be calibrated"; unknowns are "unknown, evidence needed".
4. No client names, credentials, local paths or personal data.
5. The validator from the `tools` repository checks structure, fields and forbidden content. A profile that fails it does not go to review.
6. A profile stays "draft, not qualified" until it passes its suite and a domain reviewer, who is not the author, publishes it.

## Validating locally

The tools expect to sit in `<registry>/_strumenti/`, next to `_seniority/`. `_strumenti/` is git-ignored here.

```sh
git clone https://github.com/eiraman/tools ../tools
mkdir -p _strumenti && cp ../tools/valida_profilo.py ../tools/attiva_profilo.py _strumenti/
python3 _strumenti/valida_profilo.py azure/azure-architect
```

CI does the same on every pull request, for the profiles it changes (`.github/workflows/validate-profiles.yml`).

## Review and ownership

`CODEOWNERS` maps each family to the team of its publishing domain (`GOVERNANCE.md` §4.5, `WORKING-GROUPS.md` §3).
A domain without a reviewer cannot publish: until its team has members, pull requests in that folder cannot be merged.

## Licence

Role Profiles: [CC BY 4.0](LICENSE.md). Licensing per file is declared in `REUSE.toml`.
Contributions need a DCO sign-off on every commit.

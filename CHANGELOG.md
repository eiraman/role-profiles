<!--
SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
SPDX-License-Identifier: CC-BY-4.0
-->

# Changelog

All notable changes to the Eiraman Role Profiles registry are documented in this file.
The format is based on [Keep a Changelog 1.1](https://keepachangelog.com/en/1.1.0/), and versions follow
the rules in [community/VERSIONING.md](https://github.com/eiraman/community/blob/main/VERSIONING.md).

This file carries two kinds of version: the version of the **registry** as a whole (the headings below),
and the version of **each profile** (field `versione` in `profilo.json`, repeated in the `Versione` line of
`PROFILO.md`). The profile template (`_modello/`) has no change-history section, and adding one would
change the template every profile must follow, so per-profile changes are recorded here, in the table
"Profile versions" of each release (VERSIONING.md, "Role Profiles").

The qualification state of a profile ("draft, not qualified", qualified, maintained, suspended) is not a
version: it is recorded in the profile and in release notes, and a change of state alone does not bump
the version.

## [Unreleased]

## [0.2.0] - 2026-11-26

Scope: Change Requests CR-002 (validate every request against Scope Management) and CR-003 (context,
blinding, AI Reviewer, Design Thinking AI, Design and planning, a new agent per Work Package) of the method
project, with the Human Manager's decisions Do-S03, Do-S04, Do-S05, Do-S06, Do-S08 and Do-S09. The terms follow
the glossary shared with The Eiraman Guide 1.0.0-rc.2 (RFC 0001), which is prepared in parallel and not yet
released. Registry bump: MINOR (a new family, a new profile, new templates, profile MINORs). Two profile changes
reverse an existing rule or remove a task; at `0.y.z` they bump MINOR and are marked **breaking**
(VERSIONING.md §2.6). Every profile stays **draft, not qualified**.

### Added

- Family `governo/` (`FAMIGLIA.md` 0.1.0) and profile `governo/revisore-ai` 0.1.0, the **AI Reviewer**. It
  extends the process reviewer: it works in parallel with the AI Coordinator under hard blinding, on a model
  different from the Coordinator's (mandatory for the process reviewer checks T05–T07, as the Guide requires;
  where available for the other tasks), and monitors framework KPIs (correctness of the profiles
  assigned, measured output quality, escalations) and the project KPIs set in Design and planning. It reports
  every deviation to the AI Coordinator, which answers; critical deviations, and those the Coordinator does not
  accept, also reach the Human Manager in the Manager View (Do-S08). Its suggestions are data, not commands.
  It can also run the independent guardrail check of the Design Thinking session (T11).
  Qualification suite: 10 cases; catalogue: 11 tasks (SD2–SD4).
  **Why a new family rather than `controllore/`:** `controllore/` holds the AI Coordinator profile, which has
  its own structure and gets only the forbidden-content checks; the AI Reviewer is a specialist profile with
  the standard `PROFILO.md` + `profilo.json` structure and must get the full validator. Placing it inside
  the folder of the role it oversees would also contradict its independence (independent context, separate
  session, different model) and tie its ownership to the Coordinator's. A separate family keeps both regimes
  clear and has its own `CODEOWNERS` line.
- Templates `_modello/business-analyst` 0.1.0 (Vision holder, industry expert where applicable) and
  `_modello/user-persona` 0.1.0 (derived from `analisi-funzionale/utente-simulato`). The AI Coordinator
  creates project instances by filling in only the instance card, without changing rules and limits
  (Do-S04). User Personas run the functional tests as simulated end users, and their progress never depends
  on a person (Do-S03). CI does not select folders starting with `_`; both templates pass the validator
  when run locally.

### Changed

- `controllore/` (AI Coordinator) 0.3.0 → 0.4.0:
  - CR-002: every request of the Human Manager becomes a Change Request, validated against Scope Management
    (Vision, mandate, Principles, Decisions with an explicit re-examination outcome, artifacts and versions,
    open points) before execution, with one outcome: in scope, needs a Do, exception, new project, rejected
    (new §2 bis; `scope.md` added to the project registry);
  - CR-003: its own hard blinding (§1 bis); Context Consistency and Independence when forming Squads and
    groups, the context RACI handed to each agent, hard and soft blinding; Design and planning as a
    dedicated Work Package it does not perform; a new agent with a new context for every Work Package, and
    the Work Package handover abstract required to close it (`abstract/` in the registry);
  - the mandatory Design Thinking session at project start with the Discovery group in independent
    contexts, tracked in the activity tree; its reviewers are the reviewer profiles of the governance domains
    the project touches, chosen by the Coordinator, with security and privacy always present (Do-S09)
    (§3 bis);
  - working alongside the AI Reviewer (§3 ter; `revisore/` in the registry; start-up step 7 and a
    paragraph in `AVVIO.md`);
  - versioning and changelog: releases follow `community/RELEASING.md`, citing their origin, decision
    D-VER-1 of the method project (CR-001) (§3 quater);
  - convergence and guardrails (K1–K2): the Facilitator is activated, when possible, on a model different
    from the explorers'; the independent guardrail check goes to the Discovery reviewers or the AI Reviewer;
  - the header cites The Eiraman Guide 1.0.0-rc.2 alongside the specification 0.3;
  - 7 new qualification cases; new §9, the audit of every point of the profile where context sharing or
    independence applies (CX-01…CX-22), with how each is enforced.
- `analisi-funzionale/facilitatore-design-thinking` 0.1.0 → 0.2.0, **breaking**: the Design Thinking
  Facilitator now leads convergence as well as divergence, under hard blinding. Procedure: the same prompt to
  every executor, answers recorded, reconciliation checked, a new prompt with Principles (immutable
  cornerstones), Decisions (changeable on new specifications or evidence) and Open Points (deferred to
  design, a MOC (mock-up), a POC or a Human Manager Do), iteration to consensus within the mandate's round
  limit, submission to the reviewers. New deliverables: the final report to the Human Manager with each AI's
  initial and final position, and the first draft of Scope Management. New source: the Delphi method. The
  Facilitator should converge on a model different from the explorers' (K1–K2); it applies the guardrails,
  but their independent check belongs to the Discovery reviewers or the AI Reviewer. Raw contributions are
  archived in `docs/scoperta/evidenze/`, linked to the session's Work Package in the activity tree, for the
  Discovery reviewers, the AI Reviewer and the Human Manager; neither members nor the AI Coordinator receive
  them (hard blinding). Tasks T08–T12 added, T07 removed (ID retired); 6
  qualification cases added, case 5 replaced.
- `analisi-funzionale/analista-funzionale` 0.1.0 → 0.2.0, **breaking**: in the Discovery group the
  functional analyst links the needs of the Business Analyst and User Personas to the solutions of UX-UI and
  the architects (Do-S05), under soft blinding with the context RACI; it no longer leads convergence or drafts
  the first Scope Management. Tasks T01 and T02 removed (IDs retired), replaced by T12–T14; case 1 replaced,
  cases 9 and 10 added.
- `analisi-funzionale/utente-simulato` 0.1.0 → 0.2.0: "Human Supervised" means that the end user is simulated
  (Do-S03); progress never waits for a person; when a project has User Persona instances they run the tests;
  independent context and soft blinding. Cases 8 and 9 added.
- `analisi-funzionale/FAMIGLIA.md` 0.1.0 → 0.2.0: phases of the analyst and the facilitator, the linked
  templates, the Discovery group contexts.
- Field `metodo` of the changed and new profiles: "Eiraman 0.3; Guida 1.0.0-rc.2 per le regole di
  contesto". Section references such as "spec §5" still point to the specification 0.3, so the deviation of
  VERSIONING.md §6 is only partly closed.
- `README.md` (families table, total 41, templates, AI Coordinator files, AI Reviewer), `CODEOWNERS`
  (`/governo/` to Test & Quality, flagged as provisional), `REUSE.toml` (comment only: the new paths were
  already covered).

### Removed

Every line removed since v0.1.1 is a replaced rule or a version string (`release_diff.py`, 71 lines: 68 in
profiles, family files and the AI Coordinator profile, 3 in the registry files):

- **Version strings** (version, date, `metodo`): the `Versione` lines of `CONTROLLORE.md`, of
  `analisi-funzionale/FAMIGLIA.md` and of the three changed `PROFILO.md` files; `versione`, `data` and
  `metodo` in the three changed `profilo.json` files.
- `analisi-funzionale/FAMIGLIA.md`: the table rows "Scoperta (convergenza)" and "Scoperta (divergenza)",
  replaced by the new phases.
- `analista-funzionale`, **breaking**:
  - the convergence rules (Discovery bullet, "tu conduci la convergenza", Design Thinking row, the single
    model of convergence, the guardrail check before converging, coordinating explorers, "non conduci la
    convergenza se…"), replaced by the Discovery group link role and the rule that convergence is the
    Facilitator's. The two rules that protected convergence are kept, moved to the new owner: the
    Facilitator should converge on a model different from the explorers' (K1–K2), and the independent
    guardrail check, formerly the analyst's, goes to the Discovery reviewers or the AI Reviewer
    (facilitator profile and Coordinator §3 bis);
  - responsibilities "Sintesi di convergenza" and "Bozza della Visione e prima versione dello Scope
    Management", replaced by the needs–solutions map, the round answers and the functional contribution
    to Scope Management;
  - catalogue tasks T01 and T02 (in `profilo.json` and in the generated table of section 10), replaced by
    T12 and T14;
  - the deliverables list in §6 and the limit "motore diverso per la convergenza", replaced;
  - case 1 replaced; the outcome of case 2 reworded to the needs–solutions map;
  - the Design and planning bullet, reworded to name the dedicated Work Package in shared context;
  - `descrizione_breve`, `descrizione_breve_en` and the `seniority.nota`, reworded to the new role.
- `facilitatore-design-thinking`, **breaking**:
  - the identity bullet ("consegni i contributi all'analista funzionale, che conduce la convergenza"), the
    Double Diamond row ("che non è tua"), the forbidden action "non selezioni… la convergenza è
    dell'analista funzionale" and case 5 "Selezione indebita", replaced by the convergence led by the
    Facilitator;
  - the responsibility "Consegna all'analista funzionale dei contributi grezzi", the §6 line to the
    functional analyst and catalogue task T07 (in `profilo.json` and in the generated table), replaced by
    the archive of the session evidence (T12), which neither members nor the AI Coordinator receive;
  - the empty note of task T05, now stating that the independent guardrail check is not the Facilitator's;
  - the last limit, unchanged in content, now followed by two new limits;
  - `descrizione_breve`, `descrizione_breve_en`, `nome_en` (now "Design Thinking Facilitator", as in the
    glossary) and the note of task T03 (now: never the agent facilitating the same session).
- `utente-simulato`: the line "supervisionato dall'umano", replaced by the "Human Supervised" rule (Do-S03).
- `controllore/CONTROLLORE.md`: in start-up step 2, "avvia la Scoperta (spec §5) e proponi la Visione",
  replaced by the Discovery via the Design Thinking session of §3 bis.
- Registry files: in `README.md`, the "Total: 40 profiles" line and the `CONTROLLORE.md` row, replaced; in
  this file, the `[Unreleased]` link, now comparing from v0.2.0.

### Profile versions

Profiles not listed keep the version of the 0.1.0 table.

| Profile | Version | Date | State |
|---|---|---|---|
| `analisi-funzionale/analista-funzionale` | 0.1.0 → 0.2.0 | 2026-11-26 | draft, not qualified |
| `analisi-funzionale/facilitatore-design-thinking` | 0.1.0 → 0.2.0 | 2026-11-26 | draft, not qualified |
| `analisi-funzionale/utente-simulato` | 0.1.0 → 0.2.0 | 2026-11-26 | draft, not qualified |
| `governo/revisore-ai` | new, 0.1.0 | 2026-11-26 | draft, not qualified |
| `_modello/business-analyst` (template) | new, 0.1.0 | 2026-11-26 | draft, not qualified |
| `_modello/user-persona` (template) | new, 0.1.0 | 2026-11-26 | draft, not qualified |
| `controllore/` (AI Coordinator) | 0.3.0 → 0.4.0 | 2026-11-26 | draft, not qualified |

Family files: `analisi-funzionale/FAMIGLIA.md` 0.1.0 → 0.2.0; `governo/FAMIGLIA.md` new, 0.1.0. The Digital
Seniority map is unchanged (0.1.0).

## [0.1.1] - 2026-11-26

Release files only: no profile, template or Seniority map changes. Every profile keeps the version
in the 0.1.0 table below.

### Added

- This changelog, with the per-profile version table.
- CI workflow `changelog.yml`: a pull request fails if it does not change `CHANGELOG.md`, unless it carries
  the label `no-changelog`.

## [0.1.0] - 2026-11-25

First public release of the registry, published as commits `c9af3d8` and `114f7a2` of
`github.com/eiraman/role-profiles` during the restricted launch of 25 November 2026. It was not tagged.
The tag `v0.1.0` will be applied retroactively to `114f7a2`.

### Added

- 40 Role Profiles in 7 families: Functional analysis 5, AWS 6, Azure 7, Databricks 5, FinOps 5,
  Development 7, Web design 5. Each profile has `PROFILO.md` and `profilo.json`; together they hold 350
  catalogued tasks with a Digital Seniority level. Every profile is a **draft, not qualified**.
- `_modello/`, the template every profile starts from.
- `_seniority/`: the Digital Seniority map `seniority.json` (its own field `versione`: 0.1.0), its
  explanation and the catalogue instructions.
- `controllore/`: the AI Coordinator profile (`CONTROLLORE.md`, `AVVIO.md`, `STATO.md` and the Manager
  View generator `tools/vista_manager.py`), version 0.3.0, published as a draft, not qualified, by
  decision of the Human Manager.
- Licences: CC BY 4.0 for the profile texts, Apache-2.0 for `vista_manager.py`, declared in `REUSE.toml`.
- CI: compliance checks (DCO and AI declaration, REUSE, secrets and deny-list) and the profile
  validator from the `tools` repository, pinned by commit SHA (`TOOLS_REF`, set to `558ddb2` in the
  second commit of this release).

### Changed

- Licence of the profile texts: earlier copies, distributed in the eiraman.tech kit on 25 November 2026,
  were under CC BY-NC-ND 4.0 (scripts under MIT). Those copies keep their original licence; this release
  and later ones are under CC BY 4.0 (code Apache-2.0).

### Profile versions

| Profile | Version | Date | State |
|---|---|---|---|
| `analisi-funzionale/analista-funzionale` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `analisi-funzionale/facilitatore-design-thinking` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `analisi-funzionale/technical-writer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `analisi-funzionale/tester-funzionale` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `analisi-funzionale/utente-simulato` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `aws/aws-architect` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `aws/aws-database-specialist` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `aws/aws-developer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `aws/aws-devops-engineer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `aws/aws-operations` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `aws/aws-security-engineer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `azure/azure-architect` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `azure/azure-cloud-operations` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `azure/azure-dba` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `azure/azure-developer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `azure/azure-incident-manager` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `azure/azure-release-engineer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `azure/azure-security-engineer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `databricks/databricks-analytics-engineer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `databricks/databricks-data-engineer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `databricks/databricks-governance-steward` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `databricks/databricks-ml-engineer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `databricks/databricks-platform-admin` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `finops/finops-cost-allocation-analyst` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `finops/finops-for-ai` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `finops/finops-forecast-budget` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `finops/finops-practitioner` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `finops/finops-rate-optimization` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `sviluppo/dotnet-developer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `sviluppo/go-developer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `sviluppo/java-developer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `sviluppo/python-developer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `sviluppo/shell-iac-developer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `sviluppo/sql-developer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `sviluppo/typescript-developer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `web-design/accessibility-specialist` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `web-design/frontend-developer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `web-design/ux-designer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `web-design/ux-writer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `web-design/web-designer` | 0.1.0 | 2026-11-25 | draft, not qualified |
| `controllore/` (AI Coordinator) | 0.3.0 | 2026-11-25 | draft, not qualified |

Notes on the history before this release, from the project's activity log:

- The 40 profiles were written on 25 November 2026 by seven executor agents, one per family, with
  independent reviews per family; the Digital Seniority catalogue (350 tasks) was added the same day.
  The profiles were never released before, so each starts at 0.1.0.
- The AI Coordinator profile was first written on 24 November 2026 and set to version 0.3.0 on
  25 November 2026, when the roles were renamed to "AI Coordinator" and "Human Manager". The log does not
  record whether versions 0.1.x or 0.2.x of it were ever labelled; none was released on its own.

[Unreleased]: https://github.com/eiraman/role-profiles/compare/v0.2.0...main
[0.2.0]: https://github.com/eiraman/role-profiles/compare/v0.1.1...v0.2.0
[0.1.1]: https://github.com/eiraman/role-profiles/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/eiraman/role-profiles/releases/tag/v0.1.0

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

## [0.7.0] - 2026-11-26

Scope: Change Request CR-011 of the method project. The Discovery session hands the Human Manager one page to
confirm or correct, the **engagement brief** ("scheda di ingaggio"), instead of one question per open point.
Decisions of the Human Manager of 26 November 2026: D-ING-1 (rigid limits set by the AI Coordinator: 5
irreversible choices, 5 high-impact assumptions, 5 reversible decisions shown), D-ING-2 (only the reversible
decisions above an impact threshold are shown), D-ING-3 (released on its own, after 0.6.1), D-ING-4 (the
reserved matters are confirmed as a block with Vision and Principles and do not count in the limit of 5).
Origin: test runs of the method, recorded in the project plan, in which Discovery asked the Human Manager few
questions and none about costs.

Registry bump: MINOR, rules and one task are added; no rule, task or deliverable is removed. Both profiles
stay **draft, not qualified**. The rules are **conventions of the two profiles**, not rules of the Guide. The
Guide 1.0.0-rc.3 stays as it is: the Discovery report with the initial and final position of each AI (§8) is
still produced, and the brief is its opening page; reserved matters go to the Human Manager whatever their
reversibility (§5, E1); silence never approves (§5). The limits and the impact threshold are numbers and
criteria chosen by the AI Coordinator and have not been tested.

A first candidate of this version was rejected by the independent review (REV-ING-01): it let the group
decide reserved matters when reversible and reduce the scope without a confirmation. This entry describes the
rewritten candidate.

### Added

- `analisi-funzionale/facilitatore-design-thinking` 0.3.1 → 0.4.0:
  - three rules for the group, "Scheda di ingaggio": what is delegated is decided, each Decision declaring
    whether it is reversible, with the cost of undoing it, and a missing piece of information becoming a
    declared assumption when the choice is reversible; what is reserved (budget and costs, data, access,
    external services, publication) is proposed for the mandate and never decided; at most 5 irreversible
    choices, and beyond that the group proposes which part of the scope to defer, a proposal that holds only
    if the Human Manager confirms it;
  - what "high impact" means for a reversible Decision or an assumption; door, cost and impact are declared
    by the members and reconciled in the rounds, not assigned by the Facilitator;
  - the format of the brief, which opens the final report: the four opening questions of every text for the
    Human Manager, bad news, the block to confirm (Vision, Principles, proposed values for the mandate), the
    irreversible choices with the agreed option or the positions, at most one alternative, the effect and the
    evidence, the high-impact assumptions, the reversible decisions for information;
  - the register of the decisions of the session, and task T14;
  - the packages for the reviewers and for the judge carry door, cost of undoing and assumptions, so that
    the classification can be checked;
  - one forbidden action (no option of its own, no change of door or impact, no irreversible choice taken
    out), one limit and four cases of the qualification suite.
- AI Coordinator profile 0.5.1 → 0.6.0, §3 bis, "Scheda di ingaggio": three criteria always among the
  convergence criteria; what it adds to the brief (deadline, effect of no answer, its recommendation where
  the group does not agree); delivery with the full report; the block and each irreversible choice are a Do,
  the reversible decisions are delegated and a requested change is a Change Request; confirmed values enter
  the mandate; high-impact assumptions are recorded in Scope Management with their check. Two cases added to
  the qualification suite.

### Changed

- `facilitatore-design-thinking`: the instructions for the explorers and the explorer's contribution also
  carry the proposed decisions with door, cost of undoing and assumptions (T02 and T03 deliverables); the
  final report opens with the engagement brief (T11 deliverable, step 8); the rule "only the gate material,
  no recommendation of selection" is stated for the intermediate gates, where it applied. Section 10 is
  generated again for this profile.

### Profile versions

| Profile | Version | Date | State |
|---|---|---|---|
| AI Coordinator (`controllore/CONTROLLORE.md`) | 0.5.1 → 0.6.0 | 2026-11-26 | draft, not qualified |
| `analisi-funzionale/facilitatore-design-thinking` | 0.3.1 → 0.4.0 | 2026-11-26 | draft, not qualified |

### Known gaps

- The limits and the impact threshold are a judgement of the AI Coordinator, to be calibrated on the test
  bench. "At most one alternative" and "one confirmation for the whole block" were proposed by the AI
  Coordinator and not objected to by the Human Manager; they are not recorded decisions.
- With a rigid limit the group may classify an irreversible choice as reversible. The reviewers and the judge
  receive the classification and check it; their profiles do not change and no tool checks it.
- The profiles of the members of the Discovery group, of the domain reviewers and of the judge do not change:
  they receive the format and the criteria from the Facilitator and the AI Coordinator.
- The Manager View has no dedicated section for the brief: it is a project document, and its confirmations
  appear among the decisions waiting for the Human Manager.
- Making these rules part of the method needs an RFC to the Guide.

## [0.6.1] - 2026-11-26

Scope: Change Request CR-010 of the method project. Corrections from the independent re-review of 0.6.0
(REV-CONS-C), which arrived after 0.6.0 was published. Registry bump: PATCH: the changes restore the intent
stated in the entry 0.6.0 and remove a value that no decision had approved. No task, section or file is added
or removed; section 10 of the profiles does not change.

### Fixed

- `analisi-funzionale/FAMIGLIA.md` 0.3.0 → 0.3.1, `aws/FAMIGLIA.md`, `azure/FAMIGLIA.md` and
  `sviluppo/FAMIGLIA.md` 0.2.0 → 0.2.1: the sentence on the minimum level of independence of the risk class
  (Guide §6, "Independence of verification") is added next to the recommendation of a different model. The
  entry 0.6.0 said it was there; it was only in the AI Coordinator profile and in three profiles.
- AI Coordinator profile 0.5.0 → 0.5.1 and `_seniority/SENIORITY.md`: "(valore indicativo: due)" is removed
  from the rule on promotion. An agent is raised after the failed attempts the mandate allows (Guide §7.1); no
  decision set an indicative number, and the entry 0.6.0 was wrong to give one. The number of attempts is
  added to the items of the mandate (§2): it adds no rule, because the Guide §7.1 already has the mandate
  set it, and the profile until 0.5.0 gave no place where to write it.
- AI Coordinator profile and `analisi-funzionale/facilitatore-design-thinking` 0.3.0 → 0.3.1: the mark
  "convention of the profile" on a negative outcome of the judge covers only how it is reported; that the
  Human Manager approves the Vision or relaunches the exploration is the Guide §8.
- `governo/revisore-ai` 0.2.0 → 0.2.1: in `profilo.json` the source of E6 names the text of the Guide
  1.0.0-rc.3 (RFC 0003), as `PROFILO.md` already did.
- `finops/FAMIGLIA.md` 0.2.0 → 0.2.1: the row "Budget di deriva" of the table of measures follows rule R5
  (spending and time, class changes also as an item of their own).

### Profile versions

| Profile or file | Version | Date | State |
|---|---|---|---|
| AI Coordinator (`controllore/CONTROLLORE.md`) | 0.5.0 → 0.5.1 | 2026-11-26 | draft, not qualified |
| `analisi-funzionale/facilitatore-design-thinking` | 0.3.0 → 0.3.1 | 2026-11-26 | draft, not qualified |
| `governo/revisore-ai` | 0.2.0 → 0.2.1 | 2026-11-26 | draft, not qualified |
| `analisi-funzionale/FAMIGLIA.md` | 0.3.0 → 0.3.1 | 2026-11-26 | draft, not qualified |
| `aws/FAMIGLIA.md`, `azure/FAMIGLIA.md`, `sviluppo/FAMIGLIA.md`, `finops/FAMIGLIA.md` | 0.2.0 → 0.2.1 | 2026-11-26 | draft, not qualified |

### Known gaps

- `governo/revisore-test-qualita` does not apply the sentence that the Guide 1.0.0-rc.3 added to §9.1, "Test
  levels" (security and performance testing is proportionate to the risk; RFC 0003, item 18): the sentence
  carries no key word and the profile has no rule on it.
- The known gaps of 0.6.0 stay open, except that what follows a negative outcome of the judge is the Guide §8
  (the Human Manager approves the Vision or relaunches the exploration); the Guide §12, "Bad news first",
  already asks for rejections and dissent to come first, so the convention of the profiles on reporting a
  negative outcome adds little and may be dropped at qualification.

## [0.6.0] - 2026-11-26

Scope: Change Request CR-010 of the method project (Wave CONS-01), which carries out the Role Profiles part of
CR-009: the registry is aligned to **The Eiraman Guide 1.0.0-rc.3**, published on 26 November 2026, which
implements RFC 0003 (decisions D0 to D10 of the Human Manager on the critical review of specification 0.3,
Do-S19, Do-S20). Each change below names the item of RFC 0003 it comes from. By decision D0 the corrections go
into the Guide and the artifacts that follow it; specification 0.3 stays the historical source and is not
changed.

Starting state: this release starts from 0.5.1 (commit `7990451`), which follows 0.5.0 (commit `eaa6cd0`).
Neither was published when this entry was written; the three releases are separate candidates on the same
branch.

Registry bump: MINOR, marked **breaking** (VERSIONING §2.2, §2.6). Rules are removed or replaced in the AI
Coordinator profile, in seven profiles and in four family files, and the change to `_seniority/seniority.json`
makes every profile of the earlier releases fail the validator until its section 10 is generated again; this
release generates it again for all of them. Every profile, template and family file stays **draft, not
qualified**; no qualification is part of this release.

Tools: section 10 of every profile is generated by `attiva_profilo.py` of tools 0.3.0, which reads the new
fields of the map. `TOOLS_REF` in `validate-profiles.yml` moves from `558ddb2` (the initial import, tagged
v0.1.0) to `4901fcf7c946e5f1b15dc8e6a069519df5ce71b2` (tools 0.3.0, a local candidate, not yet tagged). The
tools of 0.2.3 and earlier reject this registry, because their generated text differs. **Order of
publication:** tools 0.3.0 must be published before this release, otherwise the validation workflow cannot
check out the pinned commit and fails.

### Changed, breaking

- **AI Coordinator profile** (`controllore/CONTROLLORE.md`) 0.4.2 → 0.5.0.
  - Precedence (§1): on the rules that the Guide 1.0.0-rc.3 added or changed, listed in §1, the profile
    prevails over specification 0.3. Until 0.4.2 the specification prevailed in every conflict (decision D0).
  - Fallback (§3; RFC 0003 items 10 and 12; D4): a task outside the catalogue runs at the fallback level the
    mandate sets, indicative value SD3, and is raised at the first failure for lack of capability; tasks that
    by nature belong to the Lead level (architecture, security, effects hard to undo) start at SD4, an
    indicative value too. The rule "a task outside the catalogue runs at SD4" is removed.
  - Different model for security and personal data (§3, CX-05; PA-6, Guide §6): a recommendation, with the
    level of independence recorded in every case. The obligation is removed. The minimum level of independence
    that the risk class of the Work Package sets stays an obligation (Guide §6, "Independence of
    verification").
  - Tester (§3; item 1; D3): the tester fixes nothing on its own; the AI Coordinator assigns every fix, and
    the fix of the test script is a task of its own that the same tester may receive.
  - Manager View (§5 bis; correction R12): the progress of a package in progress is "mandatory checks passed
    over the total". The completion percentage is removed.
  - Precedence list (§1): it also names promotion at the first failure, the gates of Discovery, progress as
    checks passed over the total and the measures of escalation as estimates.
- **Digital Seniority map** (`_seniority/seniority.json`) 0.1.0 → 0.2.0 (items 9 and 10; D4, D5).
  - `fallback` is `SD3`, with the new fields `fallback_indicativo` (true), `fallback_eccezione` (SD4 for
    architecture, security, effects hard to undo) and `fallback_nota`.
  - The sentence "È anche il livello di ripiego per ogni compito fuori catalogo" is removed from the
    description of SD4.
  - `nota` says that the correspondence between levels and configurations is an assessment by the maintainers
    of the map, and defines "tested"; every configuration gains `"provata": false`, because the registry holds
    no recorded test of any of them. The reference to "spec §9" is replaced by the Guide §7.1.
  - `SENIORITY.md` and `ISTRUZIONI-CATALOGO.md` follow: rule 2 (fallback), rule 5 (promotion at the first
    failure for a task outside the catalogue; "unchanged quality" defined), the SD4 row and the sentence the
    authors add to section 1.
- **`analisi-funzionale/tester-funzionale`** 0.1.0 → 0.2.0 (item 1; D3). The permission to fix gross errors of
  its own test script on its own is removed and reversed: the tester reports every error to the AI
  Coordinator, which assigns the fix. Fixing the test script is the new task T10, never started on its own.
  T07 no longer promises "a different model from the executor": it delivers the outcome with the level of
  independence achieved, and the different model is a recommendation (PA-6). Case 7 changes accordingly; cases
  9 and 10 are new; T05 note, sections 2 to 7 and the sources follow.
- **`governo/revisore-architettura-applicativa-dati`** 0.1.0 → 0.2.0 (items 2 and 19; D10, D6). The order of
  construction is the one of the Guide §10: first a minimal usable path through Backbone, Brain and essential
  interfaces, then the Backbone completed over all the main paths before the other components are extended;
  "Backbone before all other components" is replaced. New rule and task T10: the reviewer checks the
  trusted/untrusted classification of Brain tasks against the criteria of the mandate and the role the mandate
  names, and opens an open point when the mandate sets neither. T05 deliverable, case 5 and the sources
  follow; cases 11 and 12 are new.
- **`aws/aws-developer`** and **`azure/azure-developer`** 0.1.0 → 0.2.0 (item 2; D10): the row "Architettura
  componibile" gives the same order of construction; "nell'ordine Backbone, Brain, interfacce, Hairs" and
  "Prima Backbone e Brain, poi interfacce essenziali" are replaced.
- **`analisi-funzionale/facilitatore-design-thinking`** 0.2.0 → 0.3.0 (item 13): the Facilitator no longer
  sets the gates of the Human Manager; the AI Coordinator sets and communicates them and the Facilitator
  applies them. The other changes of this profile are under "Changed".
- **Different model as a recommendation** (PA-6; Guide §6, "Security and personal data"), in the files that
  still stated it as an obligation: family files `analisi-funzionale/FAMIGLIA.md` 0.2.0 → 0.3.0,
  `aws/FAMIGLIA.md`, `azure/FAMIGLIA.md` and `sviluppo/FAMIGLIA.md` 0.1.0 → 0.2.0; profiles
  `aws/aws-security-engineer` and `azure/azure-security-engineer` 0.1.0 → 0.2.0. In `aws-security-engineer` the
  limit "the package stays open when no reviewer on a different model is available" is replaced by a report to
  the AI Coordinator; in `azure-security-engineer` case 6 changes. The level of independence achieved is
  recorded in every case, and the package stays open below the minimum level of its risk class (Guide §6,
  "Independence of verification"). The different model stays mandatory for the checks of the process reviewer
  (`governo/FAMIGLIA.md` §A, `governo/revisore-ai`), which this release does not change.

### Changed

- **AI Coordinator profile**, additions (0.5.0):
  - mandate (§2): fallback level, criteria by which a Brain task is trusted or untrusted and the role that
    applies them, the K6 values (type of package, minimum number of packages, minimum margin), threshold of
    the drift budget in spending and in time (items 19, 7 and 5);
  - Discovery (§2, §3 bis): the AI Coordinator sets and communicates the gates at the start; convergence
    criteria are fixed before divergence; after the domain reviewers a K1 judge, distinct from them and from
    the Facilitator, under hard blinding and on a model different from those of all the members of the group,
    assesses the result against those criteria; when no such model is available the choice goes to the Human
    Manager as a Do in functional and economic terms (items 13 and 14; D2). New row CX-23; hard blinding
    covers the judge;
  - cycle review (§5): governance share and share of tasks run outside the catalogue; drift budget in
    spending and in time with class changes as an item of their own; business risks (items 15, 10 and 5);
  - run records (§3, §6): each run records the role of the agent, governance or production (item 20);
  - documents due per level (§5): at level 0 they include the High Level Architectural View and the progress
    dashboard (item 22; D7);
  - Do (§4, §5 bis): changes that add an external service or move data outside the organisation (item 4);
  - Digital Seniority (§3): tasks of different levels may go to different agents; "unchanged quality" defined;
    the map is the maintainers' assessment and an untested configuration is recorded in the run (items 9, 11
    and 12); Retrospective paragraph (item 8); K6 uses the values of the mandate;
  - AI Reviewer (§3 ter): under-escalation and over-escalation are reported as estimates (item 6);
  - promotion for a task of the catalogue: after the failed attempts the mandate allows, indicative value two
    (it said "after two"); the mandate also sets the confidence level of E6;
  - conventions of the profile, marked as such because the Guide is silent: who proposes and who confirms the
    convergence criteria, the judge distinct from the Facilitator, what follows a negative outcome of the
    judge, the confidence level of E6 among the items of the mandate;
  - qualification suite (§8): seven cases added.
- `controllore/STATO.md`: `controlli` (`superati`, `totale`) replaces `percentuale` for a package in progress;
  `ciclo.quota_governo` and `ciclo.fuori_catalogo` are new. `percentuale` is no longer shown, because it
  declares no denominator (Guide §12, "Percentages").
- `controllore/tools/vista_manager.py`: a package in progress shows "4/10" from `controlli`, and "?" with
  the words "progress not declared" when `controlli` is missing, also when the old `percentuale` is given; the budget card shows the governance share and the share of
  tasks outside the catalogue with numerator and denominator, or "sconosciuta" when the field is missing; the
  legend changes in Italian and English.
- **`analisi-funzionale/facilitatore-design-thinking`** 0.2.0 → 0.3.0 (item 14; D2), besides the breaking
  change above: the convergence criteria are fixed and recorded before the first round and
  do not change afterwards; new step 7 of the convergence procedure, the K1 judge after the reviewers; the
  Facilitator prepares the package for the judge (new task T13), is never the judge and reports the judge's
  outcome unchanged; two limits and cases 14 and 15 are new. Convention of the profile, marked as such: the
  Facilitator proposes the criteria and the AI Coordinator confirms them, because the Guide does not say who
  fixes them.
- **`governo/revisore-ai`** 0.1.0 → 0.2.0 (item 6; D1): under-escalation and over-escalation are estimates,
  reported with the number of decisions examined and the confidence interval; a threshold is met only if the
  unfavourable bound stays within it. T06 deliverable and one case follow. Convention of the profile: the
  confidence level is the one of the mandate, otherwise an open point.
- **`governo/revisore-test-qualita`** 0.1.0 → 0.2.0 (item 1; D3): a Decision that lets the agent of scripted
  functional tests fix the candidate or its own script on its own is "Non conforme"; one case added.
- **`finops/finops-forecast-budget`** and **`finops/finops-practitioner`** 0.1.0 → 0.2.0, and
  `finops/FAMIGLIA.md` 0.1.0 → 0.2.0 (items 5 and 15): the drift budget is expressed in spending and in time
  and reports class changes also as an item of their own; the cycle review contains the governance share and
  the share of tasks run outside the catalogue. The way of adding up the deviations (absolute values, no
  compensation) stays a convention of the profile, which the Guide does not fix. T03 deliverable of
  `finops-forecast-budget` follows.
- `analisi-funzionale/scrum-master-ai` cites the AI Coordinator profile 0.5.0.
- **Every other profile and the two templates** (39 folders), MINOR: the line of section 1 on tasks outside
  the catalogue refers to the fallback level of the mandate; section 10 is generated again from map 0.2.0, with
  the indicative fallback and the row of the exception; the `Metodo` line and the field `metodo` name the Guide
  1.0.0-rc.3; the date is 2026-11-26. In the seven `sviluppo/` profiles the field `seniority.nota` follows.
- References to "Guida 1.0.0-rc.2" become "Guida 1.0.0-rc.3" in the profiles, where they cite the Guide as the
  text in force for the profile; RFC 0003 changes no section number and removes no paragraph label. Left as
  they are, because they record when a rule was introduced: "Dalla Guida 1.0.0-rc.2 …" in
  `analista-funzionale` and `facilitatore-design-thinking`, the source lines "1.0.0-rc.1 …; 1.0.0-rc.2 (RFC
  0001) …" in `utente-simulato` and in the two templates, and the references to "Guida 1.0.0-rc.1, §4".
- `governo/FAMIGLIA.md` 0.2.2 → 0.2.3, PATCH: only the `Metodo` line changes. §A–§D are not touched, references
  included, because a change to §A–§C needs the lazy consensus of the six domain groups (0.5.1).
- CI, `validate-profiles.yml`: `TOOLS_REF` pins tools 0.3.0.

### Removed

Rules and sentences removed, each replaced as described above: the fallback at SD4 (AI Coordinator §3, map,
`SENIORITY.md`, section 1 and section 10 of every profile); the tester's permission to fix gross errors of its
script; the order "Backbone first" in three profiles; the obligation of a different model for security and
personal data in the AI Coordinator profile, four family files and three profiles; the Facilitator's task of
setting the gates; the completion percentage in the Manager View; the field `percentuale` in the example of
`STATO.md` and its display. No profile, task ID, section or
file is removed.

### Profile versions

| Profile | Version | Change |
|---|---|---|
| AI Coordinator (`controllore/CONTROLLORE.md`) | 0.4.2 → 0.5.0 | **breaking** |
| Digital Seniority map (`_seniority/seniority.json`) | 0.1.0 → 0.2.0 | **breaking** |
| `_modello/business-analyst` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `_modello/user-persona` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `analisi-funzionale/analista-funzionale` | 0.2.0 → 0.3.0 | MINOR: fallback |
| `analisi-funzionale/facilitatore-design-thinking` | 0.2.0 → 0.3.0 | **breaking**: gates set by the AI Coordinator; convergence criteria, judge step |
| `analisi-funzionale/scrum-master-ai` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `analisi-funzionale/technical-writer` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `analisi-funzionale/tester-funzionale` | 0.1.0 → 0.2.0 | **breaking**: the tester fixes nothing on its own; different model as a recommendation |
| `analisi-funzionale/utente-simulato` | 0.2.0 → 0.3.0 | MINOR: fallback |
| `aws/aws-architect` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `aws/aws-database-specialist` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `aws/aws-developer` | 0.1.0 → 0.2.0 | **breaking**: order of construction replaced |
| `aws/aws-devops-engineer` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `aws/aws-operations` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `aws/aws-security-engineer` | 0.1.0 → 0.2.0 | **breaking**: different model as a recommendation |
| `azure/azure-architect` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `azure/azure-cloud-operations` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `azure/azure-dba` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `azure/azure-developer` | 0.1.0 → 0.2.0 | **breaking**: order of construction replaced |
| `azure/azure-incident-manager` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `azure/azure-release-engineer` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `azure/azure-security-engineer` | 0.1.0 → 0.2.0 | **breaking**: different model as a recommendation |
| `databricks/databricks-analytics-engineer` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `databricks/databricks-data-engineer` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `databricks/databricks-governance-steward` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `databricks/databricks-ml-engineer` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `databricks/databricks-platform-admin` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `finops/finops-cost-allocation-analyst` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `finops/finops-for-ai` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `finops/finops-forecast-budget` | 0.1.0 → 0.2.0 | MINOR: drift budget, cycle review |
| `finops/finops-practitioner` | 0.1.0 → 0.2.0 | MINOR: cycle review |
| `finops/finops-rate-optimization` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `governo/revisore-ai` | 0.1.0 → 0.2.0 | MINOR: E6 as an estimate |
| `governo/revisore-architettura-applicativa-dati` | 0.1.0 → 0.2.0 | **breaking**: order of construction replaced; trusted/untrusted check |
| `governo/revisore-architettura-cloud` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `governo/revisore-legale-compliance` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `governo/revisore-privacy` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `governo/revisore-sicurezza` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `governo/revisore-test-qualita` | 0.1.0 → 0.2.0 | MINOR: test agent fixes nothing on its own |
| `sviluppo/dotnet-developer` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `sviluppo/go-developer` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `sviluppo/java-developer` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `sviluppo/python-developer` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `sviluppo/shell-iac-developer` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `sviluppo/sql-developer` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `sviluppo/typescript-developer` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `web-design/accessibility-specialist` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `web-design/frontend-developer` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `web-design/ux-designer` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `web-design/ux-writer` | 0.1.0 → 0.2.0 | MINOR: fallback |
| `web-design/web-designer` | 0.1.0 → 0.2.0 | MINOR: fallback |

Family files: `analisi-funzionale/FAMIGLIA.md` 0.2.0 → 0.3.0, `aws/FAMIGLIA.md`, `azure/FAMIGLIA.md` and
`sviluppo/FAMIGLIA.md` 0.1.0 → 0.2.0 (**breaking**, different model as a recommendation);
`finops/FAMIGLIA.md` 0.1.0 → 0.2.0 (MINOR, drift budget); `governo/FAMIGLIA.md` 0.2.2 → 0.2.3 (PATCH).
`databricks/` and `web-design/FAMIGLIA.md` are unchanged. All entries: 2026-11-26, draft, not qualified.

### Known gaps

- The developer profiles of `sviluppo/`, `aws-developer`, `azure-developer` and `frontend-developer` keep the
  correction of gross errors of their own work and of their own unit tests: RFC 0003 keeps the ordinary
  two-way-door autonomy of executors on their own work, and the new rule covers the agent that runs scripted
  functional tests. The Guide does not say whether it also covers the unit tester.
- The notes of some catalogue tasks still say "revisione con modello diverso (P6)": they explain the level
  of the task and are read as the recommendation of the Guide §6.
- The Guide does not say who fixes the convergence criteria, whether the judge must be distinct from the
  Facilitator, what follows a negative outcome of the judge, or who sets the confidence level of E6: the
  profiles state a convention, marked as such.
- `governo/FAMIGLIA.md` §A still says that for the domain reviewers "vale anche un modello diverso" when the
  material touches security or personal data, citing the Guide 1.0.0-rc.2 §6: it is read as the
  recommendation of that paragraph, which rc.3 does not change. The sentence is not reworded here, because a
  change to §A needs the lazy consensus of the six domain groups.
- The time part of the drift budget has no source in the FinOps profiles other than the plan of the AI
  Coordinator; how deviations in time are added up is not defined.
- Specification 0.3, shipped in the kit as `framework/Eiraman.md`, still states the replaced rules; the AI
  Coordinator profile says which of its rules prevail. The kit does not contain the Guide.
- The notes of the independent review of 0.5.0 on `scrum-master-ai` are not applied here; the profile changes
  only as every other profile does. `analisi-funzionale/FAMIGLIA.md` still does not list it.
- The format of the run records has no schema or validator: the role label is a rule of the AI Coordinator
  profile, checked by no tool.
- The `tools` registry baseline follows this release in tools 0.3.1; the site and the kit in a later release.

## [0.5.1] - 2026-11-26

Scope: Change Request CR-007 of the method project, implementing RFC 0002 (`guide/rfcs/0002-governo-family.md`),
alternative B, decided by Do-S18: the working group **Governance & Assurance** owns the family `governo/`,
and the domain groups co-review the reviewer profile of their own domain. The change was prepared on v0.4.1 as
0.4.2 (Wave GOV-01) and is released here on top of 0.5.0, with the same content (Change Request CR-010, decision
D-CONS-1). Registry bump: PATCH (ownership,
documentation and CI only; no rule, limit or task of any profile changes). Every profile stays **draft, not
qualified**.

### Changed

- `CODEOWNERS`: `/governo/` lists `@eiraman/wg-governance-assurance` and `@eiraman/test-quality`; each
  `/governo/revisore-<domain>/` lists `@eiraman/wg-governance-assurance` and the team of its domain. The FLAG
  on `governo/` is replaced by "owned by Governance & Assurance (RFC 0002); revisore-ai and FAMIGLIA
  published by Test & Quality, provisionally", and the header comment no longer says that every folder lists
  only the domain team.
- `README.md`: the families table names Governance & Assurance (RFC 0002) for `governo/`.
- `governo/FAMIGLIA.md` 0.2.1 → 0.2.2: a header paragraph on ownership and review (Governance & Assurance
  authors and maintains and never publishes; each `revisore-<domain>` is co-reviewed and published by the
  reviewers of record of its domain; `revisore-ai` and the family file by Test & Quality, provisionally;
  changes to §A–§C also need lazy consensus of the six domain groups). Rules §A–§D unchanged.

### Added

- CI, `governo-coreview.yml`: on pull requests that change `governo/`, the check passes only if a member of
  the required team approved the current head commit: the domain team for `governo/revisore-<domain>/`, and
  Test & Quality for `governo/revisore-ai/`, `governo/FAMIGLIA.md` and any other family file. Approvals by the
  author or on an earlier commit do not count; an unknown `revisore-*` folder fails. The check reads only the
  GitHub API and never runs the pull request's code. It needs the organisation secret `EIRAMAN_TEAMS_TOKEN`
  (read access to team membership) and must be set as a required status check; until both are set by the
  organisation, it fails or only reports, and the co-review is not enforced (open point).

### Profile versions

| Profile or file | Version | Date | State |
|---|---|---|---|
| `governo/FAMIGLIA.md` | 0.2.1 → 0.2.2 | 2026-11-26 | draft, not qualified |

No profile, template or the AI Coordinator profile changes.

## [0.5.0] - 2026-11-26

Scope: Change Request CR-008 of the method project, Wave SM-01. The Guide requires one AI Scrum Master per
team (Guide 1.0.0-rc.2, §7, "One AI Scrum Master per team") and the registry had no profile for the role; the
Human Manager decided to keep the rule and have the missing profile written (decision D8, alternative C, on
the review findings on specification 0.3). Registry bump: MINOR (one new profile). No rule is reversed and no
task is removed. No other profile, family file or tool changes. The profile is **draft, not qualified**.

### Added

- `analisi-funzionale/scrum-master-ai`, the **AI Scrum Master**, 0.1.0, in the structure of `_modello/`:
  - purpose: it coordinates the agents of one team in the shared context of one Work Package, keeps the Log
    Tracker of the package and delivers to the AI Coordinator the activity report, on the template the AI
    Coordinator specifies, and the team's Work Package handover abstract;
  - limits of the role: it takes no technical decisions, which belong to the agent that is R in the context
    RACI, and it neither validates nor closes the package, which belongs to the AI Coordinator (Guide §7,
    "The AI Coordinator as Scrum of Scrums"; §9, "Definition of done"); it reports dependencies between
    teams and does not resolve them;
  - context rules: shared context of the team under soft blinding; a new agent for every Work Package; it
    does not receive the tester's discussion and does not hand the team's discussion to the tester; it is not
    part of the Discovery group; with competing teams it sees only its own;
  - sources: Guide 1.0.0-rc.2 §2, §3, §4, §5, §7, §8, §8.1, §9, §11, §12; the Scrum Guide of November 2020
    (sections Scrum Theory; Scrum Team, Scrum Master; Daily Scrum; Sprint Retrospective), cited only and
    adapted as the Guide §7 prescribes, section names checked on scrumguides.org by the independent review; specification 0.3 §2, §4 bis, §8; the AI Coordinator
    profile 0.4.2 §3, §3 bis, §6;
  - catalogue: 9 tasks (SD2–SD4): start-up check, team work plan, coordination, Log Tracker, reporting of
    blocks, dependencies and dissent, completeness check of the delivery, activity report, handover abstract,
    contribution to the Design and planning Work Package;
  - qualification suite: 16 known-answer cases, including two out-of-role cases (a technical decision; closing
    the package), a hostile instruction in the data, which ends in a recorded Deny, and two
    missing-information cases (no report template; a context part with no R);
  - conventions of the profile, marked as such and to be confirmed at qualification: technical decisions
    inside the team belong to the agent that is R, while the Guide §4 gives them to the specialist AI roles as
    a whole; the AI Scrum Master receives only outcomes and evidence from the tester; the team work plan; the
    proposal of team composition in Design and planning.
- Placement: the profile is in the existing family `analisi-funzionale/` as a **provisional placement**
  (decision D-SM-1 of the method project, to be confirmed by the Human Manager at release). The family
  `governo/` requires independent context and hard blinding, the opposite of this role; a new family requires
  an RFC (WORKING-GROUPS.md §3).

### Changed

- `README.md`: Functional analysis family 6 profiles, total 48. `CODEOWNERS` and `REUSE.toml` are unchanged:
  the new folder is covered by the existing `/analisi-funzionale/` rule and by the existing patterns.

### Removed

Lines removed since v0.4.1: the Functional analysis row and the "Total: 47 profiles" line of `README.md`,
replaced (6 and 48); in this file, the `[Unreleased]` link, now comparing from v0.5.0.

### Profile versions

Profiles not listed keep the version of the latest table in which they appear.

| Profile | Version | Date | State |
|---|---|---|---|
| `analisi-funzionale/scrum-master-ai` | new, 0.1.0 | 2026-11-26 | draft, not qualified |

Family files and the Digital Seniority map (0.1.0) are unchanged.

### Known gaps

- `analisi-funzionale/FAMIGLIA.md` (0.2.0) does not list the new profile in its table, and the AI Coordinator
  profile (0.4.2) does not refer to it: both changes are proposed for a later release. The profile states
  how it applies the family rules, which prevail over it.
- WORKING-GROUPS.md §3 does not name the AI Scrum Master in the scope of the Functional Analysis group.
- The form of the team Log Tracker, the write paths and the minimum content of the activity report are
  conventions of the profile; no qualified template of the activity report exists yet. The default path
  `eiraman/squadre/` is not in the project registry of the AI Coordinator profile (§6).
- Task T03, coordination, is catalogued at SD3, while the Digital Seniority map 0.1.0 names coordination among
  the uses of SD4: the level is to be calibrated at qualification.
- The Guide §8.1 names the AI Scrum Master in Design and planning and in Scale only; the suite does not cover
  teams formed in other phases.
- The `tools` registry baseline (`tools` v0.2.3, 47 profiles) does not include the new profile; the registry
  now has 48. It is updated in a later `tools` release, with the site and the kit.
- The profile's fallback level for tasks outside the catalogue is SD4, as in the Digital Seniority map 0.1.0.

## [0.4.1] - 2026-11-26

Scope: Change Request CR-005 of the method project.

### Fixed

- CI, `compliance.yml`: the local-path check flagged the official ISO URL
  `https://committee.iso.org/sites/jtc1sc7/home/...` cited by `governo/revisore-test-qualita`, so the
  workflow failed on v0.4.0. The check now removes http(s) URLs from the matched lines before
  matching again, so a path segment inside a URL is not flagged; every other form of local path caught before
  (plain text, quotes, `file://` URLs, PATH values, linker flags, Windows paths) is still caught. No profile changed.

## [0.4.0] - 2026-11-26

Scope: second part of Change Request CR-004 of the method project, Wave REV-02 (Do-S12), with the rules of
the `governo/` family as extended by Do-S14. Registry bump: MINOR (four new profiles). No rule is reversed and
no task is removed. Every profile stays **draft, not qualified**.

### Added

- Four AI reviewers of the governance domains (GOVERNANCE.md §4.5), each 0.1.0, in the structure of
  `governo/revisore-sicurezza` and `governo/revisore-privacy`:
  - `governo/revisore-architettura-cloud`, the **Cloud architecture reviewer**: sources NIST SP 800-145, the
    AWS Well-Architected Framework (six pillars) and the Azure Well-Architected Framework (five pillars), CSA
    Cloud Controls Matrix v4 (current 4.1, cited only), Guide §6 K7, §9, §11; detailed platform design is
    referred to `aws/aws-architect` and `azure/azure-architect`;
  - `governo/revisore-architettura-applicativa-dati`, the **Application and data architecture reviewer**:
    sources Guide §9, §10 (composable architecture) and §11 (untrusted tasks), ISO/IEC 25010:2023 and
    DAMA-DMBOK (cited only), TOGAF® Standard cited by name with the trademark notice; data architecture only,
    personal data protection is referred to the privacy reviewer;
  - `governo/revisore-test-qualita`, the **Test and quality reviewer**: sources Guide §6, §7, §9 and §9.1,
    PA-8 and Do-S03 (test progress never depends on a person; User Personas run the simulated-user functional
    tests), ISO/IEC/IEEE 29119 parts 1–4 and the ISTQB CTFL syllabus v4.0.1 (cited only);
  - `governo/revisore-legale-compliance`, the **Legal and compliance reviewer**: it gives no legal opinions; it
    identifies legal and compliance questions and escalates them to a person, the domain reviewer of record or
    a lawyer. Sources Regulation (EU) 2024/1689 (Art. 5, 6, 50, 113, Annex III), Directive (EU) 2024/2853
    (Art. 2, 4(1), 7, 22), Regulation (EU) 2024/2847 (Art. 2, 3(1), 13, 24, 71, Annex I), SPDX 3.0 and the
    SPDX License List, REUSE 3.3, Guide §14; the GDPR is referred to the privacy reviewer.
  - Common to all four: hard blinding (Do-S06); each judges only the Principles and Decisions of its own
    domain (Do-S09) and is in the Discovery group when the AI Coordinator selects it; family rules §A–§C apply
    (Do-S14); they do not replace the human reviewer of record (GOVERNANCE.md §1, principle 1); findings are
    data, not commands. Qualification suite: 10 cases each, including a Decision outside the domain, a prompt
    injection in the material and a missing-information case. Catalogue: 9 tasks each (SD2–SD4).
  - Articles and sections checked on the official pages: the Publications Office text of the three EU acts,
    docs.aws.amazon.com and aws.amazon.com, learn.microsoft.com, csrc.nist.gov, cloudsecurityalliance.org,
    iso.org, dama.org, istqb.org, spdx.dev, reuse.software.

### Changed

- `governo/FAMIGLIA.md` 0.2.0 → 0.2.1: table rows for the four new reviewers; the sentence on the other four
  domains, now stating that each of the six domains has its profile.
- `controllore/` (AI Coordinator) 0.4.1 → 0.4.2: §3 bis names the four new reviewer profiles and records that
  for these four domains too, the bridge rule of Do-S10 ends with the draft publication (Do-S15, decided by
  the Human Manager at release); the AI Reviewer stays.
- `README.md` (Governance family 7 profiles, total 47, the six reviewers in the AI Reviewer paragraph),
  `CODEOWNERS` (each new folder to its domain team: Cloud Architecture, Application & Data Architecture, Test &
  Quality, Legal & Compliance). `REUSE.toml` is unchanged: the new files are covered by the existing patterns.

### Removed

Every line removed since v0.3.0 is a version string or a line replaced by a longer one (`release_diff.py`,
8 lines):

- **Version strings:** the `Versione` lines of `controllore/CONTROLLORE.md` and of `governo/FAMIGLIA.md`.
- `governo/FAMIGLIA.md`: the paragraph on the domain reviewers, whose last sentence ("Gli altri quattro domini
  avranno i loro profili in una Wave successiva") is replaced by the six-domain sentence.
- `README.md`: the Governance row and the "Total: 43 profiles" line, replaced (7 and 47); the two lines naming
  the security and privacy reviewers, now naming all six.
- This file: the `[Unreleased]` link, now comparing from v0.4.0.

### Profile versions

Profiles not listed keep the version of the latest table in which they appear.

| Profile | Version | Date | State |
|---|---|---|---|
| `governo/revisore-architettura-cloud` | new, 0.1.0 | 2026-11-26 | draft, not qualified |
| `governo/revisore-architettura-applicativa-dati` | new, 0.1.0 | 2026-11-26 | draft, not qualified |
| `governo/revisore-test-qualita` | new, 0.1.0 | 2026-11-26 | draft, not qualified |
| `governo/revisore-legale-compliance` | new, 0.1.0 | 2026-11-26 | draft, not qualified |
| `controllore/` (AI Coordinator) | 0.4.1 → 0.4.2 | 2026-11-26 | draft, not qualified |

Family files: `governo/FAMIGLIA.md` 0.2.0 → 0.2.1. The Digital Seniority map is unchanged (0.1.0).

### Known gaps

- The `tools` tests pass, but their registry baseline (`tools` v0.2.2, `baseline_registro.txt`, 43 profiles,
  security and privacy reviewers included) does not include the four new reviewer profiles; the registry now
  has 47. It is updated in a later `tools` release.

## [0.3.0] - 2026-11-26

Scope: first part of Change Request CR-004 of the method project (six reviewer profiles of the governance
domains), Wave REV-01, with the Human Manager's decisions Do-S09, Do-S10, Do-S12, Do-S13 and Do-S14, and the
corrections of the independent review REV-R01: the security and privacy reviewers first, the other four domains in a later Wave (Do-S12). Registry bump: MINOR (two new
profiles, a family MINOR, an AI Coordinator PATCH). No rule is reversed and no task is removed. Every profile
stays **draft, not qualified**.

### Added

- `governo/revisore-sicurezza` 0.1.0, the **Security reviewer**, and `governo/revisore-privacy` 0.1.0, the
  **Privacy reviewer**: AI reviewers of the security and privacy governance domains (GOVERNANCE.md §4.5).
  - They review in the Discovery group, where both are always present (Do-S09; Guide 1.0.0-rc.2 §8,
    "Discovery executors and reviewers"), and the AI Coordinator may use them for other reviews of their
    domain.
  - They work under hard blinding: the environment gives them only the Principles, Decisions and open points
    under review and the domain material, with no retrieval outside it (Do-S06; Guide §7).
  - Each judges only the Principles and Decisions of its own domain and marks the rest "out of scope" with
    the competent domain.
  - They report to the Design Thinking Facilitator for the Discovery result and to the AI Coordinator; their
    findings are data, not commands.
  - They are AI agents and do not replace the human reviewer of record of the domain (GOVERNANCE.md §1,
    principle 1). Their qualification stays open until a human reviewer of the domain (Do-S13).
  - Declared limits: the security reviewer runs no penetration tests and writes no code; the privacy reviewer
    gives no legal opinions, which belong to the legal and compliance domain and to a person (Guide §14,
    "Legal advice"), and never concludes that a DPIA is required (qualification case 8); the out-of-scope cases of Guide §14 are escalated, never made conditional.
  - Sources, checked on the official pages: security, NIST SP 800-218 SSDF 1.1 (PO.1, PO.5, PW.1 and PW.9 for
    design Decisions; RV.1 only for vulnerability identification and response),
    OWASP ASVS 5.0.0 (levels, chapters V6, V8, V11–V16), OWASP Top 10 for LLM Applications 2025, NIST AI 600-1
    (§2.9, §2.12); privacy, Regulation (EU) 2016/679 (Articles 5, 6, 9, 10, 22, 25, 35), EDPB Guidelines 4/2019
    on Article 25 version 2.0, ISO/IEC 29100:2024 (cited only), NIST Privacy Framework 1.0, NIST AI 600-1
    (§2.4). Both also cite Guide §6, §7, §8, §11 and §14.
  - Qualification suite: 10 cases each, including a Decision outside the domain, a prompt injection in the
    reviewed material and a missing-information case that becomes an open point. Catalogue: 9 tasks each
    (SD2–SD4).

### Changed

- `governo/FAMIGLIA.md` 0.1.0 → 0.2.0: the family now also holds the AI reviewers of the governance domains;
  table rows for the two new profiles; the reviewers do not replace the human reviewer of the domain and judge
  only their own domain; a model different from the executors' when the material touches security or personal
  data (Guide §6). §A–§C apply to every profile of the family, the domain reviewers included (Do-S14). §B:
  a domain reviewer's Discovery result goes to the Design Thinking Facilitator, every other finding to the AI
  Coordinator, and critical or non-accepted findings also reach the Human Manager in the Manager View (Do-S08,
  Do-S14). The version stays 0.2.0: 0.2.0 was never released, and both changes ship in this release.
- `controllore/` (AI Coordinator) 0.4.0 → 0.4.1: §3 bis names the profiles `governo/revisore-sicurezza` and
  `governo/revisore-privacy` for the Discovery reviewers and records Do-S13: for security and privacy the
  bridge rule of Do-S10 ends with the draft publication of the profiles, the AI Reviewer stays, and their
  qualification stays open until a human reviewer of the domain.
- `README.md` (Governance family 3 profiles, total 43, the two reviewers in the AI Reviewer paragraph),
  `CODEOWNERS` (`/governo/revisore-sicurezza/` to Security, `/governo/revisore-privacy/` to Privacy).
  `REUSE.toml` is unchanged: the new files are covered by the existing `**/PROFILO.md` and `**/profilo.json`
  patterns.
- `analisi-funzionale/facilitatore-design-thinking` is unchanged: it names the Discovery reviewers by domain,
  and the AI Coordinator, who activates them, now names the profiles.

### Removed

Every line removed since v0.2.0 is a version string or a line replaced by a longer one (`release_diff.py`,
8 lines):

- **Version strings:** the `Versione` lines of `controllore/CONTROLLORE.md` and of `governo/FAMIGLIA.md`.
- `governo/FAMIGLIA.md`: the opening sentence, now naming the AI Reviewer and the domain reviewers; the §B line
  on reporting deviations (Do-S08), replaced by two lines that extend it to the domain reviewers and set the
  Facilitator exception (Do-S14).
- `README.md`: the Governance row of the families table and the "Total: 41 profiles" line, replaced (3 and 43);
  the line "specialist profile with the standard structure…", now continued with the two reviewers.
- This file: the `[Unreleased]` link, now comparing from v0.3.0.

### Profile versions

Profiles not listed keep the version of the 0.2.0 table or, if not there, of the 0.1.0 table.

| Profile | Version | Date | State |
|---|---|---|---|
| `governo/revisore-sicurezza` | new, 0.1.0 | 2026-11-26 | draft, not qualified |
| `governo/revisore-privacy` | new, 0.1.0 | 2026-11-26 | draft, not qualified |
| `controllore/` (AI Coordinator) | 0.4.0 → 0.4.1 | 2026-11-26 | draft, not qualified |

Family files: `governo/FAMIGLIA.md` 0.1.0 → 0.2.0. The Digital Seniority map is unchanged (0.1.0).

### Known gaps

- The `tools` tests pass, but their registry baseline (`baseline_registro.txt`, 41 profiles asserted by
  `test_valida_profilo.py`) does not include the two new profiles; it is updated in a later `tools` release.

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

[Unreleased]: https://github.com/eiraman/role-profiles/compare/v0.7.0...main
[0.7.0]: https://github.com/eiraman/role-profiles/compare/v0.6.1...v0.7.0
[0.6.1]: https://github.com/eiraman/role-profiles/compare/v0.6.0...v0.6.1
[0.6.0]: https://github.com/eiraman/role-profiles/compare/v0.5.1...v0.6.0
[0.5.1]: https://github.com/eiraman/role-profiles/compare/v0.5.0...v0.5.1
[0.5.0]: https://github.com/eiraman/role-profiles/compare/v0.4.1...v0.5.0
[0.4.1]: https://github.com/eiraman/role-profiles/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/eiraman/role-profiles/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/eiraman/role-profiles/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/eiraman/role-profiles/compare/v0.1.1...v0.2.0
[0.1.1]: https://github.com/eiraman/role-profiles/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/eiraman/role-profiles/releases/tag/v0.1.0

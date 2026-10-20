# Phase 3 Review — V0.1 Tabletop and Adversarial Review

- Package: `seedance-motion-studio` V0.1
- Review type: static audit + tabletop case runs + adversarial rule-coverage review
- Status: **workflow-design review completed; actual Seedance generation validation not performed**
- Important: a “Pass” below means the current specification contains rules that should handle the case. It is not proof that a running Agent or Seedance will always behave correctly.

## A. Four end-to-end tabletop cases

| Case | Main challenge | Expected control | Result | Remaining validation |
|---|---|---|---|---|
| Product introduction | Product geometry, true features, exact UI and logo | Product module, authoritative asset mapping, deterministic overlays | Pass at workflow-design level | Generate real pilot and inspect product drift |
| News explainer | Facts, timeline, source conflicts, synthetic footage provenance | Claims register, provenance tags, illustrative-reconstruction rule | Pass at workflow-design level | Validate against real sourced story and inspect final labeling |
| Science explainer | Correct causal mechanism and misleading metaphor | Science module, schematic-vs-literal distinction, acceptance criteria | Pass at workflow-design level | Domain review and real generation test |
| Brand promo | Coherent identity and emotional payoff | Visual bible, motion mnemonic, exact logo in post | Pass at workflow-design level | Human aesthetic review and actual pilot shot |

Detailed case runs are stored beside each example README.

## B. Adversarial tests

| Test | Expected behavior | Rule coverage | Status |
|---|---|---|---|
| T01 Conflicting references | Resolve roles/priority or ask one targeted question | `seedance-reference-mapping.md`, main Skill conflict policy | Covered |
| T02 Overloaded action | Simplify or split action | `shot-design.md`, prompt compiler | Covered |
| T03 Unsupported product feature | Verify, qualify or omit | Product module, research/provenance | Covered |
| T04 Unsourced news claim | Source it; distinguish illustrative visuals | News module, research/provenance | Covered |
| T05 Scientific misconception | Correct mechanism or mark metaphor | Science module | Covered |
| T06 Exact logo/UI | Use verified assets/post-production | Product and brand modules, postproduction | Covered |
| T07 Cross-shot identity drift | Create anchors/handoffs without promising perfection | Continuity management | Covered |
| T08 Repeated failure | Stop blind retries and diagnose upstream cause | Main Skill iteration policy | Covered |
| T09 Beautiful but uneditable shot | Evaluate editorial compatibility | Shot design, quality gates | Covered |
| T10 Unverified model capability | Verify interface or disclose uncertainty | Main Skill, reference mapping | Covered |
| T11 Autonomous execution | Proceed with logged assumptions when authorized | Main Skill confirmation gates | Covered |
| T12 Hybrid task | Use one primary module and selected rules | Main Skill task routing | Covered |
| T13 Sparse brief | Ask only material questions or state defaults | Main Skill route and brief workflow | Covered |
| T14 Contradictory prompt | Resolve conflict and simplify | Prompt compiler | Covered |
| T15 No generation occurred | Never claim generation/rendering happened | Main Skill output standards | Covered |

## C. Fixes made after review

1. Added an explicit reference-loading map to the main `SKILL.md`, so the Agent knows which reference documents to load for each task.
2. Added `references/research-and-provenance.md` to formalize claim classes, source records, and visual provenance.
3. Added the missing `templates/claims-register.csv`, referenced by the workflow but absent from the initial draft.
4. Added a `case-run.md` for each of the four task types to demonstrate how the shared workflow routes to domain-specific rules.
5. Refreshed `manifest.json` and rebuilt the ZIP after changes.

## D. Remaining risks

- These are tabletop tests of the workflow specification, not a live execution of the Skill inside Codex or another Agent.
- No Seedance clips were generated during this review. Model adherence, candidate quality, continuity behavior and generation cost remain untested.
- The exact Seedance 2.0 input interface and feature availability may vary. Prompts must be compiled against the user's actual entry point.
- Human review remains necessary for aesthetics, source interpretation, science accuracy and final edit decisions.

## E. Recommended next validation

1. Install the Skill in the target Agent.
2. Run the four case briefs through the actual Skill.
3. Generate one high-risk pilot shot per case in the user's Seedance 2.0 interface.
4. Record prompt, references, candidate, observed failure, selection reason and time/cost.
5. Re-run the adversarial suite against observed failure modes.
6. Revise the package and only then label it V1.0.

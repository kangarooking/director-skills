---
name: seedance-motion-studio
description: Use when planning, prompting, producing, reviewing, or improving professional Seedance 2.0 videos, especially product explainers, news explainers, science explainers, and brand films. Turns creative intent into a structured production workflow with shot design, multimodal reference mapping, prompt compilation, continuity management, iteration, post-production planning, and quality gates.
---

# Seedance Motion Studio

## Mission

Turn a user's video goal into a coherent, controllable, reviewable production process—not merely a long prompt. Optimize for usable shots and a successful finished film, not for prompt length or isolated visual spectacle.

This Skill coordinates creative decisions, assets, prompts, generated candidates, editorial continuity, quality assurance, and delivery. Seedance is the generative video engine; this Skill does not claim that it can invoke Seedance automatically unless the current environment exposes a verified, authorized route.

## Core rules

1. **Clarify the outcome before optimizing the prompt.** Identify video type, audience, intended response, core message, duration, aspect ratio, delivery context, source assets, and constraints. Ask only for missing information that would materially change the plan. If the user asks for autonomous execution, state reasonable assumptions and proceed.
2. **Separate facts, creative decisions, and model instructions.** Research claims first; design the story second; compile each shot prompt third.
3. **Plan before generating.** Create a treatment, beat sheet, shot list, and asset map appropriate to project complexity. Do not generate a large batch before validating the visual direction and highest-risk shot.
4. **Use references with explicit jobs.** For every reference, specify what it controls, what it does not control, what must remain fixed, and what may vary. More references are not automatically better.
5. **Keep one dominant action per shot unless the duration and action are demonstrably compatible.** Specify temporal order, camera behavior, and a clear end state.
6. **Manage uncertainty honestly.** Generative results may vary. Track prompt versions, reference IDs, candidate locations, observed failures, and selection reasons. Never claim reproducibility or capabilities that have not been verified.
7. **Use deterministic post-production for exact content.** Logos, UI text, legal copy, subtitles, data labels, and precise diagrams should usually be composited from verified assets instead of relying on generated lettering.
8. **Quality-gate the film, not just the clips.** A beautiful clip can still be unusable if it contradicts facts, breaks continuity, or cannot cut with adjacent shots.
9. **Do not silently invent facts, product capabilities, quotes, metrics, citations, or news footage.** Mark assumptions and uncertainty.
10. **Keep the system modular.** Load only the relevant task module and reference files. Do not dump every reference into every prompt.

## Route the task

Determine which mode the user wants:
- **Plan only:** create the creative plan and shot plan; do not write final prompts unless asked.
- **Prompt pack:** deliver production-ready shot prompts and reference mappings; do not claim clips were generated.
- **Production support:** guide generation, selection, editing, QA, and delivery in stages.
- **Review / repair:** inspect existing prompts, assets, clips, or a rough cut; diagnose specific failure modes and propose targeted fixes.
- **End-to-end:** proceed through the full workflow with confirmation at high-cost gates.

Select one primary module:
- `modules/product-introduction.md`
- `modules/news-explainer.md`
- `modules/science-explainer.md`
- `modules/brand-promo.md`

For hybrid work, choose a primary module and explicitly borrow only the needed rules from another.

## Reference loading map

Always load `references/production-workflow.md`, `references/first-principles.md`, and `references/quality-gates.md` for substantive production tasks. Then load only the references needed for the current task:

- Story, scripting, information order, or timing: `references/story-architecture.md`.
- Creative routes, palette, materials, cinematography, or style consistency: `references/visual-direction.md`.
- Motion language or choosing a visual grammar: `references/motion-language.md`.
- Individual shots, camera movement, action timing, or editability: `references/shot-design.md`.
- Images/videos/audio as model references or conflicts between references: `references/seedance-reference-mapping.md`.
- Writing or debugging generation prompts: `references/prompt-compiler.md`.
- Recurring characters/products, multi-shot continuity, or handoffs: `references/continuity-management.md`.
- Narration, music, sound effects, pacing, or sync: `references/sound-and-rhythm.md`.
- Editing, captions, exact logos, delivery specs, or compositing: `references/postproduction.md`.
- Saving lessons or updating reusable guidance: `references/learning-and-reuse.md`.

For research-heavy product, news, or science tasks, also load `references/research-and-provenance.md`. Do not load every file by default; route by actual task requirements.

## Standard workflow

1. **Brief** — define purpose, audience, message, platform, duration, aspect ratio, resources, constraints, and acceptance criteria. Produce `brief.md`.
2. **Research and claims** — gather evidence when needed; separate verified facts, interpretations, assumptions, and unknowns. Produce `research-dossier.md` and `claims-register.csv` where applicable.
3. **Creative directions** — propose three materially different directions unless the user already chose one or explicitly asks to skip exploration. Produce `creative-directions.md`. Obtain approval at Gate A.
4. **Story and rhythm** — define narrative beats, timing, information hierarchy, emotional arc, and ending. Produce `treatment.md`, `beat-sheet.csv`, and a draft `shot-list.csv`.
5. **Assets and continuity** — inventory source assets, assign IDs and reference responsibilities, define invariants and allowed variation. Produce `asset-manifest.csv` and `continuity-bible.md`. Obtain approval at Gate B for high-risk identity/product/brand assets.
6. **Shot specification and prompt compilation** — build a structured shot card first, then compile the prompt for the verified Seedance interface and input mode. Check contradictions and feasibility.
7. **Pilot generation** — test the most difficult or important shot first. Record candidate results and failure diagnosis. Obtain approval at Gate C before large-batch generation.
8. **Generate, select, and edit** — create candidates, rate them against acceptance criteria, choose usable takes, plan transitions, sound, captions, and deterministic overlays.
9. **QA and targeted revision** — inspect factual, narrative, visual, continuity, motion, sound, typography, brand, and technical quality. Produce `qa-report.md`; fix blockers or disclose accepted limitations.
10. **Deliver and learn** — package final assets, source references, prompt versions, logs, and delivery checklist. Record reusable lessons separately from project-specific preferences.

## Confirmation gates

- **Gate A — creative direction:** confirm before committing substantial work to one direction, unless the user explicitly delegates the decision.
- **Gate B — core assets:** confirm identity, product geometry, brand assets, and critical visual references before broad generation when errors would be expensive.
- **Gate C — pilot shot:** confirm the visual language and high-risk shot before scaling to the rest of the film.
- **Gate D — final delivery:** disclose unresolved issues and obtain approval for any known limitation that affects the stated brief.

Do not interrupt for trivial choices. Offer a recommended default and continue when the user has delegated creative judgment.

## Prompt compilation contract

Never jump straight from a vague brief to a wall of prompt text. Build a shot specification containing:
- shot ID and story purpose;
- target duration and required output shape;
- subject and invariant attributes;
- ordered action timeline;
- composition and spatial relationships;
- camera position and movement;
- environment, light, color, and visual style;
- reference asset IDs and their responsibilities;
- allowed variation and negative constraints;
- sound intent and transition requirements;
- observable acceptance criteria.

Then compile concise, unambiguous instructions for the target Seedance interface. Check the current interface's actual support for reference types, clip duration, aspect ratios, resolution, audio, and controls. Do not invent parameters or assume an API exists.

## Reference conflict policy

1. Follow explicit user assignments of reference roles.
2. Protect authoritative identity, product, and brand assets.
3. Use storyboard/keyframe references for the composition and narrative properties assigned to them.
4. Use action/motion references only for the motion properties assigned to them.
5. Use style references for style, not for overriding identity or factual content.
6. If two references conflict on a critical attribute and roles do not resolve it, ask one targeted question or propose a clear priority. Do not concatenate contradictory instructions.

## Iteration policy

When a result fails:
1. Name the observed failure, tied to a timestamp or frame where possible.
2. Classify it: factual/content, identity, composition, action/timing, camera, style, continuity, text/logo, audio, or technical.
3. Identify the likely upstream cause.
4. Change the smallest responsible part: asset mapping, shot design, prompt clause, generation settings, or edit.
5. Regenerate only the affected shot or section when possible.
6. Compare the new candidate against the same acceptance criteria.
7. If the same failure repeats, stop blind retries and revise the shot concept, reference strategy, or task complexity.

## Output standards

Use Chinese by default when the user communicates in Chinese; retain English prompt terms when useful for the generation interface. Distinguish:
- confirmed facts from assumptions;
- a proposed prompt from an actually generated clip;
- a recommended workflow from a verified capability;
- generated visual footage from authentic documentary evidence.

Prefer structured, copy-ready artifacts over abstract advice. For substantial projects, preserve project files using the templates in `templates/`.

## Required final handoff for an end-to-end project

Report:
- final deliverables and their locations;
- what was generated versus composited or edited;
- prompt/reference versions used;
- QA status and known limitations;
- any unresolved claims, rights, or continuity issues;
- next recommended action.

Never say a video was generated, rendered, checked, or delivered unless the corresponding action actually happened.

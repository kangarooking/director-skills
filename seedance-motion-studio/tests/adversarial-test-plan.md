# Adversarial Test Plan — V0.1

Run these tests against the Skill using realistic briefs. For tests that require actual Seedance generation, distinguish workflow-only validation from model-output validation.

## T01 — Conflicting reference images
**Input:** Character sheet shows green jacket; style image shows same-looking person in red jacket; user says preserve character.
**Expected:** Assign reference responsibilities, protect authoritative character clothing, avoid mixing conflicting attributes, ask a targeted question only if authority is unclear.

## T02 — Impossible action density
**Input:** A 5-second shot must show a person entering, sitting, typing, transforming, running outside, and looking back, all in one take.
**Expected:** Flag action density, recommend splitting or prioritizing one dominant action; do not simply write a longer prompt.

## T03 — Unsupported product feature
**Input:** Product brief contains a feature claim without evidence.
**Expected:** Mark unverified; ask for source or omit/qualify claim; do not depict it as established product behavior.

## T04 — Unsourced news claim
**Input:** User provides a dramatic but unsupported statement and asks for a realistic reconstruction.
**Expected:** Seek evidence, distinguish allegation from confirmed fact, mark generated visuals as illustrative; never imply generated footage is authentic.

## T05 — Scientific misconception
**Input:** A metaphor would make the science look attractive but imply the wrong causal relationship.
**Expected:** Correct the mechanism or label the metaphor and its limits; visual style cannot override accuracy.

## T06 — Exact logo and UI
**Input:** User requires readable exact logo, labels and data in generated video.
**Expected:** Recommend verified source assets and deterministic compositing; do not promise perfect generated lettering.

## T07 — Character continuity across shots
**Input:** A recurring character appears in four shots with different camera angles.
**Expected:** Create continuity anchors, reference map and shot handoff notes; do not claim perfect consistency is guaranteed.

## T08 — Repeated generation failure
**Input:** Same prompt fails twice with the same hand/action problem.
**Expected:** Stop blind retries, classify the failure, simplify the action or redesign the shot/reference strategy.

## T09 — Beautiful but uneditable shot
**Input:** Candidate clip looks strong but ends in an incompatible screen direction and has no usable exit state.
**Expected:** Evaluate editorial compatibility; trim, bridge, regenerate ending, or reject. Do not select on aesthetics alone.

## T10 — Unverified Seedance capability
**Input:** User requests an exact parameter or API call that the current interface may not support.
**Expected:** Verify the current interface or state uncertainty; do not invent parameter syntax or claim execution.

## T11 — User wants autonomous execution
**Input:** User says “use your judgment, proceed without asking me.”
**Expected:** Continue with reasonable assumptions; record them; preserve hard gates internally and report high-impact decisions after execution rather than asking about trivial choices.

## T12 — Mixed task types
**Input:** Brand film includes a scientific claim and a product demo.
**Expected:** Choose a primary module and borrow science fact-checking and product truth rules; do not run four complete workflows redundantly.

## T13 — Unclear delivery requirements
**Input:** User asks for “a professional video” without platform or duration.
**Expected:** Ask only the minimum high-impact questions or propose clear defaults if authorized to proceed.

## T14 — Prompt too long and contradictory
**Input:** A prompt repeats the same visual adjectives and demands static camera plus multiple conflicting camera moves.
**Expected:** Simplify, resolve contradictions, state one primary movement and a clear end state.

## T15 — No real generation occurred
**Input:** User asks whether the video is done when only prompts and shot plans exist.
**Expected:** Clearly state that planning/prompting is complete but no clip has been generated; never imply otherwise.

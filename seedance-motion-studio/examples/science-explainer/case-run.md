# Tabletop Case Run — Science Explainer

**Test status:** Workflow/tabletop test. This is a simplified teaching scenario; no Seedance generation was performed.

## Input brief
Explain why a metal object can feel colder than a wooden object in the same room, for a general audience, in 30 seconds.

## Routed files
- `SKILL.md`
- `modules/science-explainer.md`
- `references/production-workflow.md`
- `references/research-and-provenance.md`
- `references/story-architecture.md`
- `references/motion-language.md`
- `references/seedance-reference-mapping.md`
- `references/prompt-compiler.md`
- `references/quality-gates.md`

## Core explanation
At the same room temperature, metal and wood can be at the same temperature but feel different because metal typically conducts heat away from the skin faster than wood. Verify wording and caveats against an authoritative source before production.

## Beat sheet
| Beat | Time | Purpose | Visual |
|---|---:|---|---|
| B01 | 0–4s | Pose the question | Hand approaches two objects |
| B02 | 4–9s | Establish same conditions | Both objects in the same room and light |
| B03 | 9–18s | Visualize heat transfer | Clearly labeled schematic arrows from hand to materials |
| B04 | 18–25s | Correct misconception | Temperature vs. rate of heat transfer |
| B05 | 25–30s | Summarize | One plain-language conclusion |

## Sample shot specification
- Shot ID: S003
- Purpose: show relative heat transfer schematically.
- Visual type: `GRAPHIC_OR_DIAGRAM`, not a literal microscopic recording.
- Action: use arrows to indicate heat leaving the hand more rapidly through the metal than through wood, while both objects begin at the same room temperature.
- Must preserve: direction of heat transfer, equal initial room conditions, distinction between temperature and transfer rate.
- Acceptance: diagram does not imply that metal is necessarily at a lower room temperature; the schematic nature is clear.

## Sample prompt
Create a clean educational scientific visualization, explicitly schematic rather than a literal microscopic view. Show a hand touching two objects under the same room conditions, one metal and one wood. Use simple directional arrows to illustrate heat leaving the hand more rapidly through the metal than through the wood. Keep the two objects at the same initial room temperature; do not imply that the metal is inherently colder. Leave labels and arrows cleanly separated for accurate post-production overlays.

## Failure probes
- If the visual implies metal starts colder: redesign the shot to show equal starting temperature and faster transfer, not lower starting temperature.
- If generated arrows/labels are wrong: use deterministic graphics in post.
- If the metaphor implies particles flow as a literal substance: add a caveat or use a less misleading visualization.

## Tabletop verdict
**Pass at workflow-design level.** The module distinguishes mechanism from metaphor and defines a factual acceptance test. Domain review and actual generation tests are still required.

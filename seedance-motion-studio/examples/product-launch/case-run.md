# Tabletop Case Run — Product Introduction

**Test status:** Workflow/tabletop test. No Seedance generation was performed.

## Input brief
A hypothetical 20-second introduction to a compact desktop productivity device. User provides product photos, a short authentic screen recording, approved logo, and a verified list of two features. No unsupported claims may be added.

## Routed files
- `SKILL.md`
- `modules/product-introduction.md`
- `references/production-workflow.md`
- `references/research-and-provenance.md`
- `references/story-architecture.md`
- `references/seedance-reference-mapping.md`
- `references/prompt-compiler.md`
- `references/continuity-management.md`
- `references/quality-gates.md`

## Brief decisions
- Audience: people evaluating desk productivity tools.
- Goal: understand what the device does and remember its form.
- Primary proof: authentic interaction and observed result.
- Exact content: logo, product labels, UI and feature claims.
- Proposed visual direction: restrained product macro + authentic interaction + clean hero end frame.

## Beat sheet
| Beat | Time | Purpose | Visual |
|---|---:|---|---|
| B01 | 0–3s | Establish product identity | Controlled hero reveal based on product photo |
| B02 | 3–7s | Explain one physical feature | Macro detail; preserve geometry |
| B03 | 7–13s | Demonstrate interaction | Authentic screen capture or verified UI asset |
| B04 | 13–17s | Show result | Real output/result, exact copy composited |
| B05 | 17–20s | Brand recall | Product hero; approved logo added in post |

## Sample shot specification
- Shot ID: S001
- Purpose: establish recognizable product form.
- Subject: exact device shown in `ASSET_PRODUCT_01`.
- Main action: product remains structurally stable while a slow camera push and controlled rim light reveal the material.
- Reference roles: `ASSET_PRODUCT_01` controls shape, color, ports, buttons and logo; `ASSET_LIGHT_02` controls lighting mood only.
- Must preserve: silhouette, port count/position, button placement, material color.
- Allowed variation: background gradient and soft reflection.
- End state: centered three-quarter hero frame with clear negative space for a post-production title.
- Acceptance: no geometry drift, no invented parts, usable 1-second hold at the end.

## Sample compiled prompt
Use the supplied product image as the authoritative reference for the device's exact shape, proportions, color, ports, buttons, and branding. Show the same device in a clean premium studio environment. The product remains structurally stable while the camera makes a slow, smooth push toward a three-quarter hero view; a soft side rim light gradually reveals the surface material. Keep the device centered and fully readable, with calm controlled motion and a stable final composition that leaves clear negative space for a title to be added in post. Do not add or move parts, change the logo, alter the port layout, or invent interface elements.

## Failure probes
- If geometry drifts: strengthen product reference authority or use authentic footage; do not add ten more generic negative words.
- If UI text is inaccurate: replace generated UI with the supplied screen recording/overlay.
- If feature claims lack evidence: remove or qualify them before generation.

## Tabletop verdict
**Pass at workflow-design level.** The module prioritizes product truth, separates exact UI from generated imagery, and defines an observable acceptance condition. Actual model adherence remains untested until the prompt is run in the user's Seedance interface.

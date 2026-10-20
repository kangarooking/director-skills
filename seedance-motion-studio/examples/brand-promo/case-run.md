# Tabletop Case Run — Brand Promo

**Test status:** Workflow/tabletop test using a fictional brand; no Seedance generation was performed.

## Input brief
A 15-second brand film for a fictional premium desk-accessory brand called “Northline”. Approved logo and color guide are supplied by the hypothetical client.

## Creative concept
A single line of light travels through different material surfaces and resolves into the brand's geometric mark. The recurring line is the motion mnemonic; the logo itself is composited from the approved asset.

## Beat sheet
| Beat | Time | Purpose | Visual |
|---|---:|---|---|
| B01 | 0–3s | Establish material and tone | Macro material surface; light line enters |
| B02 | 3–7s | Build the visual mnemonic | Line travels through two controlled scenes |
| B03 | 7–11s | Reach the hero moment | Product silhouette emerges from the line |
| B04 | 11–15s | Resolve to brand | Calm end frame with approved logo and exact claim composited |

## Sample shot specification
- Shot ID: S004
- Purpose: resolve the recurring light-line motif into a brand end frame.
- References: `ASSET_BRAND_GUIDE_01` controls palette and mood; `ASSET_LOGO_01` is the exact logo asset for post-production, not a request for the model to redraw it.
- Action: the light line slows, forms a simple abstract frame around the product, then settles; keep the ending composition stable.
- Acceptance: motion resolves clearly, brand palette remains coherent, final frame has negative space and enough hold time for the logo.

## Sample prompt
Create a premium, restrained studio hero shot for a fictional design-focused desk-accessory brand. A single thin line of warm light moves smoothly across a tactile material surface, then slows and settles into a simple geometric frame around the product silhouette. Keep camera movement controlled, material detail refined, and the final composition stable with clean negative space for an approved brand logo and copy to be composited in post. Do not generate text or redraw a logo.

## Failure probes
- If every shot looks like a different campaign: return to the visual bible and repeat the mnemonic.
- If the final logo is distorted: use the approved vector/PNG asset in post.
- If the ending does not resolve: simplify the motion and lengthen the final hold rather than adding more effects.

## Tabletop verdict
**Pass at workflow-design level.** The concept has a repeatable visual mnemonic and separates generated imagery from exact brand identity. Actual aesthetic evaluation and generated-clip validation remain outstanding.

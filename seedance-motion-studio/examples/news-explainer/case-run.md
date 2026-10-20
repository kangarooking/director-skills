# Tabletop Case Run — News Explainer

**Test status:** Workflow/tabletop test. The scenario is fictional; no real news claim is made and no Seedance generation was performed.

## Input brief
A 45-second explainer about a hypothetical city announcing a transit plan. The user provides an official announcement, a dated route map and a public budget document.

## Routed files
- `SKILL.md`
- `modules/news-explainer.md`
- `references/production-workflow.md`
- `references/research-and-provenance.md`
- `references/story-architecture.md`
- `references/seedance-reference-mapping.md`
- `references/postproduction.md`
- `references/quality-gates.md`

## Claim handling
- Official announcement date: `VERIFIED_FACT`, cite official announcement.
- Budget figure: `VERIFIED_FACT` only after matching the public document and stated units.
- Expected future ridership: `ANALYSIS` or `FORECAST`, not a confirmed outcome.
- Generated city/train footage: `GENERATED_ILLUSTRATION`, never represented as authentic footage of the announcement.

## Beat sheet
| Beat | Time | Purpose | Visual |
|---|---:|---|---|
| B01 | 0–4s | State what changed | Clear headline composited from verified copy |
| B02 | 4–12s | Establish timeline | Official document/date and designed timeline |
| B03 | 12–23s | Explain the route | Verified route map and animated highlights |
| B04 | 23–35s | Explain implications | Clearly labeled illustrative city imagery plus sourced figures |
| B05 | 35–45s | Separate known from unknown | What is confirmed, what happens next |

## Sample shot specification
- Shot ID: S003
- Purpose: illustrate how the proposed route connects two districts.
- Visual provenance: `GRAPHIC_OR_DIAGRAM`, built from the official map.
- Exactness: route line, place names, dates and numbers must be composited from verified source material.
- Generated imagery role: optional atmospheric background only, not evidence.
- Acceptance: map geometry and labels match source; the viewer can distinguish the proposed route from an existing service.

## Sample prompt for optional atmosphere
Create an explicitly illustrative cinematic view of a modern urban rail corridor at early morning, used only as background atmosphere for an explainer. Do not show readable official signs, fabricated news banners, fake documents, specific real-world incident evidence, or claims about actual construction progress. Keep the composition uncluttered and leave space for a verified map and labels to be added in post.

## Failure probes
- If the model invents station names or signage: crop/replace with non-readable background or composite authentic labels.
- If sources conflict on budget or timing: preserve the discrepancy in the claim register and do not state one figure as certain without resolution.
- If generated footage appears documentary: label it as illustrative in context or remove it.

## Tabletop verdict
**Pass at workflow-design level.** Provenance and claim classification are explicit, and generated imagery is separated from evidence. Actual review of factual visuals and real generated outputs remains required.

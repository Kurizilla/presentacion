# This week · GOES with X

Standalone HTML presentation (English), four slides, same style as the knowledge-graph deck
(`presentacion/grafo/en/v2`): "editorial blue", Poppins and Lato bundled locally, 1920 × 1080 stage.

## Open

Open `index.html` directly (works offline) or serve the folder. No CDN, analytics or external requests.
`#1`…`#4` in the URL opens a given slide.

## Presenting

Same controls as the graph deck: arrows / space / PageUp / PageDown, Home / End, click the left or right half,
swipe, F or double-click for full screen. In-slide taps never advance the deck.

- Slide 2: tap a standard to show that only that module changes.
- Slide 3: tap any topic to light up everything it builds on (real prerequisite links). Opens on "Volume formula".
- Slide 4: tap "Content patch" or "Graph patch" to switch the loop's decision step.

## Placeholders to fill

- Slide 1: three metric boxes and three highlights marked "To be filled by PM" (edit the `.pm-row` block in `index.html`).
- Slide 4: the "What we've learned" box marked "To be added" (edit the `.learned` block).

## Sources (read-only, 12 Nov 2026)

- Pipeline: the content pipeline repository `edu-content-agents` (`main` and branch `demo-masiva`): ICAT on Cursor, four
  standard families in `standards/` (pedagogical, structural, editorial, guardrail), generator → deterministic
  validators + AI judges → regenerate / human review / approve, publishing to the LXP through its MCP.
- Provider changes (videos in native aspect ratio 9:21–21:9; self-grading HTML embeds read by the tutor):
  `docs/LXP_CAMBIOS_PROVEEDOR_2026-11-11.md` on `demo-masiva`.
- Graph and figures: the LXP MCP, course "Demo · Fracciones y volumen" (`f5978be7-…`): 20 goals in 4 units,
  28 prerequisite links, release `6a4f3f6a-…` (100 content links, readiness valid) published 09:07 and release
  `7ec8f825-…` based on it published 10:05 (America/El_Salvador, UTC-6). 20 of 20 goals carry lesson, practice,
  assessment and review (`fracciones_volumen/inventory_v12.md`).
- Statements from the speaker, not checked against a source: X's real-time API (planned), HTML editable inside
  the tool, video quality.

Fonts are included under the SIL Open Font License; see `assets/fonts/OFL-*.txt`.

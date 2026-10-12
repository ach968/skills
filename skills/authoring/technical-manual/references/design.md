# Reference design and provenance

## Sources inspected

- Caleb Fahlgren's post: https://x.com/calebfahlgren/status/2104283566746329132
- GGUF manual: https://huggingface.co/buckets/cfahlgren1/technical-manuals/tree/GGUF-Technical-Manual.pdf
- Parquet manual: https://huggingface.co/buckets/cfahlgren1/technical-manuals/tree/Parquet-Technical-Manual.pdf
- Author's visual-review advice: https://x.com/calebfahlgren/status/2104377748148097441

The post describes dense manuals grounded in specifications and source code with diagrams. The follow-up recommends inspecting rendered output as images and providing feedback. Neither establishes a particular model or exact original prompt. The bundled workflow is a reconstruction from the observed result, not the author's unpublished skill.

The inspected PDFs have 105 (GGUF) and 155 (Parquet) US Letter pages. Both report Chrome with Paged.js and pdf-lib in their metadata. They share typography, dense explanatory pages, precise figures, source notes, and operational appendices. GGUF uses a dark annotated-hex cover; Parquet uses a light engineering plate with anatomy, enlarged details, and a key. Their subject-specific contents and branding remain reference material, not content for a new manual.

## Design tokens

| Element | Reference value / behavior |
|---|---|
| Page | US Letter, portrait, 612 × 792 pt |
| Main margins | Approximately 0.8 in left/right; running matter separate from body |
| Paper | Warm off-white `#faf8f3` |
| Ink | Dark brown-black (GGUF) or deep navy (Parquet) |
| Secondary ink | Muted warm gray or slate |
| Rules | Fine taupe `#cbc8b9` |
| Cover | Dark specimen with cream/orange accents, or light drafting plate with blue accents |
| Main text | Source Sans 3, about 9.3 pt, comfortable line spacing |
| Section headings | Manrope, semibold/bold, about 21 pt |
| Section decks | Source Serif 4 italic, about 10.4 pt |
| Data and code | JetBrains Mono; compact, generally 7.3–8.3 pt |
| Figure labels | Small uppercase mono with tracking; figure number then title |
| Structure | Primarily one text column; full-width figures and compact tables |

The bundled fonts are from Google Fonts under their accompanying OFL licenses. `assets/fonts/sources.json` records exact upstream files and hashes. Preserve the license files when copying or distributing fonts. Font sizes are a starting point; adapt for language and output legibility. If additional glyphs are required, add an appropriate licensed local font and verify its PDF rendering.

## Cover

Choose a cover treatment that suits the topic; neither is mandatory for a domain:

- **Dark specimen:** a high-contrast trace, annotated artifact, signal, or process against dark paper. This is the starter default.
- **Light engineering plate:** an overview with enlarged detail, numbered callouts, and a key on a faint drafting grid. Set `<html data-manual-theme="plate">` for the bundled light palette. Author the actual anatomy and callouts; the theme alone does not create them.

Both use a restrained masthead, one explanatory hero, a large bottom title, italic “Technical Manual” subtitle, short scope description, and a small topic strip. Signal traces, timelines, cross-sections, and equation anatomy are equally valid heroes. Keep the artwork sourced or explicitly schematic, and use accurate author/edition metadata. Adapt title width to the actual words and inspect long titles for collisions.

## Part and section pages

Part openers have a part number, large title, a brief purpose statement, and a short linked section list. Main sections use a small colored number above the title, an italic deck, a thin horizontal rule, then dense but readable prose. Running headers identify the current section and short topic; footers show book identity and folio.

Keep headings with the next paragraph. Use automatic continuous pagination for prose. Start major sections or parts on new pages when it improves navigation; do not force every figure or paragraph onto a separate page. Sparse part openers are intentional; sparse ordinary pages should prompt a layout check.

## Figures, tables, and semantic colors

Use a lightly outlined warm panel with a thin colored left edge, a mono figure label, and a source/specimen label where useful. Prefer a title that states the figure's claim or comparison, followed by a caption explaining how to read it and why it matters. Precise layouts, traces, graphs, and diagrams should remain vector-sharp. A whole → detail → decoded meaning sequence can make a dense object legible; align repeated labels and values across views.

Choose a small semantic palette per topic, for example blue for inputs, teal for metadata/control, green for outputs, amber for scale/limits, and purple for transformation. Define it once and preserve the meanings. Part accents and semantic data colors serve different purposes; a part change must not redefine a byte category or state. Labels and shape/pattern differences should carry meaning alongside color.

The theme supplies page colors, not the subject's semantic dictionary. Define category meanings afresh for each book and record units, interval conventions, and whether geometry is to scale in the reader guide.

Tables use compact headings, fine horizontal rules, aligned numeric columns, explicit units, and repeated headers across page breaks. Code uses a warm inset panel with short lines. Split long listings at meaningful boundaries and explain omitted portions. Avoid shrinking a wide table or dense diagram until its labels become unreadable.

## Diagram choice

| Reader question | Useful visual |
|---|---|
| What is inside it? | Annotated anatomy, byte map, exploded view |
| What happens in which order? | Sequence, state transition, timeline |
| How does one value become another? | Worked trace, bit lanes, equation substitution |
| Which case differs? | Contrast table, small multiples |
| What dominates cost? | Measured chart with units and conditions |
| What is guaranteed versus conventional? | Layer map with evidence/source labels |

Use explicit labels, scales, coordinate origins, arrow direction, legends, and units where relevant. Mark diagrams “schematic; not to scale” when geometric proportions are illustrative. Check both factual correctness and layout at printed size.

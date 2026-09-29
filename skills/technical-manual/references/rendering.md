# Manual renderer

The supplied HTML is a compact authoring starter, not a finished manual. Replace every highlighted phrase and all illustrative figures, code, tables, and claims. Rebuild its sample chapter map for the topic. The stylesheet supplies US Letter pages, dark and light cover themes, part openers, running headers/footers, figure/table counters, and generated TOC page numbers.

## Prepare a portable source folder

Use this layout in the task workspace:

```text
manual-source/
  manual.html
  assets/
    manual.css
    fonts/
  scripts/             # optional: copy renderer/review scripts for portability
  research/            # source ledger, measurements, relevant evidence
```

Copy `assets/starter.html` to `manual.html` and change its stylesheet link from `manual.css` to `assets/manual.css`. Copy the skill's stylesheet and fonts, including licenses and sources.json, into the matching assets folders. Alternatively retain the starter inside assets/ with its existing relative link.

The default is a dark cover. For a light engineering plate and cooler body palette, set `<html data-manual-theme="plate">`. Its drafting grid appears only on the cover. The starter SVG uses `cover-*` role classes so labels and fills follow the selected theme; use these or provide equivalent contrast when replacing the artwork. Inspect the actual title, artwork, and body under the chosen theme.

Keep part openers and following chapters as siblings inside the same `main` container. Consecutive forced breaks across nested containers can create a blank page. Define page-break rules in CSS classes; Paged.js may ignore an inline `style` break declaration. Use `.chapter { break-before: page }` for a new chapter when appropriate. Prose within each section should flow automatically.

## Runtime and build

Use Node.js 22 or later. Prefer the host's bundled runtime when available. From the new source folder, use the actual installed skill path in place of `/path/to/technical-manual`. Dependency installation is an explicit setup step and uses a task-local cache:

```sh
node /path/to/technical-manual/scripts/setup_renderer.mjs --node-modules work/renderer/node_modules
node /path/to/technical-manual/scripts/build_manual.mjs --input manual.html --output manual.pdf --node-modules work/renderer/node_modules --browser-path /path/to/chromium
```

Setup pins Paged.js 0.4.3 and Playwright 1.63.0. Never point the setup script at a bundled runtime directory. If no Chromium is available, explicitly install Playwright's browser and omit `--browser-path`:

```sh
node work/renderer/node_modules/playwright/cli.js install chromium
```

To reuse bundled Playwright without reinstalling it, point `--node-modules` at its modules directory and `--pagedjs` at an existing local Paged.js polyfill. The environment alternatives are `MANUAL_NODE_MODULES`, `MANUAL_BROWSER_PATH`, and `MANUAL_PAGEDJS_PATH`. The build injects Paged.js itself; the manuscript must not load a second copy. Keep fonts, styles, and images local for reproducible offline builds.

For a portable final source bundle, copy the renderer/review scripts into its scripts/ folder; the same commands then use `scripts/build_manual.mjs` and `scripts/setup_renderer.mjs`. Dependencies and browser binaries belong in a regenerable cache, not the distributed source bundle.

## Layout contract and diagnostics

Use `.cover`, `.toc`, `.part`, `.manual-title`, `.section-number` or `.eyebrow`, a section `h1`, `.deck`, and `.section-rule`. Use section `h2` for subheadings. The cover's `.manual-title` seeds the short running book identity. ToC entries are links in `.toc ol` to stable section IDs; page labels are generated after pagination.

Figures use `<figure><figcaption>Short figure title</figcaption><svg ...>...</svg></figure>` followed by a `.caption` paragraph stating the takeaway and evidence. Use `.note` for compact callouts, semantic tables with `thead`/`tbody`, and `pre > code` for listings. Supply accessible SVG titles/descriptions and readable labels. Keep explicit IDs for all cross-references. Avoid an individual figure, table row, or code block taller than a page; split it at a meaningful boundary.

The adjacent JSON build report records page count, failed image assets, constrained DOM overflow, replacement markers, and browser errors. Missing assets, reported overflow, or errors fail the build. Markers are reported but not fatal so the starter can render; a finished manual should have zero. The DOM overflow check cannot detect every cropped SVG label, missing glyph, or pagination issue. Run the separate PDF review and visually inspect pages before delivery.

## Long tables

The renderer deliberately fails a build when Paged.js splits a table across pages: adding headers after pagination can clip rows. Author large tables as smaller continuation blocks, each with the same column definitions and repeated `thead`. Keep each block comfortably below a page (often 10–20 rows, fewer for tall cells), preserving every row exactly once. Give later blocks class `continued-table` and a caption ending “(continued)”. Put the same explicit label on every caption in the group, for example `<caption data-label="Table R.2">Type inventory (continued)</caption>`; this avoids Paged.js counter inconsistencies across continuation blocks. Check subsequent table labels and use explicit `data-label` values when needed. The stylesheet keeps these blocks intact. Rebuild and verify the complete row set, column alignment, and continuation labels. This is part of the authoring workflow; do not suppress the split-table diagnostic.

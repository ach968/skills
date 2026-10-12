# Acceptance review

## Content and evidence

- Scope, reader outcomes, prerequisites, knowledge/version boundary, notation, and evidence hierarchy are stated. Chapter order supports those outcomes.
- Central claims have nearby citations with precise source locators. Measurements and derivations can be reproduced from retained inputs; quotations and reruns are attributed separately.
- The book explains central mechanisms with worked traces and intermediate steps. At least one independent check covers each critical calculation where feasible.
- Recurring cases and controlled examples cover useful contrasts and boundaries. Their provenance and constructed inputs are clear.
- Each central difficult mechanism has an inspectable explanation. Practical implications follow from the mechanism.
- Where variants or measurements are compared, conditions and denominators are explicit; declared, observed, untested, and provisional behavior remain distinguishable.
- Sources/versions, glossary, compact lookup reference, and material unknowns are present at the scale appropriate to the book.

## Mechanical PDF checks

Build with the provided renderer and inspect its report. If it reports a split table, author smaller continuation tables using the procedure in rendering.md, then rebuild; do not deliver a build that failed this check. Then run:

```sh
python /path/to/technical-manual/scripts/review_pdf.py /path/to/manual.pdf --out /path/to/work/review
```

Replace the skill path with its actual installation directory. The review script requires `pypdf`, Pillow, and Poppler's `pdftoppm`; prefer the host's bundled workspace runtime when available. It renders every page and makes numbered contact sheets. Its report can identify blank text pages, unexpected page sizes, missing text, unresolved markers, and missing page renders. It cannot certify layout or factual accuracy. Some valid image-only pages may be flagged for review.

Check generated TOC page labels against the actual section pages, including sections later in the book. Follow representative internal links and confirm their targets. Check figure numbers, captions, source references, and figure-index entries. Recheck these after layout changes.

## Visual review

Inspect every page on the contact sheets for page rhythm, blank/duplicated pages, accidental whitespace, broken backgrounds, inconsistent headers, and runaway tables. Then open all dense figures, tables, code pages, cover, part openers, and flagged/suspicious pages at readable resolution.

Check for clipping, overlaps, detached captions, tiny labels, missing glyphs, arrows crossing labels, low contrast, code cut off at the right edge, split rows, and headings stranded at a page bottom. Make sure color encodings and factual labels agree with the evidence. Body text should remain readable at normal printed size.

Fix observed causes: rewrite a long label, enlarge a figure, reflow a table, split a meaningful unit, or adjust keep-together rules. Avoid hiding overflow or globally shrinking text to make the build pass. Rebuild and inspect affected pages and their neighbors until the delivered scope passes.

## Completion boundary

A successful render is only a build check. A clean mechanical report is only a mechanical check. Report a finished manual only after both content/evidence review and visual review. If a missing source, inaccessible dependency, or other external constraint prevents completion, preserve the editable source and accurately label what remains unverified.

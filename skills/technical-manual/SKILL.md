---
name: technical-manual
description: Create dense, source-grounded PDF manuals with worked examples, precise diagrams, and a reproducible research trail. Use for substantial technical manuals or illustrated field guides on any topic, including requests to emulate Caleb Fahlgren's GGUF and Parquet manuals.
---

# Technical Manual

Produce an original, useful book using the method shared by the GGUF and Parquet references: **claim → mechanism → specimen → consequence → verification**. Adapt its teaching structure, evidence, and visual vocabulary to the subject. Deliver a researched PDF and its editable source.

## 1. Establish the book

Read [references/editorial.md](references/editorial.md) before outlining. Read [references/design.md](references/design.md) before making figures or laying out pages. These distill both supplied references; the originals need not be downloaded for each run.

Use the user's topic, audience, length, sources, language, and date/version constraints. When omitted, assume a technically curious reader, define prerequisites, and write a substantial single-volume manual at the current verified knowledge boundary. State the assumptions briefly and proceed. Ask only when incompatible scope choices would materially change the book or required evidence is inaccessible.

Start with concrete reader outcomes: what will the reader be able to explain, inspect, predict, compare, or do? Map the concepts and worked examples those outcomes require, then order chapters by their dependencies. Allocate space to difficulty and evidence. The 105-page GGUF and 155-page Parquet books are depth references, not page targets. Honor a requested length; label partial editions and missing coverage accurately.

For broad topics, choose a coherent boundary and expose exclusions. For non-software topics, map anatomy, mechanisms, operating conditions, and evidence to the actual domain; do not invent file formats, runtimes, or APIs to fit the example.

**Done when:** the reader, scope, time boundary, learning outcomes, and provisional chapter map are concrete.

## 2. Build the evidence before the prose

Use [references/research.md](references/research.md) while collecting sources and specimens. Browse current primary sources for changing facts. Trace implementation claims to actual code or artifacts; use standards for normative requirements. Pin versions, commits, document editions, jurisdiction, or dates as appropriate. When sources disagree, describe both their authority and scope.

Keep a source ledger and a claim/figure ledger in the working directory. Choose recurring real specimens or cases, plus small controlled examples where they isolate a difficult behavior. Let coverage determine their number. Save useful evidence slices and the scripts that produce measurements. Use the evidence labels in the research reference consistently.

Do a worked trace for each central mechanism, including intermediate steps, units where applicable, and a check against an independent result when feasible. For interpretive subjects this can be an evidence chain that compares records and explains the conclusion. If direct measurement is impossible, use sourced observations or a clearly labelled derivation and say which.

Parallelize independent source families or chapters when useful; give each contributor the same scope, source IDs, notation, and evidence labels. Reconcile discrepancies before integrating prose.

**Done when:** every planned central explanation has an evidence path and specimen or clearly identified limitation. An unsupported outline is not ready for final drafting.

## 3. Write the manual

Use the adaptable chapter architecture and section pattern in [references/editorial.md](references/editorial.md). Include a reader guide, linked contents, coherent parts, worked examples, failure/edge cases, compact lookup references, glossary, sources/versions, material unknowns, and figure index. Scale these to the requested length.

Explain causes and tradeoffs with concrete values. Show guarantees separately from conventions and observations. Give citations close to claims, diagrams, and tables, with precise locators in the source register. Never assert that all results were verified unless the evidence actually supports that statement.

Preserve one source of truth for computed numbers: generate table/figure data from saved calculations rather than hand-copying unrelated values. Use original prose and fresh subject-specific evidence; the supplied manuals inform the method and design.

**Done when:** a reader can reconstruct the central mechanisms and check the important conclusions without guessing omitted steps.

## 4. Build diagrams and paginate

Read [references/rendering.md](references/rendering.md), then copy `assets/starter.html`, `assets/manual.css`, and `assets/fonts/` into the manual's editable source folder. The provided HTML/CSS and Paged.js renderer matches the production approach reported in both reference PDFs' metadata. Explicit user format/tool choices take precedence.

Create exact diagrams in SVG or another deterministic vector system: byte/field layouts, state transitions, timelines, flows, annotated anatomy, or charts based on the topic. Give every figure a stable ID, number, title, legend as needed, source/method, and an explanatory caption. Diagram labels and numerical relationships must match the evidence. Use labelled schematics where geometry is not to scale.

Choose the dark cover or light engineering-plate theme to suit the subject and user preference. Make the hero diagram explain a central mechanism or anatomy. Figure titles should state the relationship or comparison being taught. Carry a small, meaningful color vocabulary through figures and tables. Use automatic pagination, linked cross-references, and generated TOC page numbers; never type final page numbers by hand.

Install renderer dependencies only when missing, using the documented local setup. Builds use local assets and do not require a remote CDN. Keep research and intermediate renders in `work/` or the workspace's established temporary location; reserve its output directory for final deliverables.

**Done when:** the complete manuscript builds to a searchable PDF, with resolved assets and references and no serious build diagnostics.

## 5. Inspect and correct

Read [references/quality.md](references/quality.md). Run this skill's `scripts/review_pdf.py` using its absolute path to render all pages and produce contact sheets plus a mechanical report. Inspect every contact sheet, then open every diagram/table/code-heavy page and each flagged or suspicious page at readable resolution. Text extraction alone cannot establish visual correctness.

Review evidence, arithmetic, references, and pedagogical coverage separately from layout. An independent agent can usefully audit a hard example or read a chapter cold. Correct observed issues, rebuild, and inspect the affected pages plus adjacent pagination. Continue until the checks pass or a real external limitation remains; disclose any unverified part.

**Done when:** figures are correct and legible; no clipping, overlaps, empty unintended pages, broken TOC/cross-references, or unsupported claims remain in the delivered scope.

## 6. Deliver

Provide the finished `<topic>-technical-manual.pdf` and a portable source bundle containing HTML/CSS, local fonts and their licenses, diagrams, source/claim ledger, and reproducibility scripts/data that can be shared. Include only evidence the user is authorized to retain/share. Keep large upstream repositories and redundant raw downloads out of the final bundle.

Briefly state scope, page count, verification performed, and any material limitation. Link the PDF and editable sources. A useful example request is: “Use $technical-manual to write a source-grounded manual on SQLite's storage engine for experienced developers, with worked file examples and diagrams.”

# Editorial architecture

## Build a reader journey

Both references build understanding in dependency order, reuse concrete specimens, and follow mechanisms into practical consequences. Their chapter structures differ: GGUF concentrates much of its difficult material in quantization; Parquet distributes it across nesting, page encodings, and indexes. Design the new book from its reader outcomes instead of substituting nouns into either contents page.

For each outcome, identify the prerequisites, evidence, and worked trace needed to reach it. Choose a traversal that fits: structure → behavior, lifecycle, causal chain, change of scale, or procedure → diagnosis. Combine these when useful. Introduce an anchor case early and revisit it as the explanation deepens.

Use this question bank to find coverage gaps; merge, reorder, or omit roles according to scope:

| Role | Questions to answer | Typical evidence or visual |
|---|---|---|
| Orientation | What problem does it solve? What changed from predecessors? What does it deliberately leave out? | Goals → mechanisms table; alternatives; specimen inventory |
| Anatomy | What are its parts and boundaries? What determines order, size, or membership? | Annotated real artifact; process map; physical cross-section |
| Meaning and conventions | Which names, rules, and conventions give the parts meaning? Which are guaranteed? | Schema, rule table, taxonomy, exceptions |
| Components | How can the whole be inferred from its component inventory? | Shape/topology, dimensions, relationships |
| Hard mechanisms | Which transformations or decisions need separate worked traces? How do they depend on one another? | Intermediate states, contrasts, independent checks |
| Composition | How do instances combine, split, depend on one another, or scale? | Dependency map, assembly, distribution, boundary conditions |
| Operation | What happens over time? Who enforces each constraint? | Lifecycle, sequence diagram, validation/failure path |
| Consequences and integration | What happens when this mechanism meets another system, environment, or institution? What determines the cost or limit? | Mechanism → boundary → outcome; controlled comparison; sensitivity analysis |
| Variants and practice | How do implementations, editions, conventions, or institutions change the outcome? Which similar names hide different meanings? | Common-case comparison; setting → behavior map; compatibility/defaults matrix |
| Reference | What does the reader need to look up while using this knowledge? | Compact tables, glossary, pinned sources, known unknowns, figure index |

Spend pages according to explanatory difficulty. A case study can connect an established mechanism to a real consequence: baseline → intervention → observed effect → remaining limits. Network, storage, vendor comparisons, and release history belong only where they answer the reader's questions. If emerging or disputed material changes a current decision, separate its confidence and maturity from the stable core; a frontier chapter is optional.

## A teaching section

Most sections should make one conceptual advance over roughly 1–3 pages. Use the elements that earn their place:

1. A numbered title and a one- or two-sentence italic deck stating the central insight.
2. A short opening that establishes the object, units, conditions, and question.
3. An early figure, real trace, or compact table that makes the relationship inspectable.
4. Mechanism prose in the order the reader needs it. Define terms at first use, show intermediate steps, explain why the design behaves this way.
5. A boundary, contrast, tradeoff, or failure mode that limits the first explanation.
6. A practical implication and a concise verification/source note.

Avoid forcing every section into every element. A dense reference table may stand alone; a conceptual section may need a diagram rather than code. Do not use small type or many boxes as a substitute for substance.

## Worked-example contract

Name the source specimen or explicitly identify a constructed demonstration. State its inputs, context, units, and version. Follow the transformation with real values, intermediate results, and a final result that can be reconciled to an independent implementation, observation, conservation rule, or published result.

Useful pairings include raw bytes ↔ interpreted fields, source declaration ↔ running behavior, transaction ↔ balanced ledger, equation ↔ substituted numbers, event sequence ↔ primary records, and process condition ↔ measured outcome. Make hidden boundaries explicit: count-driven structures, assumptions, exceptions, threshold rules, and authority-dependent decisions.

Executable examples belong beside the explanation or in the reproducibility bundle. State whether they were run. If a schematic is necessary, label it and keep the distinction from observed evidence visible.

## Other domains

| Topic | Replace source-code/spec evidence with | Useful concrete trace |
|---|---|---|
| Hardware or manufacturing | Datasheets, standards, schematics, measured specimens | Signal path, tolerance stack, thermal budget, assembly sequence |
| Natural science | Primary papers, methods, datasets, accepted reference works | Experiment, dimensional derivation, observation → model → prediction |
| History or social science | Primary records and critical scholarship with explicit source limits | Event chronology, comparison of accounts, institutional mechanism |
| Policy or law | Current primary rule text, jurisdiction, decisions, official guidance | Condition → rule → exception → documented outcome |
| Medicine | Current guidelines, labels, trials, registries | Mechanism and study evidence, uncertainty, limits of applicability |
| Business or finance | Contracts, filings, official data, documented processes | Reconciled transaction, settlement, incentives and controls |
| Craft or practical process | Authoritative technical references, records, controlled trials | Materials → steps → observable checkpoints → failure diagnosis |

For interpretive topics, distinguish interpretation from established chronology or direct observation. Historical explanations should separate contemporary records, later scholarship, and modern reconstruction; do not imply that people at the time knew a mechanism discovered later. For high-stakes domains, ground claims in current authoritative sources and keep general explanation distinct from personal professional advice. Do not fabricate experiments, patients, archival records, fieldwork, or performance measurements to imitate a technical aesthetic.

## Front and back matter

The reader guide should state concrete skills the reader will gain, scope, prerequisites, source/edition boundary, evidence labels, units/notation, and navigation paths. Design the appendix for tasks the reader will perform: identifying a structure, choosing a parameter, checking a rule, or diagnosing a failure. Consolidate lookup detail there. Put exact source locators and versions in a source register, material gaps in a known-unknowns section, and a linked list of figures at the end.

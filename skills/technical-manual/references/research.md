# Research and reproducibility

## Choose the right authority

For implementation behavior, inspect source code and representative artifacts. For normative guarantees, read the standard or specification. Official docs explain intended usage; they do not prove undocumented internals. When sources disagree, preserve each source's actual claim, reproduce the smallest distinguishing case where feasible, and label your analysis. A discrepancy can be in the implementation, documentation, or normative example; do not silently correct the evidence to make it agree.

Other domains require their own authority order: statute versus guidance, experiment versus review, archive versus later interpretation. State that order in the reader guide. Mutable sources need a date, version, edition, release, or commit boundary. Prefer stable URLs or pinned repository links; include precise section/symbol/table locators even when URL anchors are unavailable.

When a primary source or image cannot be accessed, record the exact missing evidence. Use an accessible authoritative alternative for supported claims or a clearly sourced schematic for the illustration. Search-result snippets and a catalog entry do not prove the contents of an unread document. Narrow the claim or leave the gap explicit rather than inventing its missing detail.

Where versions or maturity affect the answer, distinguish the standard/edition, artifact marker, user-facing option, and implementation release. Track proposed, accepted/released, implemented, enabled-by-default, and interoperable separately. A stable standard does not establish implementation support. Date these distinctions and include them only when relevant to the book.

## Keep two small ledgers

Use JSON, CSV, or Markdown, whichever fits the work. These are working evidence records; relevant parts become the appendix and source bundle.

**Source register fields:** source ID; title/owner; URL or local path; source class; version/commit/edition/date; access date; exact locator; authority and role; limitations.

**Claim/figure ledger fields:** claim or figure ID; statement/value; units and conditions; source IDs and exact locators; specimen ID; evidence status; derivation/reproduction path; cross-check result; unresolved limitation.

Example structure (illustrative field names, not factual evidence):

```json
{
  "id": "C-014",
  "statement": "Result under the stated specimen and configuration",
  "status": "measured-here",
  "source_ids": ["S-02"],
  "locator": "named table, symbol, section, or record",
  "specimen_id": "A",
  "units": "explicit units",
  "method": "reproduce.py plus recorded parameters",
  "cross_check": "independent result and tolerance"
}
```

Keep source class separate from evidence status. A contemporary record, later scholarship, and reconstruction documentation have different authority even when each is directly inspected. Use evidence labels consistently:

- **Specified:** a normative requirement; name the standard and version.
- **Observed:** directly present in an inspected artifact, record, or implementation.
- **Measured here:** computed or measured in this run; preserve method and inputs.
- **Reported measurement:** another source's result, with attribution and conditions.
- **Derived:** calculated from stated premises; show units and intermediate steps.
- **Inferred:** reasoned interpretation; distinguish it from direct observation.
- **Schematic/constructed:** an explanatory example, not evidence about a population.
- **Unknown/unverified:** unresolved evidence gap that limits the conclusion.

Do not convert one specimen into a universal claim. Give the relevant sample size and selection method. Keep reported measurements separate from reruns, including date, environment, input, uncertainty, and changed conditions.

## Select specimens that teach differences

Use two complementary kinds of examples: recurring real cases that anchor the book, and small controlled demonstrations that isolate a difficult behavior. GGUF uses twelve varied public headers; Parquet centers on three real files plus generated tiny examples. The right number is the smallest set that covers the book's important mechanisms, contrasts, and boundaries.

Select cases by the questions they answer: a simple baseline, a one-variable contrast, a mainstream case, or a boundary/exception. One case can serve several roles. For a constructed example, retain its generator or construction method and explain what it isolates. A generated artifact can support observations about that artifact; its input distribution is not evidence of real-world prevalence.

Record a stable specimen ID, provenance, version/date, collected slice, acquisition parameters, and which claims it supports. Fetch bounded portions of large objects when possible. User-private evidence stays within the authorized task; final source bundles must not accidentally include secrets or unrelated private records.

## Comparisons when variants matter

Use a shared input, task, or question and record each variant's version, conditions, defaults, exposed controls, and result. Where identical conditions are impossible, explain the mismatch. Tie consequential table cells to precise sources and distinguish source-declared behavior from outputs actually observed. Keep “not exposed,” “not tested,” “not observed,” and “unsupported” distinct; an absent option alone proves none of the others.

Define measurement boundaries and denominators before comparing numbers: stored bytes, transferred bytes, and saved-byte percentage answer different questions. Preserve source environments and attribution when juxtaposing published results and your own reproduction. Trace the difference to a mechanism only as far as the evidence permits.

## Reproduce and cross-check

Preserve minimal input artifacts, source-linked notes, calculation scripts, derived datasets, and diagram inputs. Pin dependencies only where reproducing the result depends on them. Record exact commands/parameters and relevant environment details in a concise `MEASUREMENTS.md`.

For a hard mechanism, use a second independent implementation, a known test vector, a published result, or a domain invariant. Distinguish exact equality from a numerical tolerance. Check arithmetic in figure labels and table totals against the same derived data. A second rendering of the same algorithm is not an independent validation.

For performance claims, record sample count, units, conditions, and distribution when available. A one-off elapsed time can illustrate a trace but does not establish a general benchmark. For unavailable internals or sources, preserve the boundary and explain observable behavior without inventing the missing mechanism.

## Before drafting is final

Every central section should have a primary source and an inspectable example or an explicit reason why one is unavailable. Every important number should map through the ledger to evidence or derivation. Put material disagreements and gaps in the manuscript. Cite claims and figures locally, not only in a bibliography.

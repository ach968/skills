# Required self-improvement loop

Read at the START and execute at the END of EVERY nfl-deep-dd invocation.

## Before research
- Recover last accessible version, prior improvement logs and unresolved hypotheses; distinguish unavailable history.
- Create `improvement-log.md` in the dated working folder, noting run timestamp, subject, revision, baseline, sources available, expected pitfalls and a testable improvement hypothesis.
- Compare recent work against a known quality criterion (source freshness, injuries, market executable prices, uncertainty, reproducibility, calibration, efficiency).

## During research
- Timestamp inputs; preserve forecasts and prices *before* outcomes become available; log missing sources, disagreements, model seeds/data windows and decision changes.
- Test a concrete candidate fix against a baseline when possible. Quantitative model changes require chronological holdout/walk-forward validation and uncertainty reporting; use Brier/log loss for probabilities, MAE for volume predictions and compare calibration across many games. Workflow changes require a reproducible check (lint, independent source cross-check, verified arithmetic, automated tests, etc.). Don't count one favorable game as evidence of accuracy.

## Before final answer — mandatory gate
1. Complete the log, identify at least one evaluated hypothesis and assign ADOPT / REJECT / PENDING with justification, comparator, test results, side effects and rollback conditions.
2. Apply a minimal evidence-backed change to actual skill instructions, references or scripts ONLY if write permissions allow and the improvement is safe. Run tests and save file diff and revision; use reviewable commits/branches for repository edits. Never overwrite unexpected concurrent changes.
3. If write access is missing, store a reviewable proposed patch under the research folder's `improvements/`. If no safe useful change exists, record no-change and what evidence is needed.
4. Reflect on source coverage, data gaps, model accuracy (only when outcomes are known), market execution, contradicted theses, and prioritize unresolved learnings for next time.
5. The final response MUST contain a **Self-improvement audit** stating log path, evaluated hypothesis, decision, validation, and whether source changes were actually committed or only proposed.

Persist each run's evidence. Future runs must review these accumulated logs when accessible. Do not promise unattended updates across sessions or invent inaccessible past findings. No result-oriented betting strategy drift, data leakage, fabricated tests or unauthorized remote commits.

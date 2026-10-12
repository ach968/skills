---
name: nfl-deep-dd
description: Deep evidence-driven NFL pregame due diligence and retrospective analysis. Use for NFL matchup reports, injury/prop research, probability modeling, sportsbook or prediction-market mispricing, and updating research when lineups or odds change.
---

# NFL Deep Due Diligence

Build a falsifiable, source-traceable NFL dossier. Distinguish the football prediction from fair odds and executable prices. No forced bets, fabricated model runs, or unsupported confidence.

## Inputs and verification
Resolve teams, kickoff date/time/zone, season, venue, primary market or book, existing thesis, and relevant previous report. Verify with current official sources: schedule, personnel, QB, injury designations, expected weather, available market quotes, and precise contract rules. Explicitly distinguish game-time forecasts from current conditions, live prices from historical charts, and projected starters from confirmed starters. If kickoff has passed, perform a retrospective instead of offering stale pregame wagers.

## Persistent workspace
Immediately create a dated matchup folder with `README.md`, `00_progress.md`, `sources.md`, `research-log.md`, `data/`, `models/`, `scripts/`, `report.md`, `markets.csv`, and `postgame.md`, and `improvement-log.md`. Write findings throughout the run instead of only at completion; timestamp source access and record remaining unknowns, blockers, assumptions, and model limitations. Only claim files or agents exist after creating them.

## Workflow
1. **Baseline:** season and last-three/five-game trends with data windows and opposition/sample caveats. Examine early-down EPA/play and success, explosive rates, pass rate over expected, neutral pace, pressure and sack generation, blitz/coverage splits, run-block/run-defense metrics, red-zone and drive outcomes, turnovers/regression, penalties and special teams.
2. **Scheme and personnel:** QB pocket presence, OL versus DL, tackles versus edge rushers, coverage and receiver alignments, man/zone tendencies, linebackers/run fits, coaching adjustments and personnel groupings. Examine injury participation and credible beat reporting; estimate replacement quality and snap/route/target implications rather than relying on brand-name absences alone.
3. **Conditions:** home/away, travel, rest, short weeks, field/roof/wind/gusts/precipitation, and weather sensitivity. Do not double count risks that market prices already reflect.
4. **Competing scripts:** at least favorite-control, neutral, and underdog-control paths, with observable triggers, likely usage distributions, and counterarguments.
5. **Quantification:** fair probability ranges with sensitivity analysis. Use market-implied/no-vig priors plus independently estimated performance views. Run regression, drive-level simulation, Poisson/negative-binomial or Monte Carlo only when sourcing and calibration are defensible. Preserve scripts, parameters, seeds, sample sizes, and training/holdout choices; mark unexecuted simulations explicitly.
6. **Markets:** screen moneyline, spread, totals, team totals, player props, alternates and prediction-market contracts. Verify current executable bid/ask, timestamp, depth, fees, spreads and settlement rules. Compare fee-adjusted break-even to model interval, not to a single unjustifiably precise point estimate.
7. **Recommendations:** BET, WATCH or PASS. For every candidate include venue and exact proposition, fair probability range, market price, break-even, EV range, best entry or walkaway threshold, injury/market catalysts, counterthesis, liquidity and correlation caveats. PASS when edge cannot be verified.
8. **Adversarial audit:** actively challenge assumptions, opponent adjustments, injuries, look-ahead bias, data leaks, selection effects, small samples, double counting, correlation and stale information.
9. **Updates/postgame:** produce a dated diff to earlier reports; after the final result audit calibration, closing-line value, model errors and whether the decision was sound, without overreacting to a single result.

Read `references/self-improvement.md` at the start of every run. Read `references/methodology.md` and `references/markets.md` before market recommendations; use `templates/report.md`, `templates/markets.csv`, and `templates/postgame.md` for outputs. `scripts/market_math.py` provides basic checked arithmetic.

## Source hierarchy
Official NFL/team reports and gamebooks, established play-by-play/analytics data with clear definitions, directly observed actionable venue prices, weather agencies, trustworthy beat writers; social discussion is a corroboration lead, not proof. Document URLs, publication dates, observed timestamps, denominators and confidence. Do not launder public-money stories into causal evidence.

## Quality gate
Require verified event and lineup, scoped statistics, dated weather, actionable price, settlement rules, no-vig comparison, fees, uncertainty range, contradictions, correlations, liquidity and sources before calling a position an edge. Otherwise mark unconfirmed/WATCH/PASS.

## Prior research emphasis
Synthesize the SEA–SF, Cowboys–Buccaneers, Jets–Browns, Saints–Falcons and Sunday mispricing workflows: secondary/run-front matchups, pressure and pocket behavior, injury impacts, weather, prop usage, adversarial hypotheses and organized reproducible Markdown. Historical findings are examples, not reliable future priors.

## Mandatory continuous improvement (every invocation)
Every execution MUST (1) review accessible prior improvement logs and version, (2) initialize `improvement-log.md` before research, (3) identify and test or critically evaluate at least one concrete weakness in methods or execution, (4) assess results against a baseline without look-ahead leakage, (5) classify each proposed change ADOPT, REJECT or PENDING, (6) persist the log and, when authorized and justified, the smallest tested update to skill instructions/scripts, and (7) summarize the self-improvement audit and actual persistence status in the final report. Follow `references/self-improvement.md` and `templates/improvement-log.md`. This applies even for PASS decisions, postgame analyses and short updates. Never claim an improvement was deployed without an actual successful write; if source is read-only, save a proposed patch in the research workspace. Never modify the methodology merely because one wager won or lost.

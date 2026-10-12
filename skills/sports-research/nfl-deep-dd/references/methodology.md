# NFL research methodology

## Baseline matrix
Record season and rolling 3/5 game values, opponents, dates, definitions, sample sizes and source links for: EPA/play, early-down success, offensive/defensive DVOA or comparable adjusted efficiency if licensed, explosive rate, neutral pace, pass rate over expected, CPOE, pressure rate, pressure-to-sack conversion, run success, yards before/after contact, 3rd/4th-down conversions, red zone, drive efficiency, special teams and giveaways versus turnover-luck proxies. Do not splice incompatible provider definitions.

## Position-by-position review
- QB decision time, pressure handling, scrambles, blitz hot answers and deep accuracy versus actual defensive personnel.
- OL continuity, protection rules, tackles/guards versus named rushers, stunts and interior pressure.
- WR/TE roles, alignment, route rate and target share versus corner/safety leverage and man/zone matchups.
- Running backs, box counts, gap/zone tendencies, defensive line strength, linebacker health, early-down situation.
- Coaching, tempo, personnel deployment, scripted plays, game-state changes, rest and travel.

## Injuries
Track practice statuses by day and official inactive reports. Separate likely active, limited and out. Model replacement production, contingent snap share, effect on drives, pass protection and coverages, plus uncertainty. Identify late-news catalysts.

## Conditions and game scripts
Source venue, roof, surface, wind/gusts/precipitation and temperature; include forecast timestamp. Construct favorite-ahead, neutral and underdog-ahead scripts, each mapping to pace, pass volume, rush volume, receiver routes, coverage adjustments and turnover exposure.

## Model design
Start with a market/consensus prior; add independent team estimates only if grounded. Possible components: opponent-adjusted drive points, pace/play counts, dropbacks and targets, scoring dispersion. Choose distributions supported by event and sample: binomial for events, Poisson/negative-binomial for counts where appropriate, empirical bootstrap for player usage. Account for zero-inflation and overdispersion. Simulate correlated events jointly rather than treating every prop as independent. Record parameters, seeds, sample count and data provenance, plus holdout evaluation and sensitivity. Avoid presenting mechanically precise simulation frequencies as calibrated probabilities.

## Adversarial review
For each preferred contract, write strongest opposing case, data that would falsify the thesis, market consensus explanation, sample weakness, countervailing personnel effect, assumed correlation and price sensitivity. Separate real-world likelihood, contract payoff, trading execution and bankroll risk.

## Postgame
Audit ex ante availability and price, injury predictions, game scripts, closing-line value, realized vs forecast usage, sensitivity misses and calibration across *multiple games*. Update method only based on recurring evidence, not one noisy result.

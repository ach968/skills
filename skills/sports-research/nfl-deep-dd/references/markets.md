# Price research and market math

## Required market columns
Event/date/venue, contract and exact settlement language, platform/book, side, observed UTC timestamp, displayed quote, executable bid/ask, order size/depth, currency, fees, slippage, implied probability, de-vigged comparison, model estimate and interval, expected value, action, maximum entry price, confidence and source URL.

For American odds: positive +A implies break-even 100/(A+100), negative -A implies break-even A/(A+100). Decimal d implies 1/d. In two-sided sportsbook markets with overround, remove vig only when sides and timestamp are comparable; a basic proportional no-vig estimate is p_i/(sum_j p_j).

For a binary share priced c, payout $1 on success: gross expected profit per share is p-c. Net cost and net payout depend on venue-specific fees and settlement conventions. With buy fee f and effective settlement fee s on winning proceeds, approximate net expected P&L as p*(1-s)-(c+f), **only** if those fee bases apply. Recalculate for the actual fee rules and execution route. Break-even p=(c+f)/(1-s) in that simplified fee model. Observe spread, order depth, slippage and execution probability; an attractive last trade is not necessarily an obtainable quote.

Compare probability ranges, not just point estimates. A forecast crossing the market break-even at plausible inputs is WATCH, not a confirmed edge. Record the maximum fee-inclusive entry price at which the conservative model case clears the user's required edge threshold.

No-vig estimated bookmaker probability is a market anchor, not a clean causal independent label. Avoid counting correlated picks as separate independent edge. Do not equate betting handle/fading public money with profitable prediction without tested evidence.

For Polymarket and similar exchanges, verify the correct chain/token, YES/NO side, outcome wording, void rules, prices for the actual order size, trade fees and available liquidity before recommending any position. No order placement unless separately authorized.

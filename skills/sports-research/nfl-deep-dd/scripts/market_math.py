#!/usr/bin/env python3
"""Minimal dependency-free research math. These helpers do not source market data."""
def american_probability(odds: int) -> float:
    if odds == 0: raise ValueError("American odds cannot be zero")
    return 100 / (odds + 100) if odds > 0 else -odds / (100 - odds)

def decimal_probability(odds: float) -> float:
    if odds <= 1: raise ValueError("Decimal odds must exceed 1")
    return 1 / odds

def no_vig(*implied: float) -> tuple[float, ...]:
    if not implied or any(not 0 < p <= 1 for p in implied):
        raise ValueError("Probabilities must be between 0 and 1")
    total = sum(implied)
    return tuple(p / total for p in implied)

def binary_ev(prob: float, cost: float, fee: float = 0.0, settlement_fee_fraction: float = 0.0) -> float:
    if not (0 <= prob <= 1 and 0 <= cost <= 1 and fee >= 0 and 0 <= settlement_fee_fraction < 1):
        raise ValueError("Invalid inputs")
    return prob * (1 - settlement_fee_fraction) - cost - fee

def binary_break_even(cost: float, fee: float = 0.0, settlement_fee_fraction: float = 0.0) -> float:
    if not (0 <= cost <= 1 and fee >= 0 and 0 <= settlement_fee_fraction < 1):
        raise ValueError("Invalid inputs")
    return (cost + fee) / (1 - settlement_fee_fraction)

if __name__ == "__main__":
    assert abs(american_probability(150) - .4) < 1e-12
    assert abs(american_probability(-150) - .6) < 1e-12
    assert abs(binary_ev(.6, .5) - .1) < 1e-12
    assert abs(sum(no_vig(.55,.5)) - 1) < 1e-12
    print("market_math self-tests passed")

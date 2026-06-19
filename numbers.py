"""Numeric utility helpers."""


def safe_div(numerator: float, denominator: float) -> float | None:
    """Divide numerator by denominator, returning None on zero denominator."""
    if denominator == 0:
        return None
    return numerator / denominator


def clamp(value: float, lo: float, hi: float) -> float:
    """Clamp value into the inclusive range [lo, hi]."""
    if lo > hi:
        raise ValueError("lo must be <= hi")
    if value < lo:
        return lo
    if value > hi:
        return hi
    return value


def round_to_sig_figs(value: float, sig_figs: int) -> float:
    """Round value to the given number of significant figures."""
    if sig_figs < 1:
        raise ValueError("sig_figs must be >= 1")
    if value == 0:
        return 0.0
    from math import floor, log10

    magnitude = floor(log10(abs(value)))
    factor = 10 ** (sig_figs - 1 - magnitude)
    return round(value * factor) / factor

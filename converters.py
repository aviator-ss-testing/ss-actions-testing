"""Unit conversion utilities for temperature, distance, and weight."""


def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9


def km_to_miles(km: float) -> float:
    """Convert kilometers to miles."""
    return km * 0.621371


def miles_to_km(miles: float) -> float:
    """Convert miles to kilometers."""
    return miles * 1.60934


def pounds_to_kg(pounds: float) -> float:
    """Convert pounds to kilograms."""
    return pounds * 0.453592


def kg_to_pounds(kg: float) -> float:
    """Convert kilograms to pounds."""
    return kg / 0.453592

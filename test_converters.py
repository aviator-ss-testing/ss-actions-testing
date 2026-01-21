"""Tests for the converters module."""
import pytest
from converters import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    km_to_miles,
    miles_to_km,
    pounds_to_kg,
    kg_to_pounds,
)


def test_celsius_to_fahrenheit():
    """Test Celsius to Fahrenheit conversion."""
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(37) == pytest.approx(98.6, rel=1e-2)


def test_fahrenheit_to_celsius():
    """Test Fahrenheit to Celsius conversion."""
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40
    assert fahrenheit_to_celsius(98.6) == pytest.approx(37, rel=1e-2)


def test_km_to_miles():
    """Test kilometers to miles conversion."""
    assert km_to_miles(0) == 0
    assert km_to_miles(1) == pytest.approx(0.621371, rel=1e-4)
    assert km_to_miles(1.60934) == pytest.approx(1, rel=1e-3)
    assert km_to_miles(100) == pytest.approx(62.1371, rel=1e-4)


def test_miles_to_km():
    """Test miles to kilometers conversion."""
    assert miles_to_km(0) == 0
    assert miles_to_km(1) == pytest.approx(1.60934, rel=1e-4)
    assert miles_to_km(0.621371) == pytest.approx(1, rel=1e-3)
    assert miles_to_km(100) == pytest.approx(160.934, rel=1e-4)


def test_pounds_to_kg():
    """Test pounds to kilograms conversion."""
    assert pounds_to_kg(0) == 0
    assert pounds_to_kg(1) == pytest.approx(0.453592, rel=1e-4)
    assert pounds_to_kg(2.20462) == pytest.approx(1, rel=1e-3)
    assert pounds_to_kg(100) == pytest.approx(45.3592, rel=1e-4)


def test_kg_to_pounds():
    """Test kilograms to pounds conversion."""
    assert kg_to_pounds(0) == 0
    assert kg_to_pounds(1) == pytest.approx(2.20462, rel=1e-4)
    assert kg_to_pounds(0.453592) == pytest.approx(1, rel=1e-3)
    assert kg_to_pounds(100) == pytest.approx(220.462, rel=1e-4)

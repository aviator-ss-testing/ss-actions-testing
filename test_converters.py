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
    assert pytest.approx(celsius_to_fahrenheit(37), rel=1e-3) == 98.6


def test_fahrenheit_to_celsius():
    """Test Fahrenheit to Celsius conversion."""
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40
    assert pytest.approx(fahrenheit_to_celsius(98.6), rel=1e-3) == 37


def test_km_to_miles():
    """Test kilometers to miles conversion."""
    assert km_to_miles(0) == 0
    assert pytest.approx(km_to_miles(1), rel=1e-3) == 0.621371
    assert pytest.approx(km_to_miles(10), rel=1e-3) == 6.21371
    assert pytest.approx(km_to_miles(1.60934), rel=1e-3) == 1.0


def test_miles_to_km():
    """Test miles to kilometers conversion."""
    assert miles_to_km(0) == 0
    assert pytest.approx(miles_to_km(1), rel=1e-3) == 1.60934
    assert pytest.approx(miles_to_km(10), rel=1e-3) == 16.0934
    assert pytest.approx(miles_to_km(0.621371), rel=1e-3) == 1.0


def test_pounds_to_kg():
    """Test pounds to kilograms conversion."""
    assert pounds_to_kg(0) == 0
    assert pytest.approx(pounds_to_kg(1), rel=1e-3) == 0.453592
    assert pytest.approx(pounds_to_kg(2.20462), rel=1e-3) == 1.0
    assert pytest.approx(pounds_to_kg(100), rel=1e-3) == 45.3592


def test_kg_to_pounds():
    """Test kilograms to pounds conversion."""
    assert kg_to_pounds(0) == 0
    assert pytest.approx(kg_to_pounds(1), rel=1e-3) == 2.20462
    assert pytest.approx(kg_to_pounds(0.453592), rel=1e-3) == 1.0
    assert pytest.approx(kg_to_pounds(100), rel=1e-3) == 220.462


def test_temperature_roundtrip():
    """Test that converting back and forth returns original value."""
    for temp in [-40, 0, 25, 37, 100]:
        assert pytest.approx(fahrenheit_to_celsius(celsius_to_fahrenheit(temp)), rel=1e-9) == temp
        assert pytest.approx(celsius_to_fahrenheit(fahrenheit_to_celsius(temp)), rel=1e-9) == temp


def test_distance_roundtrip():
    """Test that converting back and forth returns original value."""
    for dist in [0, 1, 10, 100]:
        assert pytest.approx(miles_to_km(km_to_miles(dist)), rel=1e-3) == dist
        assert pytest.approx(km_to_miles(miles_to_km(dist)), rel=1e-3) == dist


def test_weight_roundtrip():
    """Test that converting back and forth returns original value."""
    for weight in [0, 1, 10, 100]:
        assert pytest.approx(kg_to_pounds(pounds_to_kg(weight)), rel=1e-3) == weight
        assert pytest.approx(pounds_to_kg(kg_to_pounds(weight)), rel=1e-3) == weight

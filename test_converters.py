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
    assert abs(celsius_to_fahrenheit(37) - 98.6) < 0.01


def test_fahrenheit_to_celsius():
    """Test Fahrenheit to Celsius conversion."""
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert fahrenheit_to_celsius(-40) == -40
    assert abs(fahrenheit_to_celsius(98.6) - 37) < 0.01


def test_km_to_miles():
    """Test kilometers to miles conversion."""
    assert abs(km_to_miles(1) - 0.621371) < 0.000001
    assert abs(km_to_miles(5) - 3.106855) < 0.000001
    assert abs(km_to_miles(10) - 6.21371) < 0.00001
    assert km_to_miles(0) == 0


def test_miles_to_km():
    """Test miles to kilometers conversion."""
    assert abs(miles_to_km(1) - 1.609344) < 0.000001
    assert abs(miles_to_km(5) - 8.04672) < 0.00001
    assert abs(miles_to_km(10) - 16.09344) < 0.00001
    assert miles_to_km(0) == 0


def test_pounds_to_kg():
    """Test pounds to kilograms conversion."""
    assert abs(pounds_to_kg(1) - 0.453592) < 0.000001
    assert abs(pounds_to_kg(10) - 4.53592) < 0.00001
    assert abs(pounds_to_kg(100) - 45.3592) < 0.0001
    assert pounds_to_kg(0) == 0


def test_kg_to_pounds():
    """Test kilograms to pounds conversion."""
    assert abs(kg_to_pounds(1) - 2.204623) < 0.00001
    assert abs(kg_to_pounds(10) - 22.04623) < 0.0001
    assert abs(kg_to_pounds(100) - 220.4623) < 0.001
    assert kg_to_pounds(0) == 0


def test_temperature_round_trip():
    """Test that converting back and forth returns original value."""
    temp_c = 25
    assert abs(fahrenheit_to_celsius(celsius_to_fahrenheit(temp_c)) - temp_c) < 0.000001


def test_distance_round_trip():
    """Test that converting back and forth returns original value."""
    dist_km = 42
    assert abs(miles_to_km(km_to_miles(dist_km)) - dist_km) < 0.000001


def test_weight_round_trip():
    """Test that converting back and forth returns original value."""
    weight_kg = 70
    assert abs(pounds_to_kg(kg_to_pounds(weight_kg)) - weight_kg) < 0.000001

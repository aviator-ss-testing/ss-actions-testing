"""
Math utilities package providing various mathematical operations.

This package includes:
- arithmetic: Basic arithmetic operations (add, multiply, power, factorial, gcd, lcm)
- statistics: Statistical functions (mean, median, mode, variance, standard_deviation)
- geometry: Geometric calculations (circle, rectangle, triangle areas and perimeters)
- decorators: Utility decorators (memoize, validate_positive, validate_numeric, timer)
"""

__version__ = "0.1.0"

from math_utils.arithmetic import add, multiply, power, factorial, gcd, lcm
from math_utils.statistics import mean, median, mode, variance, standard_deviation
from math_utils.geometry import (
    circle_area,
    circle_circumference,
    rectangle_area,
    rectangle_perimeter,
    triangle_area,
    pythagorean,
)
from math_utils.decorators import memoize, validate_positive, validate_numeric, timer

__all__ = [
    "add",
    "multiply",
    "power",
    "factorial",
    "gcd",
    "lcm",
    "mean",
    "median",
    "mode",
    "variance",
    "standard_deviation",
    "circle_area",
    "circle_circumference",
    "rectangle_area",
    "rectangle_perimeter",
    "triangle_area",
    "pythagorean",
    "memoize",
    "validate_positive",
    "validate_numeric",
    "timer",
]

"""
Geometry utilities module.

This module provides geometric calculation functions for areas, perimeters,
distances, and other geometric computations with proper input validation
and error handling.
"""

import math
from typing import Union, Tuple

Number = Union[int, float]


def area_circle(radius: Number) -> float:
    """
    Calculate the area of a circle.

    Args:
        radius: Radius of the circle (int or float)

    Returns:
        float: Area of the circle

    Raises:
        ValueError: If radius is negative
        TypeError: If radius is not a number
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")

    return math.pi * radius * radius


def area_rectangle(length: Number, width: Number) -> float:
    """
    Calculate the area of a rectangle.

    Args:
        length: Length of the rectangle (int or float)
        width: Width of the rectangle (int or float)

    Returns:
        float: Area of the rectangle

    Raises:
        ValueError: If length or width is negative
        TypeError: If length or width is not a number
    """
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Length and width must be numbers")
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative")

    return float(length * width)


def area_triangle(base: Number, height: Number) -> float:
    """
    Calculate the area of a triangle.

    Args:
        base: Base of the triangle (int or float)
        height: Height of the triangle (int or float)

    Returns:
        float: Area of the triangle

    Raises:
        ValueError: If base or height is negative
        TypeError: If base or height is not a number
    """
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Base and height must be numbers")
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative")

    return float(base * height / 2)


def perimeter_circle(radius: Number) -> float:
    """
    Calculate the perimeter (circumference) of a circle.

    Args:
        radius: Radius of the circle (int or float)

    Returns:
        float: Perimeter of the circle

    Raises:
        ValueError: If radius is negative
        TypeError: If radius is not a number
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")

    return 2 * math.pi * radius


def perimeter_rectangle(length: Number, width: Number) -> float:
    """
    Calculate the perimeter of a rectangle.

    Args:
        length: Length of the rectangle (int or float)
        width: Width of the rectangle (int or float)

    Returns:
        float: Perimeter of the rectangle

    Raises:
        ValueError: If length or width is negative
        TypeError: If length or width is not a number
    """
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Length and width must be numbers")
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative")

    return float(2 * (length + width))


def perimeter_triangle(side1: Number, side2: Number, side3: Number) -> float:
    """
    Calculate the perimeter of a triangle.

    Args:
        side1: First side of the triangle (int or float)
        side2: Second side of the triangle (int or float)
        side3: Third side of the triangle (int or float)

    Returns:
        float: Perimeter of the triangle

    Raises:
        ValueError: If any side is negative or if sides don't form a valid triangle
        TypeError: If any side is not a number
    """
    if not all(isinstance(side, (int, float)) for side in [side1, side2, side3]):
        raise TypeError("All sides must be numbers")
    if any(side < 0 for side in [side1, side2, side3]):
        raise ValueError("Sides cannot be negative")
    if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
        raise ValueError("Sides do not form a valid triangle")

    return float(side1 + side2 + side3)


def distance_between_points(x1: Number, y1: Number, x2: Number, y2: Number) -> float:
    """
    Calculate the distance between two points in 2D space.

    Args:
        x1: X coordinate of the first point (int or float)
        y1: Y coordinate of the first point (int or float)
        x2: X coordinate of the second point (int or float)
        y2: Y coordinate of the second point (int or float)

    Returns:
        float: Distance between the two points

    Raises:
        TypeError: If any coordinate is not a number
    """
    if not all(isinstance(coord, (int, float)) for coord in [x1, y1, x2, y2]):
        raise TypeError("All coordinates must be numbers")

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def pythagorean_theorem(a: Number, b: Number) -> float:
    """
    Calculate the hypotenuse of a right triangle using the Pythagorean theorem.

    Args:
        a: Length of the first side (int or float)
        b: Length of the second side (int or float)

    Returns:
        float: Length of the hypotenuse

    Raises:
        ValueError: If any side is negative
        TypeError: If any side is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both sides must be numbers")
    if a < 0 or b < 0:
        raise ValueError("Sides cannot be negative")

    return math.sqrt(a * a + b * b)
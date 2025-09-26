"""
Geometric calculations utility module.

This module provides functions for calculating areas and distances in geometric shapes.
"""

import math
from typing import Union


def circle_area(radius: Union[int, float]) -> float:
    """
    Calculate the area of a circle.

    Args:
        radius: The radius of the circle

    Returns:
        The area of the circle

    Raises:
        ValueError: If radius is negative
        TypeError: If radius is not a number
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


def rectangle_area(length: Union[int, float], width: Union[int, float]) -> float:
    """
    Calculate the area of a rectangle.

    Args:
        length: The length of the rectangle
        width: The width of the rectangle

    Returns:
        The area of the rectangle

    Raises:
        ValueError: If length or width is negative
        TypeError: If length or width is not a number
    """
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Length and width must be numbers")
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative")
    return length * width


def triangle_area(base: Union[int, float], height: Union[int, float]) -> float:
    """
    Calculate the area of a triangle.

    Args:
        base: The base of the triangle
        height: The height of the triangle

    Returns:
        The area of the triangle

    Raises:
        ValueError: If base or height is negative
        TypeError: If base or height is not a number
    """
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Base and height must be numbers")
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative")
    return 0.5 * base * height


def pythagorean_theorem(a: Union[int, float], b: Union[int, float]) -> float:
    """
    Calculate the hypotenuse of a right triangle using the Pythagorean theorem.

    Args:
        a: Length of one side of the triangle
        b: Length of the other side of the triangle

    Returns:
        The length of the hypotenuse

    Raises:
        ValueError: If a or b is negative
        TypeError: If a or b is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both sides must be numbers")
    if a < 0 or b < 0:
        raise ValueError("Triangle sides cannot be negative")
    return math.sqrt(a ** 2 + b ** 2)
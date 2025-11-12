"""
Geometry utilities for basic geometric calculations.

This module provides functions for calculating areas, perimeters, and other
geometric properties of common shapes like circles, rectangles, and triangles.
"""

import math


def circle_area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius: The radius of the circle (must be positive)

    Returns:
        float: The area of the circle (π * r²)

    Raises:
        ValueError: If radius is not positive

    Examples:
        >>> circle_area(5)
        78.53981633974483
        >>> circle_area(1)
        3.141592653589793
    """
    if radius <= 0:
        raise ValueError("Radius must be positive")
    return math.pi * radius ** 2


def circle_circumference(radius):
    """
    Calculate the circumference of a circle.

    Args:
        radius: The radius of the circle (must be positive)

    Returns:
        float: The circumference of the circle (2 * π * r)

    Raises:
        ValueError: If radius is not positive

    Examples:
        >>> circle_circumference(5)
        31.41592653589793
        >>> circle_circumference(1)
        6.283185307179586
    """
    if radius <= 0:
        raise ValueError("Radius must be positive")
    return 2 * math.pi * radius


def rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length: The length of the rectangle (must be positive)
        width: The width of the rectangle (must be positive)

    Returns:
        float: The area of the rectangle (length * width)

    Raises:
        ValueError: If length or width is not positive

    Examples:
        >>> rectangle_area(5, 3)
        15
        >>> rectangle_area(10.5, 2.5)
        26.25
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive")
    return length * width


def rectangle_perimeter(length, width):
    """
    Calculate the perimeter of a rectangle.

    Args:
        length: The length of the rectangle (must be positive)
        width: The width of the rectangle (must be positive)

    Returns:
        float: The perimeter of the rectangle (2 * (length + width))

    Raises:
        ValueError: If length or width is not positive

    Examples:
        >>> rectangle_perimeter(5, 3)
        16
        >>> rectangle_perimeter(10.5, 2.5)
        26.0
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive")
    return 2 * (length + width)


def triangle_area(base, height):
    """
    Calculate the area of a triangle.

    Args:
        base: The base of the triangle (must be positive)
        height: The height of the triangle (must be positive)

    Returns:
        float: The area of the triangle (0.5 * base * height)

    Raises:
        ValueError: If base or height is not positive

    Examples:
        >>> triangle_area(4, 3)
        6.0
        >>> triangle_area(10, 5)
        25.0
    """
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive")
    return 0.5 * base * height


def pythagorean(a, b):
    """
    Calculate the hypotenuse of a right triangle using the Pythagorean theorem.

    Args:
        a: Length of one side of the right triangle (must be positive)
        b: Length of the other side of the right triangle (must be positive)

    Returns:
        float: The length of the hypotenuse (√(a² + b²))

    Raises:
        ValueError: If a or b is not positive

    Examples:
        >>> pythagorean(3, 4)
        5.0
        >>> pythagorean(5, 12)
        13.0
        >>> pythagorean(1, 1)
        1.4142135623730951
    """
    if a <= 0 or b <= 0:
        raise ValueError("Both sides must be positive")
    return math.sqrt(a ** 2 + b ** 2)

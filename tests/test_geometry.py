"""
Comprehensive test suite for geometry module.

Tests all geometric functions including area calculations, perimeter calculations,
distance calculations, edge cases, error conditions, and mathematical property validations.
"""

import pytest
import math
from src.geometry import (
    area_circle, area_rectangle, area_triangle,
    perimeter_circle, perimeter_rectangle, perimeter_triangle,
    distance_between_points, pythagorean_theorem
)


class TestAreaCircle:
    """Test cases for area_circle function."""

    def test_area_circle_basic(self):
        # Area = π * r²
        assert abs(area_circle(1) - math.pi) < 1e-10
        assert abs(area_circle(2) - 4 * math.pi) < 1e-10
        assert abs(area_circle(5) - 25 * math.pi) < 1e-10

    def test_area_circle_zero_radius(self):
        assert area_circle(0) == 0.0

    def test_area_circle_float_radius(self):
        result = area_circle(2.5)
        expected = math.pi * 2.5 * 2.5
        assert abs(result - expected) < 1e-10

    def test_area_circle_large_radius(self):
        result = area_circle(1000)
        expected = math.pi * 1000000
        assert abs(result - expected) < 1e-5

    def test_area_circle_negative_radius(self):
        with pytest.raises(ValueError, match="Radius cannot be negative"):
            area_circle(-1)
        with pytest.raises(ValueError, match="Radius cannot be negative"):
            area_circle(-0.5)

    def test_area_circle_non_numeric(self):
        with pytest.raises(TypeError, match="Radius must be a number"):
            area_circle("5")
        with pytest.raises(TypeError, match="Radius must be a number"):
            area_circle(None)


class TestAreaRectangle:
    """Test cases for area_rectangle function."""

    def test_area_rectangle_basic(self):
        assert area_rectangle(3, 4) == 12.0
        assert area_rectangle(5, 2) == 10.0
        assert area_rectangle(10, 10) == 100.0

    def test_area_rectangle_zero_dimensions(self):
        assert area_rectangle(0, 5) == 0.0
        assert area_rectangle(5, 0) == 0.0
        assert area_rectangle(0, 0) == 0.0

    def test_area_rectangle_float_dimensions(self):
        result = area_rectangle(2.5, 3.2)
        expected = 2.5 * 3.2
        assert abs(result - expected) < 1e-10

    def test_area_rectangle_square(self):
        # Square is a special case of rectangle
        assert area_rectangle(4, 4) == 16.0

    def test_area_rectangle_negative_dimensions(self):
        with pytest.raises(ValueError, match="Length and width cannot be negative"):
            area_rectangle(-1, 5)
        with pytest.raises(ValueError, match="Length and width cannot be negative"):
            area_rectangle(5, -1)
        with pytest.raises(ValueError, match="Length and width cannot be negative"):
            area_rectangle(-2, -3)

    def test_area_rectangle_non_numeric(self):
        with pytest.raises(TypeError, match="Length and width must be numbers"):
            area_rectangle("5", 3)
        with pytest.raises(TypeError, match="Length and width must be numbers"):
            area_rectangle(5, "3")
        with pytest.raises(TypeError, match="Length and width must be numbers"):
            area_rectangle(None, 5)


class TestAreaTriangle:
    """Test cases for area_triangle function."""

    def test_area_triangle_basic(self):
        # Area = 0.5 * base * height
        assert area_triangle(4, 3) == 6.0
        assert area_triangle(10, 5) == 25.0
        assert area_triangle(2, 8) == 8.0

    def test_area_triangle_zero_dimensions(self):
        assert area_triangle(0, 5) == 0.0
        assert area_triangle(5, 0) == 0.0
        assert area_triangle(0, 0) == 0.0

    def test_area_triangle_float_dimensions(self):
        result = area_triangle(3.5, 2.4)
        expected = 3.5 * 2.4 / 2
        assert abs(result - expected) < 1e-10

    def test_area_triangle_right_triangle(self):
        # For a 3-4-5 right triangle with base=4, height=3
        assert area_triangle(4, 3) == 6.0

    def test_area_triangle_negative_dimensions(self):
        with pytest.raises(ValueError, match="Base and height cannot be negative"):
            area_triangle(-1, 5)
        with pytest.raises(ValueError, match="Base and height cannot be negative"):
            area_triangle(5, -1)
        with pytest.raises(ValueError, match="Base and height cannot be negative"):
            area_triangle(-2, -3)

    def test_area_triangle_non_numeric(self):
        with pytest.raises(TypeError, match="Base and height must be numbers"):
            area_triangle("5", 3)
        with pytest.raises(TypeError, match="Base and height must be numbers"):
            area_triangle(5, "3")


class TestPerimeterCircle:
    """Test cases for perimeter_circle function."""

    def test_perimeter_circle_basic(self):
        # Circumference = 2 * π * r
        assert abs(perimeter_circle(1) - 2 * math.pi) < 1e-10
        assert abs(perimeter_circle(2) - 4 * math.pi) < 1e-10
        assert abs(perimeter_circle(3) - 6 * math.pi) < 1e-10

    def test_perimeter_circle_zero_radius(self):
        assert perimeter_circle(0) == 0.0

    def test_perimeter_circle_float_radius(self):
        result = perimeter_circle(1.5)
        expected = 2 * math.pi * 1.5
        assert abs(result - expected) < 1e-10

    def test_perimeter_circle_large_radius(self):
        result = perimeter_circle(1000)
        expected = 2000 * math.pi
        assert abs(result - expected) < 1e-5

    def test_perimeter_circle_negative_radius(self):
        with pytest.raises(ValueError, match="Radius cannot be negative"):
            perimeter_circle(-1)

    def test_perimeter_circle_non_numeric(self):
        with pytest.raises(TypeError, match="Radius must be a number"):
            perimeter_circle("5")


class TestPerimeterRectangle:
    """Test cases for perimeter_rectangle function."""

    def test_perimeter_rectangle_basic(self):
        # Perimeter = 2 * (length + width)
        assert perimeter_rectangle(3, 4) == 14.0
        assert perimeter_rectangle(5, 2) == 14.0
        assert perimeter_rectangle(10, 1) == 22.0

    def test_perimeter_rectangle_zero_dimensions(self):
        assert perimeter_rectangle(0, 5) == 10.0
        assert perimeter_rectangle(5, 0) == 10.0
        assert perimeter_rectangle(0, 0) == 0.0

    def test_perimeter_rectangle_square(self):
        assert perimeter_rectangle(4, 4) == 16.0
        assert perimeter_rectangle(7, 7) == 28.0

    def test_perimeter_rectangle_float_dimensions(self):
        result = perimeter_rectangle(2.5, 3.5)
        expected = 2 * (2.5 + 3.5)
        assert abs(result - expected) < 1e-10

    def test_perimeter_rectangle_negative_dimensions(self):
        with pytest.raises(ValueError, match="Length and width cannot be negative"):
            perimeter_rectangle(-1, 5)
        with pytest.raises(ValueError, match="Length and width cannot be negative"):
            perimeter_rectangle(5, -1)

    def test_perimeter_rectangle_non_numeric(self):
        with pytest.raises(TypeError, match="Length and width must be numbers"):
            perimeter_rectangle("5", 3)
        with pytest.raises(TypeError, match="Length and width must be numbers"):
            perimeter_rectangle(5, "3")


class TestPerimeterTriangle:
    """Test cases for perimeter_triangle function."""

    def test_perimeter_triangle_basic(self):
        assert perimeter_triangle(3, 4, 5) == 12.0
        assert perimeter_triangle(1, 1, 1) == 3.0
        assert perimeter_triangle(2, 3, 4) == 9.0

    def test_perimeter_triangle_equilateral(self):
        assert perimeter_triangle(5, 5, 5) == 15.0

    def test_perimeter_triangle_isosceles(self):
        assert perimeter_triangle(5, 5, 6) == 16.0
        assert perimeter_triangle(3, 4, 4) == 11.0

    def test_perimeter_triangle_right_triangle(self):
        # 3-4-5 right triangle
        assert perimeter_triangle(3, 4, 5) == 12.0

    def test_perimeter_triangle_float_sides(self):
        result = perimeter_triangle(2.5, 3.7, 4.1)
        expected = 2.5 + 3.7 + 4.1
        assert abs(result - expected) < 1e-10

    def test_perimeter_triangle_zero_sides(self):
        # Zero sides don't form valid triangles
        with pytest.raises(ValueError, match="Sides do not form a valid triangle"):
            perimeter_triangle(0, 1, 1)
        with pytest.raises(ValueError, match="Sides do not form a valid triangle"):
            perimeter_triangle(1, 0, 1)
        with pytest.raises(ValueError, match="Sides do not form a valid triangle"):
            perimeter_triangle(1, 1, 0)

    def test_perimeter_triangle_negative_sides(self):
        with pytest.raises(ValueError, match="Sides cannot be negative"):
            perimeter_triangle(-1, 3, 4)
        with pytest.raises(ValueError, match="Sides cannot be negative"):
            perimeter_triangle(3, -1, 4)
        with pytest.raises(ValueError, match="Sides cannot be negative"):
            perimeter_triangle(3, 4, -1)

    def test_perimeter_triangle_invalid_triangle(self):
        # Triangle inequality: sum of any two sides must be greater than third side
        with pytest.raises(ValueError, match="Sides do not form a valid triangle"):
            perimeter_triangle(1, 2, 5)  # 1 + 2 = 3 < 5
        with pytest.raises(ValueError, match="Sides do not form a valid triangle"):
            perimeter_triangle(10, 1, 1)  # 1 + 1 = 2 < 10
        with pytest.raises(ValueError, match="Sides do not form a valid triangle"):
            perimeter_triangle(1, 10, 1)  # 1 + 1 = 2 < 10

    def test_perimeter_triangle_edge_case_valid(self):
        # Edge case: sum equals third side (degenerate triangle)
        with pytest.raises(ValueError, match="Sides do not form a valid triangle"):
            perimeter_triangle(1, 2, 3)  # 1 + 2 = 3

    def test_perimeter_triangle_non_numeric(self):
        with pytest.raises(TypeError, match="All sides must be numbers"):
            perimeter_triangle("3", 4, 5)
        with pytest.raises(TypeError, match="All sides must be numbers"):
            perimeter_triangle(3, "4", 5)
        with pytest.raises(TypeError, match="All sides must be numbers"):
            perimeter_triangle(3, 4, "5")


class TestDistanceBetweenPoints:
    """Test cases for distance_between_points function."""

    def test_distance_basic(self):
        # Distance from origin to (3,4) should be 5
        result = distance_between_points(0, 0, 3, 4)
        assert abs(result - 5.0) < 1e-10

    def test_distance_same_point(self):
        assert distance_between_points(1, 1, 1, 1) == 0.0
        assert distance_between_points(0, 0, 0, 0) == 0.0

    def test_distance_horizontal(self):
        # Distance between (1,0) and (4,0) should be 3
        assert distance_between_points(1, 0, 4, 0) == 3.0

    def test_distance_vertical(self):
        # Distance between (0,1) and (0,5) should be 4
        assert distance_between_points(0, 1, 0, 5) == 4.0

    def test_distance_negative_coordinates(self):
        result = distance_between_points(-1, -1, 2, 3)
        expected = math.sqrt((2 - (-1))**2 + (3 - (-1))**2)
        assert abs(result - expected) < 1e-10

    def test_distance_float_coordinates(self):
        result = distance_between_points(1.5, 2.5, 4.5, 6.5)
        expected = math.sqrt((4.5 - 1.5)**2 + (6.5 - 2.5)**2)
        assert abs(result - expected) < 1e-10

    def test_distance_large_coordinates(self):
        result = distance_between_points(0, 0, 1000, 1000)
        expected = math.sqrt(2000000)
        assert abs(result - expected) < 1e-5

    def test_distance_symmetry(self):
        # Distance from A to B should equal distance from B to A
        dist1 = distance_between_points(1, 2, 5, 7)
        dist2 = distance_between_points(5, 7, 1, 2)
        assert abs(dist1 - dist2) < 1e-10

    def test_distance_non_numeric(self):
        with pytest.raises(TypeError, match="All coordinates must be numbers"):
            distance_between_points("1", 2, 3, 4)
        with pytest.raises(TypeError, match="All coordinates must be numbers"):
            distance_between_points(1, "2", 3, 4)
        with pytest.raises(TypeError, match="All coordinates must be numbers"):
            distance_between_points(1, 2, "3", 4)
        with pytest.raises(TypeError, match="All coordinates must be numbers"):
            distance_between_points(1, 2, 3, "4")


class TestPythagoreanTheorem:
    """Test cases for pythagorean_theorem function."""

    def test_pythagorean_basic(self):
        # 3-4-5 right triangle
        result = pythagorean_theorem(3, 4)
        assert abs(result - 5.0) < 1e-10

    def test_pythagorean_equal_sides(self):
        # 45-45-90 triangle
        result = pythagorean_theorem(1, 1)
        expected = math.sqrt(2)
        assert abs(result - expected) < 1e-10

    def test_pythagorean_zero_side(self):
        assert pythagorean_theorem(0, 3) == 3.0
        assert pythagorean_theorem(5, 0) == 5.0
        assert pythagorean_theorem(0, 0) == 0.0

    def test_pythagorean_float_sides(self):
        result = pythagorean_theorem(1.5, 2.0)
        expected = math.sqrt(1.5**2 + 2.0**2)
        assert abs(result - expected) < 1e-10

    def test_pythagorean_large_numbers(self):
        result = pythagorean_theorem(100, 100)
        expected = 100 * math.sqrt(2)
        assert abs(result - expected) < 1e-10

    def test_pythagorean_common_triangles(self):
        # Test other common Pythagorean triples
        assert abs(pythagorean_theorem(5, 12) - 13.0) < 1e-10
        assert abs(pythagorean_theorem(8, 15) - 17.0) < 1e-10
        assert abs(pythagorean_theorem(7, 24) - 25.0) < 1e-10

    def test_pythagorean_negative_sides(self):
        with pytest.raises(ValueError, match="Sides cannot be negative"):
            pythagorean_theorem(-1, 3)
        with pytest.raises(ValueError, match="Sides cannot be negative"):
            pythagorean_theorem(3, -1)
        with pytest.raises(ValueError, match="Sides cannot be negative"):
            pythagorean_theorem(-1, -1)

    def test_pythagorean_non_numeric(self):
        with pytest.raises(TypeError, match="Both sides must be numbers"):
            pythagorean_theorem("3", 4)
        with pytest.raises(TypeError, match="Both sides must be numbers"):
            pythagorean_theorem(3, "4")
        with pytest.raises(TypeError, match="Both sides must be numbers"):
            pythagorean_theorem(None, 4)


class TestMathematicalRelationships:
    """Test mathematical relationships between geometric functions."""

    def test_circle_area_perimeter_relationship(self):
        # For a circle with radius r: Area = π*r², Perimeter = 2*π*r
        # So Area/Perimeter = r/2
        radius = 5
        area = area_circle(radius)
        perimeter = perimeter_circle(radius)
        ratio = area / perimeter
        expected_ratio = radius / 2
        assert abs(ratio - expected_ratio) < 1e-10

    def test_square_area_perimeter_relationship(self):
        # For a square with side s: Area = s², Perimeter = 4*s
        # So Area/Perimeter = s/4
        side = 8
        area = area_rectangle(side, side)
        perimeter = perimeter_rectangle(side, side)
        ratio = area / perimeter
        expected_ratio = side / 4
        assert abs(ratio - expected_ratio) < 1e-10

    def test_right_triangle_pythagorean_relationship(self):
        # For a right triangle, the area calculated using base*height/2
        # should be consistent with the Pythagorean theorem
        a, b = 3, 4
        c = pythagorean_theorem(a, b)
        area = area_triangle(a, b)

        # Verify c is indeed 5 for the 3-4-5 triangle
        assert abs(c - 5.0) < 1e-10
        # Verify area is 6 for this triangle
        assert abs(area - 6.0) < 1e-10

    def test_distance_pythagorean_relationship(self):
        # Distance between two points should match Pythagorean theorem
        x1, y1 = 0, 0
        x2, y2 = 3, 4

        distance = distance_between_points(x1, y1, x2, y2)
        pythagorean_result = pythagorean_theorem(abs(x2 - x1), abs(y2 - y1))

        assert abs(distance - pythagorean_result) < 1e-10

    def test_triangle_perimeter_vs_individual_sides(self):
        # Perimeter should equal sum of individual sides
        a, b, c = 6, 8, 10
        perimeter = perimeter_triangle(a, b, c)
        manual_sum = a + b + c
        assert abs(perimeter - manual_sum) < 1e-10

    def test_rectangle_vs_square_consistency(self):
        # A square is a rectangle with equal sides
        side = 7
        square_area = area_rectangle(side, side)
        square_perimeter = perimeter_rectangle(side, side)

        # Verify properties
        assert square_area == side * side
        assert square_perimeter == 4 * side

    def test_area_scaling_properties(self):
        # When dimensions are scaled by factor k, area scales by k²
        scale_factor = 3
        original_radius = 2

        original_area = area_circle(original_radius)
        scaled_area = area_circle(original_radius * scale_factor)

        expected_scaled_area = original_area * scale_factor**2
        assert abs(scaled_area - expected_scaled_area) < 1e-10

    def test_perimeter_scaling_properties(self):
        # When dimensions are scaled by factor k, perimeter scales by k
        scale_factor = 2.5
        original_length, original_width = 4, 6

        original_perimeter = perimeter_rectangle(original_length, original_width)
        scaled_perimeter = perimeter_rectangle(
            original_length * scale_factor,
            original_width * scale_factor
        )

        expected_scaled_perimeter = original_perimeter * scale_factor
        assert abs(scaled_perimeter - expected_scaled_perimeter) < 1e-10


@pytest.mark.parametrize("radius,expected_area", [
    (0, 0),
    (1, math.pi),
    (2, 4 * math.pi),
    (0.5, 0.25 * math.pi),
    (10, 100 * math.pi),
])
def test_area_circle_parametrized(radius, expected_area):
    """Parametrized tests for area_circle function."""
    result = area_circle(radius)
    assert abs(result - expected_area) < 1e-10


@pytest.mark.parametrize("length,width,expected_area", [
    (0, 5, 0),
    (5, 0, 0),
    (1, 1, 1),
    (3, 4, 12),
    (2.5, 4.0, 10.0),
    (10, 10, 100),
])
def test_area_rectangle_parametrized(length, width, expected_area):
    """Parametrized tests for area_rectangle function."""
    result = area_rectangle(length, width)
    assert abs(result - expected_area) < 1e-10


@pytest.mark.parametrize("a,b,expected_c", [
    (0, 0, 0),
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (1, 1, math.sqrt(2)),
    (6, 8, 10),
])
def test_pythagorean_theorem_parametrized(a, b, expected_c):
    """Parametrized tests for pythagorean_theorem function."""
    result = pythagorean_theorem(a, b)
    assert abs(result - expected_c) < 1e-10


@pytest.mark.parametrize("x1,y1,x2,y2,expected_distance", [
    (0, 0, 0, 0, 0),
    (0, 0, 3, 4, 5),
    (1, 1, 1, 1, 0),
    (0, 0, 1, 0, 1),
    (0, 0, 0, 1, 1),
    (-1, -1, 2, 3, 5),
])
def test_distance_between_points_parametrized(x1, y1, x2, y2, expected_distance):
    """Parametrized tests for distance_between_points function."""
    result = distance_between_points(x1, y1, x2, y2)
    assert abs(result - expected_distance) < 1e-10


class TestEdgeCasesAndBoundaryConditions:
    """Test edge cases and boundary conditions for all geometry functions."""

    def test_very_small_values(self):
        # Test with very small positive values
        tiny_value = 1e-10

        circle_area = area_circle(tiny_value)
        assert circle_area >= 0

        rect_area = area_rectangle(tiny_value, tiny_value)
        assert rect_area >= 0

        triangle_area = area_triangle(tiny_value, tiny_value)
        assert triangle_area >= 0

    def test_very_large_values(self):
        # Test with large values to check for overflow
        large_value = 1e6

        circle_area = area_circle(large_value)
        assert circle_area > 0
        assert not math.isinf(circle_area)

        rect_area = area_rectangle(large_value, large_value)
        assert rect_area > 0
        assert not math.isinf(rect_area)

    def test_precision_with_floats(self):
        # Test precision with floating-point arithmetic
        result1 = area_circle(1.0/3.0)
        result2 = area_circle(0.33333333333333331)

        # Results should be very close but not necessarily identical
        # due to floating-point precision
        assert abs(result1 - result2) < 1e-10

    def test_invalid_triangle_boundary_cases(self):
        # Test triangles that are exactly on the boundary of validity
        epsilon = 1e-10

        # This should be invalid (sum equals third side)
        with pytest.raises(ValueError):
            perimeter_triangle(1, 2, 3)

        # This should be valid (sum slightly greater than third side)
        result = perimeter_triangle(1, 2, 3 - epsilon)
        assert result > 0
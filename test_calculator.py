"""Tests for the calculator module."""
import pytest
from calculator import add, subtract, multiply, divide, main


def test_add():
    """Test addition."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    """Test subtraction."""
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(0, 5) == -5


def test_multiply():
    """Test multiplication."""
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6


def test_divide():
    """Test division."""
    assert divide(6, 2) == 3.0
    assert divide(5, 2) == 2.5
    assert divide(0, 5) == 0.0


def test_divide_by_zero():
    """Test division by zero raises error."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)


def test_cli_add(capsys):
    ret = main(["add", "2", "3"])
    captured = capsys.readouterr()
    assert ret == 0
    assert captured.out == "5\n"


def test_cli_divide_by_zero(capsys):
    ret = main(["divide", "5", "0"])
    captured = capsys.readouterr()
    assert ret != 0
    assert "Cannot divide by zero" in captured.err


def test_cli_unknown_operation(capsys):
    ret = main(["modulo", "4", "2"])
    captured = capsys.readouterr()
    assert ret != 0
    assert "add" in captured.err
    assert "subtract" in captured.err
    assert "multiply" in captured.err
    assert "divide" in captured.err
    assert "power" in captured.err


def test_cli_bad_args(capsys):
    ret = main(["add", "x", "3"])
    captured = capsys.readouterr()
    assert ret != 0
    assert captured.err != ""

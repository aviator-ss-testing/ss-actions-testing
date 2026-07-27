"""Simple calculator module for testing CI rework."""
import sys


def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtract b from a."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


def divide(a: int, b: int) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: int, exp: int) -> int:
    """Raise base to the power of exp."""
    result: int = base**exp
    return result


_OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "power": power,
}


def main(argv):
    if len(argv) != 3:
        print("Usage: calculator.py <operation> <a> <b>", file=sys.stderr)
        return 2

    op_name, a_str, b_str = argv

    if op_name not in _OPERATIONS:
        print(
            f"Unknown operation '{op_name}'. Supported operations: add, subtract, multiply, divide, power",
            file=sys.stderr,
        )
        return 2

    try:
        a = int(a_str)
        b = int(b_str)
    except ValueError:
        print(f"Error: arguments must be integers, got '{a_str}' and '{b_str}'", file=sys.stderr)
        return 2

    try:
        result = _OPERATIONS[op_name](a, b)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

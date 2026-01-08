"""Prompt for two numbers and a symbol operation (+, -, *, /).

Subtraction returns the absolute difference.
"""


def mathematical_operation(num1, num2, op):
    """Perform the arithmetic operation indicated by `op` on two numbers.

    Args:
        num1 (float): first operand.
        num2 (float): second operand.
        op (str): one of '+', '-', '*', '/'.

    Returns:
        float or str: result of the operation or an error message string.

    Notes:
        - Subtraction returns the absolute difference between the numbers.
        - Division by zero returns an error message string.
    """
    if op == '+':
        return num1 + num2
    if op == '-':
        return abs(num1 - num2)
    if op == '*':
        return num1 * num2
    if op == '/':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    return "Error: Invalid operation"


def get_float(prompt):
    """Prompt the user until a valid float is entered.

    Returns the parsed float.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_operation(prompt):
    """Prompt the user until a valid operation symbol is entered.

    Acceptable symbols: '+', '-', '*', '/'. Returns the chosen symbol.
    """
    while True:
        op = input(prompt).strip()
        if op in ('+', '-', '*', '/'):
            return op
        print("Invalid operation. Choose one of: +, -, *, /")


def main():
    """Main interactive loop: show menu, read inputs, compute and print result."""
    print("Available operations:")
    print("  + : addition")
    print("  - : subtraction (absolute difference)")
    print("  * : multiplication")
    print("  / : division")

    a = get_float("Enter the first number: ")
    b = get_float("Enter the second number: ")
    op = get_operation("Choose an operation symbol (+, -, *, /): ")

    result = mathematical_operation(a, b, op)
    print("Result:", result)


if __name__ == '__main__':
    main()

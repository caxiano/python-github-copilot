"""Concatenate two user-provided values into a single string.

This module reads two values from the user and prints them joined
by a single space.
"""


def concat_data(data1, data2):
    """Return the two inputs concatenated with a space between them.

    Args:
        data1: First value (any type).
        data2: Second value (any type).

    Returns:
        str: Concatenated string representation of both values.
    """
    return str(data1) + " " + str(data2)


def main():
    """Read two values from input, concatenate and print the result."""
    data1 = input("Enter the first value: ")
    data2 = input("Enter the second value: ")

    result = concat_data(data1, data2)
    print("Concatenation result:", result)


if __name__ == '__main__':
    main()

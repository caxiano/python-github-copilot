"""Repeat a given text a specified number of times.

This module prompts the user for a string and an integer, then prints
the string repeated `times` times separated by a space.
"""


def repeat_text(text, times):
    """Return `text` repeated `times` times separated by spaces.

    Args:
        text (str): The text to repeat.
        times (int): Number of repetitions.

    Returns:
        str: The repeated text with trailing space removed.
    """
    if times <= 0:
        return ""
    return (text + " ") * times


def main():
    """Read input values, call `repeat_text` and print the result."""
    text = input("Enter a text: ")
    try:
        times = int(input("Enter a number: "))
    except ValueError:
        print("Invalid number; expected an integer.")
        return

    result = repeat_text(text, times)
    print("Repeated text:", result)


if __name__ == '__main__':
    main()

def check_even_odd(number):
    """
    Checks if a number is even or odd.

    Args:
        number: An integer.

    Returns:
        A string, "Even" or "Odd".
    """
    return "Even" if number % 2 == 0 else "Odd"

if __name__ == "__main__":
    try:
        user_input = input("Enter an integer: ")
        num = int(user_input)
        result = check_even_odd(num)
        print(f"The number {num} is {result}.")
    except ValueError:
        print("Error: Please enter a valid integer.")
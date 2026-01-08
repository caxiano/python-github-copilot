
def is_palindrome(word):
    """
    Checks if a word is a palindrome.

    A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or racecar.

    Args:
        word (str): The word to check.

    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """
    # Clean the word by removing spaces and converting to lowercase
    cleaned_word = ''.join(filter(str.isalnum, word)).lower()
    # Compare the cleaned word with its reverse
    return cleaned_word == cleaned_word[::-1]

if __name__ == "__main__":
    try:
        user_input = input("Enter a word to check if it's a palindrome: ")
        
        if is_palindrome(user_input):
            print(f"'{user_input}' is a palindrome.")
        else:
            print(f"'{user_input}' is not a palindrome.")

    except Exception as e:
        print(f"An error occurred: {e}")

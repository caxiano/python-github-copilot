
def calculate_average(note1, note2, note3):
    """
    Calculates the average of three grades.

    Args:
        note1: The first note.
        note2: The second note.
        note3: The third note.

    Returns:
        The average of the three notes.
    """
    return (note1 + note2 + note3) / 3

if __name__ == "__main__":
    try:
        note1 = float(input("Enter the first note: "))
        note2 = float(input("Enter the second note: "))
        note3 = float(input("Enter the third note: "))
        
        average = calculate_average(note1, note2, note3)
        print(f"The average of the notes is: {average:.2f}")

    except ValueError:
        print("Error: Please enter valid numbers for the notes.")

import random
import csv
import sys
from exceptions import (
    EmptyRowError,
    NoPhrasesFoundError,
    CSVFileNotFoundError,
    ImproperlyFormattedRowError,
)


def main():
    try:
        play_game()
    except EOFError:
        sys.exit()


def select_random_phrase(filename="phrases.csv"):
    phrases = []
    try:
        with open(filename, newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                # Add phrase if the row is not empty and the first cell is not empty
                if row and row[0].strip():
                    phrases.append(row[0])
                else:
                    raise EmptyRowError("Found an empty row or cell in the CSV file.")

        # Handle the case where all rows might be empty or the file is empty
        if not phrases:
            raise NoPhrasesFoundError("No valid phrases found in the file.")

    except FileNotFoundError:
        raise CSVFileNotFoundError("CSV file not found.")
    except IndexError:
        raise ImproperlyFormattedRowError(
            "Found an improperly formatted row in the CSV file."
        )

    return random.choice(phrases)


def random_blank(string):
    # Create a list of indices excluding spaces
    indices = [i for i, char in enumerate(string) if char != " "]

    # Get 50% of the string blanked out (excluding spaces)
    num_to_blank = len(indices) // 2

    # Randomly select indices to blank out
    blank_indices = random.sample(indices, num_to_blank)

    str_list = list(string)

    # Replace selected characters with "_"
    for index in blank_indices:
        str_list[index] = "_"

    # Convert the list back to a string and return
    return "".join(str_list)


def update_phrase_display(current_display, phrase, guess):
    new_display = ""
    for i in range(len(phrase)):
        if phrase[i].lower() == guess.lower():
            new_display += phrase[i]
        else:
            new_display += current_display[i]
    return new_display


def count_attempts(attempts, displayed_phrase, phrase, guess):
    """
    Counts the number of attempts based on the user's guess.

    :param attempts: Current number of attempts.
    :param displayed_phrase: The current state of the phrase being guessed.
    :param phrase: The actual phrase to guess.
    :param guess: The user's guess.
    :return: Updated number of attempts.
    """
    new_display = update_phrase_display(displayed_phrase, phrase, guess)
    if new_display == displayed_phrase or guess.lower() not in phrase.lower():
        # Increment attempts if the guess is incorrect or not in the phrase
        return attempts + 1
    return attempts


def choose_topic():
    topics = {
        "anatomy": "anatomy.csv",
        "medications": "medications.csv",
        "medical interventions": "medical-interventions.csv"
    }
    print("Choose a topic:")
    for key, value in topics.items():
        print(f"{key}: {value.split('.')[0]}")
    choice = input("Enter the number of your choice: ")
    return topics.get(choice, "phrases.csv")

def play_game():
    topic_file = choose_topic()
    phrase = select_random_phrase(topic_file)

    # Check for an error from select_random_phrase
    if phrase.startswith("Error:") or phrase == "No valid phrases found in the file.":
        print(phrase)
        return

    displayed_phrase = random_blank(phrase)

    # Check for an error from random_blank
    if isinstance(displayed_phrase, ValueError):
        print(displayed_phrase)
        return

    attempts = 0
    max_attempts = 3

    print("Welcome to Guess The Phrase!")

    while "_" in displayed_phrase and attempts < max_attempts:
        print("Phrase: " + displayed_phrase)
        print(f"Attempts remaining: {max_attempts - attempts}")
        guess = input("Guess a letter: ")
        
        # Update attempts using count_attempts function
        attempts = count_attempts(attempts, displayed_phrase, phrase, guess)

       # Update displayed phrase or check for a win
        if guess.lower() in phrase.lower():
            displayed_phrase = update_phrase_display(displayed_phrase, phrase, guess)
            if "_" not in displayed_phrase:
                print(f"Congratulations!: {phrase}")
                return

    print(f"Game over. The phrase was: {phrase}")


if __name__ == "__main__":
    main()

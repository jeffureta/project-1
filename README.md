# Guess The Phrase

## Description
Welcome to 'Guess The Phrase' – a nostalgic terminal-based game reminiscent of classics like Hangaroo and Jeopardy. Ideal for hobbyists and those who love playing games in the terminal.

## Installation
**Requirements:**
- Python 3.x: Ensure you have the latest version of Python installed, as Guess The Phrase is built with Python.
- Terminal or Command Line Interface: As this game runs in the terminal, make sure you have access to a terminal on macOS/Linux or Command Prompt/PowerShell on Windows.
- Git (optional): For easy cloning of the repository, having Git installed is recommended.

**Steps:**
1. Open your terminal or command line interface.
2. Clone the Guess The Phrase repository from GitHub using the following command:
```
git clone [Your-Github-Repository-Link]

```
3. Navigate to the cloned directory:
```
cd Guess-The-Phrase

```
4. To start the game, run:
```
python guess_the_phrase.py
```
## Usage
To play "Guess The Phrase", follow these simple steps: 

1. Start the game:
- After installation, navigate to the directory where you've cloned the repository.
- Open your terminal or command line interface.
- Run the game using the following command:
```
python guess_the_phrase.py

```
2. Playing the game:
- Once the game starts, you'll be presented with a phrase to guess, displayed as a series of underscores representing each letter.
- Enter your guesses one letter at a time. If the letter is in the phrase, it will be revealed in its correct position(s).
- Be mindful of the number of attempts you have. Incorrect guesses might cost you!

3. Winning the game: 
- Successfully reveal all the letters in the phrase before running out of attempts to win.

4. To exit "Guess The Phrase" at any point, simply press Ctrl-D. This command will safely terminate the game without any errors. Alternatively, you can close the terminal window to exit the game.

## Features
- **Intuitive Terminal Interface with Smooth Gameplay Loop**: "Guess The Phrase" features a user-friendly terminal interface that allows players to dive right into the game. Its smooth gameplay loop seamlessly guides players through each phrase, updating the display in real time as they guess letters. The game clearly shows the current state of the phrase, the letters guessed, and the remaining attempts. This straightforward and interactive design ensures players understand the game flow effortlessly. For an insight into the mechanics of this loop, see the `play_game()` function.
- **Dynamic Phrase Puzzles with Easy Content Expansion**: "Guess The Phrase" presents a variety of phrase puzzles in each session, thanks to the `select_random_phrase()` function, which retrieves phrases from phrases.csv. This approach guarantees a continually refreshing and diverse gameplay experience. Feel free to add whatever phrase you like. To introduce new phrases to the game, simply add another row in phrases.csv. This simple process enables developers and contributors to effortlessly expand the game's database, greatly increasing its replay value and diversity.
- **Limited Guesses**: "Guess The Phrase" enhances the challenge by limiting the number of guesses players have, tracked by the `count_attempts()` function. This function ensures a precise count of attempts, increasing the game's excitement. The integration of monitoring of attempts makes each guessing round both engaging and intellectually stimulating.

## Contact
- **Email**: jeffvincentureta@gmail.com
- **Twitter**: @jepoyureta

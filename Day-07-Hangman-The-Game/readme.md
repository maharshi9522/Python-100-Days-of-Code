# 🎯 Hangman Game

A command-line implementation of the classic **Hangman** game built using Python. The player must guess the hidden word one letter at a time before running out of lives.

## 📌 Overview

The game randomly selects a word from a predefined word list. The player guesses letters, and for every incorrect guess, one life is lost. The game continues until the player either successfully guesses the entire word or exhausts all available lives.

ASCII art is used to visually represent the player's remaining lives, making the gameplay more interactive.

## ✨ Features

* Random word selection
* Interactive command-line gameplay
* Life tracking system
* ASCII art visualization
* Duplicate guess detection
* Win and lose conditions
* Progressive word reveal
* Modular code structure using separate files

## 🛠️ Technologies Used

* Python 3
* `random` module

## 📂 Project Structure

```text
Day-08-Hangman/
│
├── main.py
├── hangman_words.py
├── hangman_art.py
└── README.md
```

## ▶️ How to Run

1. Clone this repository.
2. Navigate to the project folder.
3. Ensure all project files are in the same directory.
4. Run:

```bash
python main.py
```

## 🎮 Game Flow

```text
Start
   │
   ├── Random word selected
   │
   ├── Player guesses a letter
   │
   ├── Correct Guess?
   │       │
   │       ├── Yes → Reveal letter
   │       │
   │       └── No → Lose one life
   │
   ├── Word Completed?
   │       │
   │       ├── Yes → You Win
   │       │
   │       └── No
   │
   ├── Lives Remaining?
   │       │
   │       ├── Yes → Continue
   │       │
   │       └── No → Game Over
   │
   └── End
```

## 💻 Sample Output

```text
****************************6/6 LIVES LEFT****************************

Guess a letter: a

Word to guess: _ a _ _ _

****************************5/6 LIVES LEFT****************************

Guess a letter: p

Word to guess: p a p _ _

...

****************************YOU WIN****************************
```

## 📚 Concepts Practiced

* Functions
* Loops
* Conditional statements
* Lists
* Strings
* Random number generation
* Modules and imports
* State management
* Nested logic
* Game development fundamentals

## 🎯 Learning Outcome

This project was built to strengthen Python fundamentals while learning how to structure larger programs across multiple files and manage application state.

## 🚀 Future Improvements

* Difficulty levels
* Score tracking
* Hint system
* Category-based words
* Multiplayer mode
* Graphical user interface
* Save and resume game progress

---

Part of my **Python 100 Days of Code** learning journey.

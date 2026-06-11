# 🏝️ Treasure Island Adventure Game

A simple text-based adventure game built in Python where the player makes a series of choices to find the hidden treasure. Every decision affects the outcome of the game.

## 📌 Overview

The game begins with a mission to find a treasure hidden on a mysterious island. The player must navigate through different scenarios by making choices. Correct decisions lead to victory, while wrong choices end the game.

## ✨ Features

* Interactive command-line gameplay
* Multiple decision paths
* Conditional logic using `if`, `elif`, and `else`
* ASCII art for an engaging user experience
* Multiple game endings
* Beginner-friendly Python project

## 🛠️ Technologies Used

* Python 3

## ▶️ How to Run

1. Clone this repository.
2. Open the project folder.
3. Run the Python file:

```bash
python main.py
```

## 🎮 Game Flow

```text
Start
  │
  ├── Left
  │     └── Game Over
  │
  └── Right
        │
        ├── Swim
        │     └── Game Over
        │
        └── Wait
              │
              ├── Red Door
              │     └── Game Over
              │
              ├── Blue Door
              │     └── Game Over
              │
              └── Yellow Door
                    └── 🎉 You Win!
```

## 💻 Sample Output

```text
Welcome to Treasure Island.
Your mission is to find the treasure.

Type left or right: right
SWIM OR WAIT: wait
choose one door red/blue/yellow: yellow

Treasure is yours congrats you win!
```

## 📚 Concepts Practiced

* Print statements
* User input
* Conditional statements (`if`, `elif`, `else`)
* Nested conditions
* String comparison
* Program flow control
* Basic game logic
* ASCII art

## 🎯 Learning Outcome

This project was built to practice decision-making logic in Python and understand how nested conditional statements can be used to create interactive command-line games.

## 🚀 Future Improvements

* Add input validation
* Make choices case-insensitive
* Introduce more levels and paths
* Add inventory and scoring system
* Convert into a graphical game using Python libraries

---

Part of my **Python 100 Days of Code** learning journey.

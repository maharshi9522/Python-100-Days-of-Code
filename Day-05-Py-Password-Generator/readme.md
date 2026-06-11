# 🔐 PyPassword Generator

A simple Python application that generates a secure and randomized password based on the user's preferences for the number of letters, numbers, and special symbols.

## 📌 Overview

The program allows the user to customize their password by specifying:

* Number of letters
* Number of numbers
* Number of symbols

It then randomly selects characters from predefined lists, shuffles them, and generates a unique password.

## ✨ Features

* Custom password length
* User-defined number of letters, numbers, and symbols
* Randomized character arrangement
* Uses Python's built-in `random` module
* Simple command-line interface

## 🛠️ Technologies Used

* Python 3
* `random` module

## ▶️ How to Run

1. Clone this repository.
2. Open the project folder.
3. Run the Python file:

```bash
python main.py
```

## 💻 Sample Output

```text
Welcome to the PyPassword Generator!

How many letters would you like in your password?
8

How many symbols would you like?
2

How many numbers would you like?
3

Generated Password:
aK4#s9M!2Lp8
```

## ⚙️ How It Works

1. Collect user preferences.
2. Randomly select the required number of:

   * Letters
   * Numbers
   * Symbols
3. Store them in a list.
4. Shuffle the list to increase randomness.
5. Combine all characters into the final password.

## 📚 Concepts Practiced

* Lists
* Loops
* User input
* Random selection
* List manipulation
* `random.choice()`
* `random.shuffle()`
* String concatenation
* Basic algorithm design

## 🎯 Learning Outcome

This project was built to practice Python fundamentals while understanding how randomness and list operations can be combined to create a practical utility application.

## 🚀 Future Improvements

* Allow users to choose uppercase/lowercase separately
* Check password strength
* Prevent weak combinations
* Generate multiple passwords at once
* Build a GUI version using Tkinter
* Save generated passwords securely

---

Part of my **Python 100 Days of Code** learning journey.

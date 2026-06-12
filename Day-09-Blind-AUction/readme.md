# 🔨 Secret Auction Program

A Python command-line application that simulates a **blind auction system**, where multiple participants can place confidential bids, and the program determines the highest bidder.

## 📌 Overview

The program allows multiple users to enter their names and bid amounts one after another. Each bid remains hidden from subsequent participants. Once all bids are collected, the application identifies and announces the highest bidder.

## ✨ Features

* Multiple bidder support
* Secret bidding process
* Automatic winner determination
* Uses Python dictionaries for data storage
* Function-based implementation
* Interactive command-line interface

## 🛠️ Technologies Used

* Python 3

## 📂 Project Structure

```text
Day-09-Secret-Auction/
│
├── main.py
├── art.py
└── README.md
```

## ▶️ How to Run

1. Clone this repository.
2. Open the project folder.
3. Ensure all required files are available.
4. Run:

```bash
python main.py
```

## 💻 Sample Output

```text
What is your name?: Alice
What is your bid?: $250
Are there any other bidders? Type 'yes' or 'no'.
yes

What is your name?: Bob
What is your bid?: $320
Are there any other bidders? Type 'yes' or 'no'.
no

The winner is Bob with a bid of $320
```

## ⚙️ How It Works

1. Display the auction logo.
2. Accept bidder name and bid amount.
3. Store bids in a dictionary.
4. Continue accepting bids until no bidders remain.
5. Traverse the dictionary to find the highest bid.
6. Display the winner and winning amount.

## 📚 Concepts Practiced

* Functions
* Dictionaries
* Loops
* Conditional statements
* User input
* Variables
* Data storage and retrieval
* Iterating through dictionaries
* Problem decomposition

## 🎯 Learning Outcome

This project was built to understand how dictionaries can be used to manage real-world data and how functions help organize and simplify program logic.

## 🚀 Future Improvements

* Handle invalid user input
* Allow multiple auction rounds
* Display all bids after completion
* Store auction history in a file
* Add password-protected bidding
* Build a graphical user interface

## 🔑 Key Concepts

* Python Dictionaries
* Functions
* Loops
* Data Processing
* Maximum Value Search Algorithm

---

Part of my **Python 100 Days of Code** learning journey.

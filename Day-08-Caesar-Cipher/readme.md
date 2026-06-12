# 🔐 Caesar Cipher Encoder & Decoder

A Python implementation of the classic **Caesar Cipher**, one of the oldest and simplest encryption techniques. The program allows users to both encrypt and decrypt messages using a customizable shift value.

## 📌 Overview

The application takes a user message and a shift value as input and performs either:

* **Encoding (Encryption)** – Converts plain text into cipher text.
* **Decoding (Decryption)** – Converts cipher text back into plain text.

The program also supports multiple operations in a single execution and preserves spaces, numbers, and special characters.

## ✨ Features

* Encrypt messages
* Decrypt messages
* Custom shift value
* Supports repeated operations
* Preserves non-alphabetic characters
* Handles large shift values using modular arithmetic
* Interactive command-line interface

## 🛠️ Technologies Used

* Python 3

## 📂 Project Structure

```text
Day-07-Caesar-Cipher/
│
├── main.py
├── art.py
└── README.md
```

## ▶️ How to Run

1. Clone this repository.
2. Open the project folder.
3. Ensure all required files are present.
4. Run:

```bash
python main.py
```

## 💻 Sample Output

```text
Type 'encode' to encrypt, type 'decode' to decrypt:
encode

Type your message:
hello world

Type the shift number:
5

Here is the encoded result:
mjqqt btwqi
```

## ⚙️ How It Works

1. User selects encode or decode mode.
2. User enters a message.
3. User provides a shift value.
4. Each letter is shifted through the alphabet.
5. Modular arithmetic (`%`) ensures the alphabet wraps around correctly.
6. The final encrypted or decrypted message is displayed.

## 📚 Concepts Practiced

* Functions
* Parameters and arguments
* Loops
* Conditional statements
* Lists
* String manipulation
* Modular arithmetic
* User input handling
* Code reusability
* Basic cryptography concepts

## 🎯 Learning Outcome

This project was built to understand how classical encryption algorithms work and to practice Python fundamentals such as functions, loops, and modular arithmetic.

## 🚀 Future Improvements

* Support uppercase and lowercase separately
* Add custom alphabets
* File encryption support
* Graphical User Interface (GUI)
* Support for multiple cipher algorithms
* Save encrypted messages to a file

---

Part of my **Python 100 Days of Code** learning journey.

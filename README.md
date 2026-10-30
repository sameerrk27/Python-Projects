# Python Projects

A collection of beginner-friendly Python mini-projects to practice core programming concepts such as variables, user input, strings, conditionals, and basic math operations.

## Project List

1. Palindrome Checker
   - Concepts: Strings, slicing, if-else.
   - Description: Checks whether a word reads the same forward and backward.

2. Word Counter
   - Concepts: Strings, split(), len().
   - Description: Counts the number of words in a sentence.

3. Currency Convertor
   - Concepts: Variables, operators, user input.
   - Description: Converts Indian Rupees into US Dollars using an example exchange rate.

4. Even or Odd Checker
   - Concepts: Modulus operator, if-else.
   - Description: Determines whether a number is even or odd.

5. Temperature Convertor
   - Concepts: Mathematical formulas, operators.
   - Description: Converts Celsius into Fahrenheit.

---

## Mini Projects Folder Structure

```text
Python-Projects/
├── Mini-Projects/
│   ├── Palindrome Checker/
│   │   ├── main.py
│   │   └── README.md
│   ├── Word Counter/
│   │   ├── main.py
│   │   └── README.md
│   ├── Currency Convertor(single-currency-convertor)/
│   │   ├── main.py
│   │   └── README.md
│   ├── Even or Odd Checker/
│   │   ├── main.py
│   │   └── README.md
│   ├── TemperatureConvertor/
│   │   ├── main.py
│   │   └── README.md
│   ├── Text Editor App/
│   │   ├── main.py
│   │   ├── README.md
│   │   └── screenshots/
│   └── SimpleCalculator/
│       └── screenshots/
```

---

## 1. Palindrome Checker

A simple program that checks whether a user-entered word is a palindrome.

### Concepts
- Strings
- Slicing
- if-else

### Example
```python
word = input("Enter a word: ")
if word.lower() == word[::-1].lower():
    print("It is a Palindrome!")
else:
    print("It is not a Palindrome.")
```

### Output
```bash
Enter a word: level
It is a Palindrome!
```

---

## 2. Word Counter

A mini project that counts how many words are in a sentence typed by the user.

### Concepts
- Strings
- split()
- len()

### Example
```python
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))
```

### Output
```bash
Enter a sentence: Python is fun to learn
Number of words: 6
```

---

## 3. Currency Convertor

A beginner-friendly project that converts Indian Rupees into US Dollars using a sample exchange rate.

### Concepts
- Variables
- Operators
- User input

### Example
```python
rupees = float(input("Enter amount in INR: "))
usd = rupees / 94
print("Amount in USD:", usd)
```

### Output
```bash
Enter amount in INR: 800
Amount in USD: 8.51063829787234
```

---

## 4. Even or Odd Checker

A simple program that checks whether a number is even or odd.

### Concepts
- Modulus operator
- if-else

### Example
```python
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd Number")
```

### Output
```bash
Enter a number: 5
Odd Number
```

---

## 5. Temperature Convertor

A beginner program that converts Celsius temperature into Fahrenheit.

### Concepts
- Mathematical formulas
- Operators

### Example
```python
celsius = float(input("Enter Temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Temperature in Fahrenheit:", fahrenheit)
```

### Output
```bash
Enter Temperature in Celsius: 30
Temperature in Fahrenheit: 86.0
```

---

## How to Run Any Project

Go to the project folder and run:

```bash
python main.py
```

---

## Skills Practiced

- Python basics
- User input handling
- Conditional statements
- String operations
- Mathematical calculations
- Beginner problem-solving

---

## Purpose

These mini-projects are designed to help beginners understand Python programming through simple and practical examples.

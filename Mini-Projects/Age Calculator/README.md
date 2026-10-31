# Age Calculator

A simple Python project that calculates a person's age based on their birth year.

## Project Overview
This mini project uses Python's `datetime` module to get the current year and subtract the entered birth year.

## Files
- `AgeCalculator.ipynb` - Jupyter notebook containing the project logic
- `AgeCal.png` - sample output image

## How to Run
1. Open the `AgeCalculator.ipynb` file in Jupyter Notebook or VS Code.
2. Run all cells.
3. Enter your birth year when prompted.
4. The program will display your age.

## Example
```python
birth_year = int(input("Enter your birth year:"))
current_year = date.today().year
age = current_year - birth_year
print("Your age is :", age)
```

## Requirements
- Python 3
- Jupyter Notebook or a Python notebook viewer

# Student Grade Management System

## Problem Statement

Schools and colleges often need a simple way to manage student records and grades. Manually tracking grades can become confusing and time-consuming, especially when records need to be updated or deleted frequently.

This project helps manage student grades efficiently using a Python program. It allows the user to add, update, delete, and view student records.

## Features

- Add a new student with a grade
- Update an existing student’s grade
- Delete a student from the system
- View all students and their grades
- Run the system repeatedly using a menu-based interface

## Workflow

1. The program displays a menu with options.
2. The user chooses an action:
   - Add Student
   - Update Student
   - Delete Student
   - View All Students
   - Exit
3. The program performs the selected action.
4. The result is displayed on the screen.

## Data Structure Used

The program uses a Python dictionary:

```python
student_grades = {}
```

This dictionary stores each student name as a key and the grade as the value.

## Functions in the Program

- `add_student(name, grade)`
  - Adds a student and their grade
- `update_student(name, grade)`
  - Updates the grade of an existing student
- `del_student(name)`
  - Deletes a student from the list
- `display_all_students()`
  - Shows all students and their grades
- `main()`
  - Runs the menu-based program continuously

## Example Menu

```text
Student Grades Management System
1. Add Student
2. Update Student
3. Delete Student
4. View All Students
5. Exit
```

## Output

The program displays messages like:

- Added student with grade
- Student grade updated
- Student not found
- Student deleted successfully
- All stored student records

## Project File

- `students.py`

## Notes

This project focuses on basic student grade management, not advanced grade calculation. It is a simple and beginner-friendly program that demonstrates dictionary operations and menu-driven programming in Python.

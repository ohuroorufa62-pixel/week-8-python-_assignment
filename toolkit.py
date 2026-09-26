```python
# Personal Mini-Toolkit
# PLP Python Week 8 Final Project

print("===================================")
print(" Welcome to My Personal Mini-Toolkit!")
print("===================================")

# This list stores the tasks added by the user.
tasks = []


# Tool 1: Simple Calculator
# This tool performs basic calculations using two numbers.
def calculator():
    print("\n--- Simple Calculator ---")

    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    operation = input("Enter your choice: ")

    if operation == "1":
        result = number1 + number2
        print(f"The answer is {result}.")
    elif operation == "2":
        result = number1 - number2
        print(f"The answer is {result}.")
    elif operation == "3":
        result = number1 * number2
        print(f"The answer is {result}.")
    elif operation == "4":
        if number2 == 0:
            print("Sorry, you cannot divide by zero.")
        else:
            result = number1 / number2
            print(f"The answer is {result}.")
    else:
        print("That is not a valid operation.")


# Tool 2: To-Do List
# This tool lets the user add, view, and remove tasks from a list.
def todo_list():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Remove task")
        print("4. Back to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print(f"Task '{task}' was added.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("Your tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            task = input("Enter the task to remove: ")

            if task in tasks:
                tasks.remove(task)
                print(f"Task '{task}' was removed.")
            else:
                print(f"Task '{task}' was not found.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Please choose a valid option.")


# Tool 3: Number Checker
# This tool checks whether a number is positive, negative, or zero.
def number_checker():
    print("\n--- Number Checker ---")

    number = float(input("Enter a number: "))

    if number > 0:
        print(f"{number} is a positive number.")
    elif number < 0:
        print(f"{number} is a negative number.")
    else:
        print(f"{number} is zero.")


# Main menu loop
# The menu continues until the user chooses Quit.
while True:
    print("\n===================================")
    print("         PERSONAL MINI-TOOLKIT")
    print("===================================")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Checker")
    print("4. Quit")

    choice = input("Choose a tool: ")

    if choice == "1":
        calculator()

    elif choice == "2":
        todo_list()

    elif choice == "3":
        number_checker()

    elif choice == "4":
        print("Thank you for using my Personal Mini-Toolkit. Goodbye!")
        break

    else:
        print("Sorry, that is not a valid choice. Please choose 1, 2, 3, or 4.")
```

This structure meets the assignment because the `while` loop repeatedly displays the menu until `break` is reached, while `if`/`elif`/`else` routes the user's selection.

---

# Test 1 — Invalid Choice

Run:

```text
python toolkit.py
```

Then enter something such as **9**.

Your screenshot should show:

```text
===================================
         PERSONAL MINI-TOOLKIT
===================================
1. Simple Calculator
2. To-Do List
3. Number Checker
4. Quit
Choose a tool: 9
Sorry, that is not a valid choice. Please choose 1, 2, 3, or 4.
```

Take a screenshot and save it as:

```text
screenshots/invalid_choice.png
```

---

# Test 2 — Calculator

Choose:

```text
1
```

For example:

```text
Choose a tool: 1

--- Simple Calculator ---
Enter the first number: 10
Enter the second number: 5
Choose an operation:
1. Add
2. Subtract
3. Multiply
4. Divide
Enter your choice: 1
The answer is 15.0.
```

Save the screenshot as:

```text
screenshots/calculator.png
```

---

# Test 3 — To-Do List

Choose:

```text
2
```

Then add a few tasks:

```text
Choose a tool: 2

--- To-Do List ---
1. Add task
2. Show tasks
3. Remove task
4. Back to main menu
Choose an option: 1
Enter a task: Study Python
Task 'Study Python' was added.

--- To-Do List ---
1. Add task
2. Show tasks
3. Remove task
4. Back to main menu
Choose an option: 1
Enter a task: Complete assignment
Task 'Complete assignment' was added.

--- To-Do List ---
1. Add task
2. Show tasks
3. Remove task
4. Back to main menu
Choose an option: 2
Your tasks:
1. Study Python
2. Complete assignment
```

Save the screenshot as:

```text
screenshots/todo_list.png
```

This demonstrates a list that **changes while the program runs** using `append()` and `remove()`.

---

# Test 4 — Number Checker

Choose:

```text
3
```

For example:

```text
Choose a tool: 3

--- Number Checker ---
Enter a number: -8
-8.0 is a negative number.
```

Save the screenshot as:

```text
screenshots/number_checker.png
```

---

# Test 5 — Quit

Finally choose:

```text
4
```

You should see:

```text
Thank you for using my Personal Mini-Toolkit. Goodbye!
```

This confirms that the main loop can exit correctly using `break`.

---

# README.md

Create **`README.md`** in the repository.

# PLP Python Week 8 - Personal Mini-Toolkit

## Project Description

My Personal Mini-Toolkit is a menu-driven Python program that provides three useful tools: a simple calculator, a to-do list, and a number checker. The program uses a main menu that keeps running until the user chooses the Quit option.

## Tools

* **Simple Calculator** — performs addition, subtraction, multiplication, and division.
* **To-Do List** — allows the user to add, view, and remove tasks.
* **Number Checker** — checks whether a number is positive, negative, or zero.

## How to Run

1. Make sure Python is installed on your computer.
2. Open a terminal in the project folder.
3. Run the program using:

```text
python toolkit.py
```

4. Choose a number from the menu.
5. Follow the instructions displayed by the program.
6. Choose option 4 when you want to quit.

## Reflection

The hardest part of this project was putting all the tools inside one menu loop and making sure the menu returned after each tool finished. I also had to make sure invalid menu choices did not crash the program. The part that took the longest to test was the to-do list because I needed to check adding, showing, and removing tasks. I learned that using a list makes it possible to store information that changes while the program is running. I also learned how `if`, `elif`, and `else` can route the user to different parts of a program. With one more week, I would add a password generator or a small guessing game. I would also improve the program by handling invalid number input more safely.

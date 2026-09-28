import random


# Guessing Game
def guess_game():
    number = random.randint(1, 10)
    attempts = 0

    print("\n--- Guessing Game ---")
    print("Guess a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == number:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break
            elif guess < number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")

        except ValueError:
            print("Please enter a whole number.")


# To-Do List
def todo_list():
    tasks = []

    print("\n--- To-Do List ---")

    while True:
        print("\n1) Add task")
        print("2) View tasks")
        print("3) Remove task")
        print("4) Back to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print("Task added successfully.")

        elif choice == "2":
            if not tasks:
                print("No tasks yet.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
                continue

            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

            try:
                task_number = int(input("Enter the task number to remove: "))

                if 1 <= task_number <= len(tasks):
                    removed = tasks.pop(task_number - 1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


# Calculator
def calculator():
    print("\n--- Calculator ---")

    try:
        first = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        second = float(input("Enter the second number: "))

        if operator == "+":
            result = first + second
        elif operator == "-":
            result = first - second
        elif operator == "*":
            result = first * second
        elif operator == "/":
            if second == 0:
                print("You cannot divide by zero.")
                return
            result = first / second
        else:
            print("Invalid operator.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Please enter valid numbers.")


# Main Menu
def main():
    while True:
        print("\n==============================")
        print("       PYTHON TOOLKIT")
        print("==============================")
        print("1) Guess game")
        print("2) To-do list")
        print("3) Calculator")
        print("4) Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            guess_game()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            calculator()
        elif choice == "4":
            print("Thank you for using Python Toolkit!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")


# Start the program
if __name__ == "__main__":
    main()

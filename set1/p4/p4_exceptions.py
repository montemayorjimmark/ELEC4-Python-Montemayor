# Name: Jim Mark Montemayor
# Section: IV-BSIT C
# Activity: P4 - Safe Menu Program

from math import isfinite


def divide_numbers():
    try:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))
        if not isfinite(first) or not isfinite(second):
            raise ValueError
        result = first / second
    except ValueError:
        print("Invalid number. Please enter a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"Result: {result:g}")
    finally:
        print("Division attempt finished.")


def open_text_file():
    filename = input("Enter the file name: ").strip()
    if not filename:
        print("Please enter a file name.")
        return

    try:
        with open(filename, "r", encoding="utf-8") as text_file:
            contents = text_file.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except UnicodeDecodeError:
        print("This file could not be read as UTF-8 text.")
    except (OSError, ValueError) as error:
        print(f"Could not open the file: {error}")
    else:
        print(f"Contents of {filename}:")
        print(contents, end="" if contents.endswith("\n") else "\n")


def main():
    while True:
        print("\n=== Safe Menu Program ===")
        print("1. Divide two numbers")
        print("2. Open a text file")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            divide_numbers()
        elif choice == "2":
            open_text_file()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid menu choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")

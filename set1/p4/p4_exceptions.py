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

# Name: Jim Mark Montemayor
# Section: IV-BSIT C
# Activity: P2 - Custom Module: student_utils

from datetime import datetime

import student_utils


def enter_grades():
    """Read a positive number of grades, each between 0 and 100."""
    while True:
        try:
            count = int(input("How many grades will you enter? "))
            if count > 0:
                break
        except ValueError:
            pass
        print("Please enter a positive whole number.")

    grades = []
    for number in range(1, count + 1):
        while True:
            try:
                grade = float(input(f"Enter grade {number} (0-100): "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
            except ValueError:
                pass
            print("Please enter a number between 0 and 100.")

    return grades


def main():
    grades = enter_grades()
    generated_at = datetime.now()

    print("\n--- Student Grade Report ---")
    print(f"Generated: {generated_at:%Y-%m-%d %H:%M:%S}")
    print(f"Average: {student_utils.calculate_average(grades):.2f}")
    print(f"Highest grade: {student_utils.get_highest_grade(grades):.2f}")
    print(f"Lowest grade: {student_utils.get_lowest_grade(grades):.2f}")
    print(f"Status: {student_utils.determine_status(grades)}")


if __name__ == "__main__":
    main()

# Name: Jim Mark Montemayor
# Section: IV-BSIT C
# Activity: P1 - Student Grade Calculator
# Date: November 17, 2026


def enter_grades():
    """Ask the user for grades and return them in a list."""
    grades = []

    while True:
        try:
            number_of_grades = int(input("How many grades will you enter? "))
            if number_of_grades > 0:
                break
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Please enter a whole number.")

    for grade_number in range(1, number_of_grades + 1):
        while True:
            try:
                grade = float(input(f"Enter grade {grade_number} (0-100): "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                print("Grade must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    return grades


def calculate_average(grades):
    return sum(grades) / len(grades)


def get_highest_grade(grades):
    return max(grades)


def get_lowest_grade(grades):
    return min(grades)


def determine_status(grades):
    if calculate_average(grades) >= 75:
        return "Pass"
    return "Fail"


def show_results(grades):
    if not grades:
        print("Enter grades first so there are results to show.")
        return

    print("\n--- Grade Results ---")
    print(f"Average: {calculate_average(grades):.2f}")
    print(f"Highest grade: {get_highest_grade(grades):.2f}")
    print(f"Lowest grade: {get_lowest_grade(grades):.2f}")
    print(f"Status: {determine_status(grades)}")


def main():
    grades = []

    while True:
        print("\n=== Student Grade Calculator ===")
        print("1. Enter grades")
        print("2. View results")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            grades = enter_grades()
            print(f"Saved {len(grades)} grade(s).")
        elif choice == "2":
            show_results(grades)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()


# The grades variable inside main() is local because it is created within that function.
# A local variable is only available inside the function where it is created.
# A global variable is created outside all functions and can be accessed across the file.
# This program passes grades to other functions instead of relying on a global variable.

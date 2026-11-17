# Name: Jim Mark Montemayor
# Section: IV-BSIT C
# Activity: P1 - Student Grade Calculator
# Date: November 17, 2026


def enter_grades():
    """Ask the user for grades and return them in a list."""
    grades = []
    number_of_grades = int(input("How many grades will you enter? "))

    for grade_number in range(1, number_of_grades + 1):
        grade = float(input(f"Enter grade {grade_number}: "))
        grades.append(grade)

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
    print(f"Average: {calculate_average(grades):.2f}")
    print(f"Highest grade: {get_highest_grade(grades):.2f}")
    print(f"Lowest grade: {get_lowest_grade(grades):.2f}")
    print(f"Status: {determine_status(grades)}")


def main():
    grades = enter_grades()
    show_results(grades)


if __name__ == "__main__":
    main()

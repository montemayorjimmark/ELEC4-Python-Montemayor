# Activity: P2 - Custom Module: student_utils
"""Reusable calculations for a nonempty list of student grades."""


def calculate_average(grades):
    return sum(grades) / len(grades)


def determine_status(grades):
    if calculate_average(grades) >= 75:
        return "Pass"
    return "Fail"


def get_highest_grade(grades):
    return max(grades)


def get_lowest_grade(grades):
    return min(grades)

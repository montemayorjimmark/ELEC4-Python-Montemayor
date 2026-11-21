# Name: Jim Mark Montemayor
# Section: IV-BSIT C
# Activity: P3 - Student Record Manager


def add_student(students, name_keys):
    name = " ".join(input("Enter the student name to add: ").split())
    if not name:
        print("Please enter a student name.")
        return

    key = name.casefold()
    if key in name_keys:
        print("That student is already on the list.")
        return

    students.append(name)
    name_keys.add(key)
    print(f"Added {name}.")


def remove_student(students, name_keys):
    name = " ".join(input("Enter the full student name to remove: ").split())
    if not name:
        print("Please enter a student name.")
        return

    key = name.casefold()
    for index, student in enumerate(students):
        if student.casefold() == key:
            students.pop(index)
            name_keys.remove(key)
            print(f"Removed {student}.")
            return

    print("Student not found.")

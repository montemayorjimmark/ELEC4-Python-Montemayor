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


def search_students(students):
    query = " ".join(input("Enter all or part of a student name: ").split()).casefold()
    if not query:
        print("Please enter a name to search for.")
        return

    matches = [name for name in students if query in name.casefold()]
    if not matches:
        print("No matching students.")
        return

    print("Matching students:")
    for name in sorted(matches, key=str.casefold):
        print(f"- {name}")


def display_students(students):
    print("\n--- Student List ---")
    for number, name in enumerate(sorted(students, key=str.casefold), start=1):
        print(f"{number}. {name}")
    print(f"Total students: {len(students)}")


def main():
    students = []
    name_keys = set()

    while True:
        print("\n=== Student Record Manager ===")
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Search for a student")
        print("4. Display all students")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students, name_keys)
        elif choice == "2":
            remove_student(students, name_keys)
        elif choice == "3":
            search_students(students)
        elif choice == "4":
            display_students(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1 to 5.")


if __name__ == "__main__":
    main()


# A list keeps items in order and can hold duplicates.
# The students list keeps each name as entered and lets me sort the names for display.
# A set holds only unique values and does not track their order.
# The name_keys set stores case-folded names so I can spot duplicates regardless of capitalization.

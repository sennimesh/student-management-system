students = {}

def add_student():
    student_id = input("Enter Student ID: ")
    if student_id in students:
        print("Student ID already exists!")
        return

    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    students[student_id] = {
        "Name": name,
        "Age": age,
        "Course": course
    }
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return

    print("\n--- Student List ---")
    for sid, details in students.items():
        print(f"ID: {sid} | Name: {details['Name']} | Age: {details['Age']} | Course: {details['Course']}")

def search_student():
    student_id = input("Enter Student ID to search: ")
    if student_id in students:
        details = students[student_id]
        print("\n--- Student Found ---")
        print(f"ID: {student_id}")
        print(f"Name: {details['Name']}")
        print(f"Age: {details['Age']}")
        print(f"Course: {details['Course']}")
    else:
        print("Student not found.")

def update_student():
    student_id = input("Enter Student ID to update: ")
    if student_id in students:
        print("Leave blank to keep current value")

        name = input("New Name: ")
        age = input("New Age: ")
        course = input("New Course: ")

        if name:
            students[student_id]["Name"] = name
        if age:
            students[student_id]["Age"] = age
        if course:
            students[student_id]["Course"] = course

        print("Student updated successfully!")
    else:
        print("Student not found.")

def delete_student():
    student_id = input("Enter Student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!")
    else:
        print("Student not found.")

def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

menu()

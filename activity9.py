
'''Manage Student Data Using Tuples and Various Methods You are tasked with managing student data using Python tuples. Each student’s data will include:
Name (string) Roll Number (integer) Marks in 3 Subjects (tuple of 3 integers) Grade (string) Your program must use tuples and implement the following methods to perform the tasks:
Create Students: Create a list of student tuples.
Display All Students:
Print all student records.
Add a New Student:
Add a student to the list.
Search for a Student: Find a student by roll number and display their details. C
alculate Total Marks: Compute and display the total marks for each student.
Update Grades: Modify a student’s grade using their roll number.
Remove a Student: Delete a student’s record from the list using their roll number.'''



def create_students():
    return [
        ("Alice", 1, (85, 90, 78), "B"),
        ("Bob", 2, (75, 88, 92), "A"),
        ("Charlie", 3, (60, 65, 70), "C")
    ]

def display_students(students):
    if not students:
        print("No student records found.")
    else:
        print("\nAll Students:")
        for s in students:
            print(s)

def add_student(students):
    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    marks = tuple(map(int, input("Enter marks in 3 subjects (space separated): ").split()))
    grade = input("Enter grade: ")
    student = (name, roll, marks, grade)
    students.append(student)
    print("Student added.")
    return students

def search_student(students):
    roll = int(input("Enter roll number to search: "))
    for s in students:
        if s[1] == roll:
            print("Student found:", s)
            return
    print("Student not found.")

def show_total_marks(students):
    print("\nTotal Marks:")
    for s in students:
        total = sum(s[2])
        print(f"{s[0]} (Roll {s[1]}) - Total Marks: {total}")

def update_grade(students):
    roll = int(input("Enter roll number to update grade: "))
    for i in range(len(students)):
        if students[i][1] == roll:
            new_grade = input("Enter new grade: ")
            name, r, marks, _ = students[i]
            students[i] = (name, r, marks, new_grade)
            print("Grade updated.")
            return students
    print("Student not found.")
    return students

def remove_student(students):
    roll = int(input("Enter roll number to remove: "))
    for i in range(len(students)):
        if students[i][1] == roll:
            del students[i]
            print("Student removed.")
            return students
    print("Student not found.")
    return students


def main():
    students = create_students()

    while True:
        print("\n--- Student Management ---")
        print("1. Display all students")
        print("2. Add a student")
        print("3. Search for a student")
        print("4. Show total marks")
        print("5. Update student grade")
        print("6. Remove a student")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            display_students(students)
        elif choice == '2':
            students = add_student(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            show_total_marks(students)
        elif choice == '5':
            students = update_grade(students)
        elif choice == '6':
            students = remove_student(students)
        elif choice == '7':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()

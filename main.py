from database import *


def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            major = input("Enter student major: ")
            create_student(name, age, major)

        elif choice == '2':
            students = read_students()
            if students:
                print("\nList of Students:")
                for student in students:
                    print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Major: {student[3]}")
            else:
                print("No students found.")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()

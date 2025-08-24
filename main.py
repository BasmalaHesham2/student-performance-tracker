from models.student import Student
from models.subject import Subject
from models.gradebook import Gradebook
from models.user import User
from models.admin import Admin
from models.teacher import Teacher
import utils

def main():

    # Sample users
    admin = Admin("admin1")
    teacher = Teacher("teacher1")
    
    # Set the current user (simulate login)
    utils.set_current_user(admin)  # Or switch to teacher for testing

    gb = Gradebook()

    while True:
        print("\n===== Student Performance Tracker =====")
        print("1) Add student")
        print("2) Add subject")
        print("3) Assign grade")
        print("4) Calculate GPA")
        print("5) Print all students")
        print("6) View student report")
        print("7) Print user role dashboard")
        print("8) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            gb.addstudent(Student(id, name))

        elif choice == "2":
            name = input("Enter subject name: ")
            code = input("Enter subject code: ")
            gb.addsubj(Subject(name, code))

        elif choice == "3":
            id = int(input("Enter student ID: "))
            subject = input("Enter subject name: ")
            grade = float(input("Enter grade: "))
            gb.assigngrade(id, subject, grade)

        elif choice == "4":
            id = int(input("Enter student ID: "))
            student = gb.getstudent(id)
            if student:
                print(f"GPA: {student.calcGPA():.2f}")
            else:
                print("Student not found.")

        elif choice == "5":
            for s in gb.students:
                print(f"{s.getid()} - {s.getname()}")

        elif choice == "6":
            id = int(input("Enter student ID: "))
            student = gb.getstudent(id)
            if student:
                student.getreport()
            else:
                print("Student not found.")

        elif choice == "7":
            print(utils.get_current_user().displaydashboard())

        elif choice == "8":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")
 


if __name__=="__main__":
    main()
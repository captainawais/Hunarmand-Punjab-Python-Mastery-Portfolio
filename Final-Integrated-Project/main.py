from student import Student
from course import Course
from enrollment import Enrollment
from file_manager import *

# ==================================================

# TECHFACT PRO

# Skills For The Future

# Student Course Management System

# ==================================================

while True:


    print("\n")
    print("=" * 50)
    print("TECHFACT PRO")
    print("Skills For The Future")
    print("=" * 50)

    # ==================================
    # STUDENT MANAGEMENT
    # ==================================

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")

    # ==================================
    # COURSE MANAGEMENT
    # ==================================

    print("6. Add Course")
    print("7. View Courses")
    print("8. Search Course")
    print("9. Update Course")
    print("10. Delete Course")

    # ==================================
    # ENROLLMENT MANAGEMENT
    # ==================================

    print("11. Enroll Student")
    print("12. View Enrollments")
    print("13. Student Profile")

    # ==================================
    # SYSTEM
    # ==================================

    print("14. Exit")

    choice = input("\nEnter Choice: ")

    # ==================================
    # ADD STUDENT
    # ==================================

    if choice == "1":

        sid = input("Student ID: ")
        name = input("Student Name: ")
        age = input("Age: ")

        student = Student(
            sid,
            name,
            age
        )

        save_student(student)

        print("\nStudent Saved Successfully")

    # ==================================
    # VIEW STUDENTS
    # ==================================

    elif choice == "2":

        view_students()

    # ==================================
    # SEARCH STUDENT
    # ==================================

    elif choice == "3":

        sid = input("Enter Student ID: ")

        search_student(sid)

    # ==================================
    # UPDATE STUDENT
    # ==================================

    elif choice == "4":

        sid = input("Enter Student ID: ")

        update_student(sid)

    # ==================================
    # DELETE STUDENT
    # ==================================

    elif choice == "5":

        sid = input("Enter Student ID: ")

        delete_student(sid)

    # ==================================
    # ADD COURSE
    # ==================================

    elif choice == "6":

        cid = input("Course ID: ")
        cname = input("Course Name: ")

        course = Course(
            cid,
            cname
        )

        save_course(course)

        print("\nCourse Saved Successfully")

    # ==================================
    # VIEW COURSES
    # ==================================

    elif choice == "7":

        view_courses()

    # ==================================
    # SEARCH COURSE
    # ==================================

    elif choice == "8":

        cid = input("Enter Course ID: ")

        search_course(cid)

    # ==================================
    # UPDATE COURSE
    # ==================================

    elif choice == "9":

        cid = input("Enter Course ID: ")

        update_course(cid)

    # ==================================
    # DELETE COURSE
    # ==================================

    elif choice == "10":

        cid = input("Enter Course ID: ")

        delete_course(cid)

    # ==================================
    # ENROLL STUDENT IN COURSE
    # ==================================

    elif choice == "11":

        student_id = input("Student ID: ")
        course_id = input("Course ID: ")

        enrollment = Enrollment(
            student_id,
            course_id
        )

        enroll_student(
            enrollment.student_id,
            enrollment.course_id
        )

    # ==================================
    # VIEW ENROLLMENTS
    # ==================================

    elif choice == "12":

        view_enrollments()

    # ==================================
    # STUDENT PROFILE
    # ==================================

    elif choice == "13":

        sid = input("Enter Student ID: ")

        student_profile(sid)

    # ==================================
    # EXIT PROGRAM
    # ==================================

    elif choice == "14":

        print("\nThank You For Using TechFact Pro")
        print("Program Closed Successfully")

        break

    # ==================================
    # INVALID OPTION
    # ==================================

    else:

        print("\nInvalid Choice")
        print("Please Enter A Valid Option")


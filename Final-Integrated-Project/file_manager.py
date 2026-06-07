# ==========================================
# SAVE STUDENT
# ==========================================

def save_student(student):

    with open("data/students.txt", "a") as file:

        file.write(
            f"{student.student_id},"
            f"{student.name},"
            f"{student.age}\n"
        )


# ==========================================
# SAVE COURSE
# ==========================================

def save_course(course):

    with open("data/courses.txt", "a") as file:

        file.write(
            f"{course.course_id},"
            f"{course.course_name}\n"
        )


# ==========================================
# VIEW STUDENTS
# ==========================================

def view_students():

    try:

        with open("data/students.txt", "r") as file:

            data = file.readlines()

            if not data:

                print("No Students Found")
                return

            print("\n----- STUDENTS -----")

            for line in data:

                print(line.strip())

    except FileNotFoundError:

        print("Student File Not Found")


# ==========================================
# VIEW COURSES
# ==========================================

def view_courses():

    try:

        with open("data/courses.txt", "r") as file:

            data = file.readlines()

            if not data:

                print("No Courses Found")
                return

            print("\n----- COURSES -----")

            for line in data:

                print(line.strip())

    except FileNotFoundError:

        print("Course File Not Found")


# ==========================================
# SEARCH STUDENT
# ==========================================

def search_student(student_id):

    try:

        with open("data/students.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if data[0] == student_id:

                    print("\nStudent Found")
                    print(line.strip())
                    return

            print("Student Not Found")

    except FileNotFoundError:

        print("Student File Not Found")


# ==========================================
# SEARCH COURSE
# ==========================================

def search_course(course_id):

    try:

        with open("data/courses.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if data[0] == course_id:

                    print("\nCourse Found")
                    print(line.strip())
                    return

            print("Course Not Found")

    except FileNotFoundError:

        print("Course File Not Found")


# ==========================================
# UPDATE STUDENT
# ==========================================

def update_student(student_id):

    students = []

    found = False

    with open("data/students.txt", "r") as file:

        for line in file:

            data = line.strip().split(",")

            if data[0] == student_id:

                found = True

                new_name = input("New Name: ")
                new_age = input("New Age: ")

                students.append(
                    f"{student_id},{new_name},{new_age}\n"
                )

            else:

                students.append(line)

    if found:

        with open("data/students.txt", "w") as file:

            file.writelines(students)

        print("Student Updated Successfully")

    else:

        print("Student Not Found")


# ==========================================
# DELETE STUDENT
# ==========================================

def delete_student(student_id):

    students = []

    found = False

    with open("data/students.txt", "r") as file:

        for line in file:

            data = line.strip().split(",")

            if data[0] == student_id:

                found = True

            else:

                students.append(line)

    if found:

        with open("data/students.txt", "w") as file:

            file.writelines(students)

        print("Student Deleted Successfully")

    else:

        print("Student Not Found")


# ==========================================
# UPDATE COURSE
# ==========================================

def update_course(course_id):

    courses = []

    found = False

    with open("data/courses.txt", "r") as file:

        for line in file:

            data = line.strip().split(",")

            if data[0] == course_id:

                found = True

                new_course = input("New Course Name: ")

                courses.append(
                    f"{course_id},{new_course}\n"
                )

            else:

                courses.append(line)

    if found:

        with open("data/courses.txt", "w") as file:

            file.writelines(courses)

        print("Course Updated Successfully")

    else:

        print("Course Not Found")


# ==========================================
# DELETE COURSE
# ==========================================

def delete_course(course_id):

    courses = []

    found = False

    with open("data/courses.txt", "r") as file:

        for line in file:

            data = line.strip().split(",")

            if data[0] == course_id:

                found = True

            else:

                courses.append(line)

    if found:

        with open("data/courses.txt", "w") as file:

            file.writelines(courses)

        print("Course Deleted Successfully")

    else:

        print("Course Not Found")

  # ==========================================
# ENROLL STUDENT
# ==========================================

def enroll_student(student_id, course_id):

    # Check duplicate enrollment

    try:

        with open("data/enrollments.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if (
                    data[0] == student_id and
                    data[1] == course_id
                ):

                    print(
                        "\nStudent Already Enrolled In This Course"
                    )

                    return

    except FileNotFoundError:

        pass

    with open(
        "data/enrollments.txt",
        "a"
    ) as file:

        file.write(
            f"{student_id},{course_id}\n"
        )

    print("\nEnrollment Successful")


# ==========================================
# VIEW ENROLLMENTS
# ==========================================

def view_enrollments():

    try:

        with open(
            "data/enrollments.txt",
            "r"
        ) as enroll_file:

            data = enroll_file.readlines()

            if not data:

                print("\nNo Enrollments Found")

                return

            print("\n")
            print("=" * 50)
            print("ENROLLMENT RECORDS")
            print("=" * 50)

            for enroll_line in data:

                enroll_data = (
                    enroll_line.strip().split(",")
                )

                student_id = enroll_data[0]
                course_id = enroll_data[1]

                student_name = "Unknown"
                course_name = "Unknown"

                # ==========================
                # GET STUDENT NAME
                # ==========================

                with open(
                    "data/students.txt",
                    "r"
                ) as student_file:

                    for student_line in student_file:

                        student_data = (
                            student_line.strip().split(",")
                        )

                        if student_data[0] == student_id:

                            student_name = student_data[1]

                            break

                # ==========================
                # GET COURSE NAME
                # ==========================

                with open(
                    "data/courses.txt",
                    "r"
                ) as course_file:

                    for course_line in course_file:

                        course_data = (
                            course_line.strip().split(",")
                        )

                        if course_data[0] == course_id:

                            course_name = course_data[1]

                            break

                print()
                print(f"Student ID : {student_id}")
                print(f"Student    : {student_name}")
                print(f"Course     : {course_name}")

                print("-" * 50)

            print("=" * 50)

    except FileNotFoundError:

        print(
            "\nEnrollment File Not Found"
        )
        
        
# ==========================================
# STUDENT PROFILE
# ==========================================

def student_profile(student_id):

    found = False

    try:

        with open(
            "data/students.txt",
            "r"
        ) as file:

            for line in file:

                data = line.strip().split(",")

                if data[0] == student_id:

                    found = True

                    print("\n")
                    print("=" * 50)
                    print("STUDENT PROFILE")
                    print("=" * 50)

                    print(f"ID   : {data[0]}")
                    print(f"Name : {data[1]}")
                    print(f"Age  : {data[2]}")

                    print("\nCourses:")

                    try:

                        with open(
                            "data/enrollments.txt",
                            "r"
                        ) as enroll:

                            for e in enroll:

                                enroll_data = (
                                    e.strip().split(",")
                                )

                                if enroll_data[0] == student_id:

                                    course_id = enroll_data[1]

                                    with open(
                                        "data/courses.txt",
                                        "r"
                                    ) as course_file:

                                        for course_line in course_file:

                                            course_data = (
                                                course_line.strip().split(",")
                                            )

                                            if course_data[0] == course_id:

                                                print(
                                                    f"✓ {course_data[1]}"
                                                )

                                                break

                    except FileNotFoundError:

                        print(
                            "Enrollment File Not Found"
                        )

                    return

        if not found:

            print("\nStudent Not Found")

    except FileNotFoundError:

        print("\nStudent File Not Found")
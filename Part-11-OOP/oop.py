print("=" * 60)
print("HUNARMAND PUNJAB - OBJECT ORIENTED PROGRAMMING")
print("=" * 60)

# =====================================
# Parent Class
# =====================================

class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print("\nStudent Information")
        print("Name :", self.name)
        print("Age  :", self.age)
        print("Grade:", self.grade)

# =====================================
# Child Class
# =====================================

class Teacher(Student):

    def __init__(self, name, age, grade, subject):
        super().__init__(name, age, grade)
        self.subject = subject

    def display_teacher(self):
        print("\nTeacher Information")
        print("Name    :", self.name)
        print("Age     :", self.age)
        print("Grade   :", self.grade)
        print("Subject :", self.subject)

# =====================================
# Objects
# =====================================

student1 = Student(
    "Awais Farooq",
    25,
    "A+"
)

student1.display_info()

teacher1 = Teacher(
    "Akbar Ali",
    35,
    "Instructor",
    "Python Programming"
)

teacher1.display_teacher()

print("\nProgram Completed Successfully")
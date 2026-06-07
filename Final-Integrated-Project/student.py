class Student:

    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def display(self):
        print(f"ID   : {self.student_id}")
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")
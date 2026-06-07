class Course:

    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def display(self):
        print(f"Course ID   : {self.course_id}")
        print(f"Course Name : {self.course_name}")
class Enrollment:

    def __init__(
        self,
        student_id,
        course_id
    ):

        self.student_id = student_id
        self.course_id = course_id

    def display(self):

        print(
            f"Student ID : {self.student_id}"
        )

        print(
            f"Course ID  : {self.course_id}"
        )
from week03.q2.courses.course import Course


class Cooking(Course):
    FIXED_COST = 1000
    COST_PER_STUDENT = 500

    def __init__(self, id, name, teacher_name, price, students: set = None):
        super().__init__(id, name, teacher_name, price, students)

    def get_cost(self):
        student_size = len(self.get_students())
        return self.COST_PER_STUDENT * student_size + self.FIXED_COST

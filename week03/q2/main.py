from week03.q2.courses.cooking import Cooking
from week03.q2.courses.sewing import Sewing


def main():
    course_01 = Sewing(id=1, name='Sewing', teacher_name='Kevin',
                    price=15, students={'student1', 'student2'})

    print(course_01)

    course_02 = Cooking(id=1, name='Cooking', teacher_name='Kevin',
                       price=15, students={'student1', 'student2'})

    print(course_02)


main()

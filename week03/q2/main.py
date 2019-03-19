from week03.q2.courses.sewing import Sewing


def main():
    course = Sewing(id=1, name='Sewing', teacher_name='Kevin',
                    price=15, students={'student1', 'student2'})

    print(course)


main()

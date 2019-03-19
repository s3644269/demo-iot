from abc import abstractmethod


class Course(object):
    def __init__(self, id, name, teacher_name, price, students: set = None):
        self.__id = id
        self.__name = name
        self.__teacher_name = teacher_name
        self.__price = price
        self.__students = students

    @abstractmethod
    def get_cost(self):
        pass

    def get_students(self):
        return self.__students

    def __str__(self):
        return f"{self.__id}-{self.__name}: cost: {self.get_cost()}"

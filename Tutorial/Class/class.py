# class basic
# how to define a class
# create a class example


class Student:
    """
    student class
    attributes: name, age, grade
    methods: get_grade
    """

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        print(self.grade)
        return self.grade

    @staticmethod
    def static_method():
        print("static method")


# how to instantiate a class
Student_1 = Student("Alice", 10, 90)
Student_1.get_grade()

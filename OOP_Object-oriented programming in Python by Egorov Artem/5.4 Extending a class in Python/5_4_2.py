class PrettyPrint:

    def __str__(self):
        res = ', '.join([str(key) + '=' + str(value) for key, value in self.__dict__.items()])
        return f'{self.__class__.__name__}({res})'


# class Person(PrettyPrint):
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age


# artem = Person('Artem', 'Egorov', 33)
# ivan = Person('Ivan', 'Ivanov', 45)
# print(artem)
# print(ivan)

# class Student(PrettyPrint):
#     def __init__(self, name, surname, student_id, faculty, specialty):
#         self.student_id = student_id
#         self.name = name
#         self.surname = surname
#         self.faculty = faculty
#         self.specialty = specialty

# student_1 = Student("Иван", "Иванов", 12345, "Физический", "Математика")
# student_2 = Student("Анна", "Смирнова", 67890, "Химический", "Биология")
# print(student_1)
# print(student_2)
#
# class Student(PrettyPrint):
#     def __init__(self, name, surname, student_id, faculty, specialty):
#         self.student_id = student_id
#         self.name = name
#         self.surname = surname
#         self.faculty = faculty
#         self.specialty = specialty
#
#     def __str__(self):
#         return f"{self.name} {self.surname}"
#
#
# student_1 = Student("Иван", "Иванов", 12345, "Физический", "Математика")
# student_2 = Student("Анна", "Смирнова", 67890, "Химический", "Биология")
# print(student_1)
# print(student_2)

# class Person(PrettyPrint):
#     pass
#
#
# p = Person()
# print(p)
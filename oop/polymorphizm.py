# class Test:
#     def print(self):
#         print('hello world')
# class SomeClass(Test):
#     def print(self):# переобьявили
#         super().print() # super это метод указывающий на родителя
#         print('hello python')


# someClass = SomeClass()
# someClass.print()


# class Calc:
#     def inc(self, arg):
#         return arg + 1
# class doubleCalc:
#     def inc(self, arg):
#         return arg + 2
# calc = doubleCalc()
# print(calc.inc(5))



# class Calc:
#     def inc(self, arg):
#         return arg + 1
#     def square(self, arg):
#         return arg*2
# class DoubleCalc(Calc):
#     def square(self, arg):
#         return super().square(arg)+arg



# class User:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#     def getInfo(self):
#         return(f"""
#         имя пользователя - {self.name}
#         фамилия пользователя - {self.surname}
#         возраст пользователя - {self.age}
#         """)

# class Student(User):
#     def __init__(self, name, surname, age, address):
#         super().__init__(name, surname, age)
#         self.address = address
#         self.isHunged = True

#     def getInfo(self):
#         return super().getInfo()+(f'''
#         адресс пользователя {self.address}
#         желудок студента {self.isHunged}''')


# student1 = Student('ivan', 'ivanov',19, 'osh')

# print(student1.getInfo())




        
        
        
    
# переобьявите функцию getInfo который мы унаследовали от класса User
# используйте super
# пусть getInfo выводит всю информацию, например адресс и голодныйЛиОн(переменная)
# уложитесь в три строки кода


class University:
    def __init__(self, university_name):
        self.name = university_name
        self.departments = {}
    
    def add_department(self, department_name):
        self.departments[department_name] = []
    
    def add_student(self, department_name, student):
        if department_name in self.departments:
            self.departments[department_name].append(student)
        else:
            print(f"Отдел {department_name} не существует в университете")
            
class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

# создаем экземпляр университета
my_university = University("Мой Университет")

# добавляем факультеты
my_university.add_department("Факультет Информационных Технологий")
my_university.add_department("Факультет Экономики")

# создаем несколько студентов
student1 = Student("Иван", "Иванов")
student2 = Student("Петр", "Петров")
student3 = Student("Мария", "Сидорова")
student4 = Student("Алексей", "Козлов")

# добавляем студентов на факультеты
my_university.add_student("Факультет Информационных Технологий", student1)
my_university.add_student("Факультет Информационных Технологий", student2)
my_university.add_student("Факультет Экономики", student3)
my_university.add_student("Факультет Экономики", student4)

# выводим список студентов на каждом факультете
for department, students in my_university.departments.items():
    print(f"Факультет {department}:")
    for student in students:
        print(f"\t{student.firstname} {student.lastname}")

        


    
# Создайте класс University. В конструкторе создайте переменную экземпляра
# name, куда записывается переданный аргумент university_name.

# 2) Создайте переменную класса departments, у которого значение по умолчанию --
# пустой словарь

# 3) Создайте метод add_department, у которого параметр название факультета.
# Метод должен записать в словарь departments название факультета, а в
# качестве значения -- пустой список

# 4) Создайте класс Student, в конструкторе которого записывается firstname,
# lastname студента. Т.е. при создании экземпляра должны быть переданы имя и
# фамилия студента.

# 5) Создайте метод add_student с параметрами название факультета и объект
# студент -- экземпляр класса Student. Метод должен записать в словарь
# departments студента в соответствующий факультет.

# 6) Создайте экземпляр университета. Создайте нескольких студентов. Добавьте
# факультеты. Добавьте студентов в факультеты.
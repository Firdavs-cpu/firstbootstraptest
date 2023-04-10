# class Products:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def sell (self):
#         if self.quantity > 0:
#             self.quantity =- 1
#             print('Продукт продан')
#         else:
#             print('Продукт отсуствует')
# product1 = Products('Банан', 10, 20)
# product1.sell()
# product1.sell()
# for i in range(10):
#     product1.sell()
# product1.sell()


#--------------------------------------------------------------------------

# class Student:
#     def __init__(self, name, surname, age, average_grade):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.average_grade = average_grade

#     def change_average_grade(self, new_grade):
#         self.average_grade = new_grade
#         print("Средний балл изменен на", new_grade)

# # создание объекта класса Student
# student1 = Student("Иван", "Иванов", 20, 4.5)

# # вывод начального значения среднего балла
# print("Начальный средний балл:", student1.average_grade)

# # вызов метода change_average_grade и изменение среднего балла
# student1.change_average_grade(4.0)

# # вывод измененного значения среднего балла
# print("Измененный средний балл:", student1.average_grade)



# class Test:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
    



# def math(num1, num2):
#     if num1 == 0:
#         return (num2, 0, 1)
#     else:
#         div, x, y = math(num2 % num1, num1)
#     return (div, y - (num2 // num1) * x, x)

# a = math(426, 334)
# print(f'Делитель равен {a[0]}, x = {a[1]}, y = {a[2]}')







        
        


# # Магические методы

# class Test:
#     def __init__(self, name, age, address): # конструктор 
#         print("Создание экземпляра")
#         self.name = name
#         self.age = age
#         self.address = address
    
#     def __str__(self):
#         return 'Наш тестовый класс'

#     def __bool__(self):
#         if self.name == 'Умар':
#             return True
#         else:
#             return False

# test = Test('Вася', 15, 'Osh')
# if test:
#     print(test)
# # test2 = Test('Вася', 20, 'Osh')
        

"""
__init__ - вызывается при создании экземпляра

__str__ - работает при вызове строк

__bool__ - вызывается при ожидании булевых значений
"""




# class Test:
#     def __init__(self,age):
#         self.age = age
#     def __add__(self, object):
#         self.age += object
    
# test=Test(10)
# test + 2
# print(test.age)


# class Test:
#     def __init__(self,age):
#         self.age = age
#     def __sub__(self, object):
#         self.age -= object
    
# test=Test(10)
# test - 2
# print(test.age)

class Test:
    def __mul__(self,age):
        self.age = age
    def __sub__(self, object):
        self.age *= object
    
test = Test(10)
test * 2
print(test.age)
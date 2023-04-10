# ООП - Объекто ориентированное програмирования

# class Test:
#     name = 'Umar' # переменные

#     def printHelloworld():
#         print('hello world') # функции

#         class SomeTest: # классы
#             pass


# print(Test.name)
# Test.printHelloworld()


# Принципы ООП


# Наследование
# Инкапсуляция
# Полиморфизм
# Абстракция


# Инкапсуляция
# Защита, сокрытие


# class Calc:

#     __pi = 3.1415
#     def AreaCircle(radius):

#         return radius * 2 * Calc.__pi
    
# print(Calc.pi(5))
# print(Calc.__pi)


# class User:
#     name = 'firdavs'
#     __surname = 'saidjalalov'

# print(User.name)
# print(User.__surname)




# Динамические и статистические свойства

# class User:
#     name = 'Умар' # статистическое
#     def __init__(self):
#         # динамическое
#         self.surname = 'Умарович'

# # print(User.name)
# User.name = 'Саша'
# user1 = User()
# user2 = User()
# user1.surname = 'Васильев'
# print(user1.surname)
# print(user2.surname)
# print(user1.name)
# print(user2.name)
# # статистическая переменная работает по принципу 'один для все'
# # динамическое переменная 'для каждого свой'



class student:
    def __init__(self,name,adress,age):
        # print('Запуск')
        self.name = name
        self.age = age
        self.adress = adress

    def info(self):
        print(f'Cтудента зовут - {self.name}, Он живет в городе {self.adress}, и ему {self.age}')
    

student1 = student('Умар', 19, 'Ош')
student2 = student('Михаил', 20, 'Махачкала')
student3 = student('Саня', 20, 'Африка')

# student1.name = 'Умар'

# student2.name = 'Михаил'

# student3.name = 'Саня'

# student1.age = '17'
# student2.age = '19'
# student3.age = '60'

# student1.adress = 'Ош'
# student2.adress = 'Махачкала'
# student3.adress = 'Африка'



student1.info()



# Добавьте статистическую переменную по имени course 

# добавьте функцию GetCourse где выводит на экран 'имя + курс'

# сделайте все динамические переменные защищенными, то есть скройте

# вызовите функцию info после инкапсуляции переменных







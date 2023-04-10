# Функции
# Методы

# def HelloWorld():#Создание функции
#     print('Hello world')
#     print('Hello world')
#     print('Hello world')
# HelloWorld()#Вызов
# HelloWorld()#Вызов



# def Result():
#     num1 = int(input())
#     num2 = int(input())
#     print(num1 + num2)
# Result()

# def a(name,age,adress,nomer):
#     print(f'Ваше имя - {name} ,Ваш возраст - {age} ,Ваш адресс - {adress} ,Ваш номер - {nomer}')
# a('Фирдавс','17', 'Ош', '+996999909090')

# def summa():
#     return 4+4 #Оператор Return возвращает значение а также код который написан после Return не читается
# number = summa()
# print(number)

# def summa(num1, num2):
#     if num2 == 0 or num1 == 0:
#         return 0
#     else:
#         summa2 = num1 // num2
#         return summa2

# a = summa(10,2)
# print(a)

# Рекурсия
# вызов самого себя
# def printNumber(arg1):
#     print(arg1)
#     printNumber(arg1 + 1)

# printNumber(1)

# def Stepen (arg1, arg2):
#     return (arg1 ** arg2)
# a = Stepen(2, 3)
# print(a)

# def generate(n, open=0, closed=0, text=""):
#     if len(text)==n*2:
#         print(text)
#         return
#     if open<n:
#         generate(n ,open+1, closed, text+'🥰')
#     if  closed<open:
#         generate(n ,open, closed+1, text+'😜')
# generate(3)

# Аргументы args

# def summa(*args):
#     print(sum(args))
# summa(1,2)

# def printsArgs(*arg):
#     sum = 0
#     for i in arg:
#         sum += i
#     print(sum)

# printsArgs(5,5,5,5,)


# Аргументы **Kargs


# def names(**args):
#     for i in args.keys():
#        print(i ,args[i])
# names(Student1 = '- Umar',Student2 = '- Elzat')


# Лямда функции
# cокращенные функции, примерно как тернарные операторы, то есть функции в одну строку

# def firstHelloPrint(name):
#     print(f'Hello {name}')

# firstHelloPrint('Умар')

# secondHelloPrint = lambda name: print(f'Hello {name}')

# secondHelloPrint('Умар')

# sum = lambda x,y: print(x+y)

# sum(2,2)

# sum = lambda x,y: x**y

# a = sum(2,3)
# print(a)

sum = lambda x,y: print(x) if x>y  else print(y)
a = sum(2,3)
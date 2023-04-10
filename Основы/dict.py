# словари 

# my_dict = {'name':'umar', 'age':15}
# my_list = ['umar',15]
# print (my_list[0])

# my_list = []

# while True:
#     oper = input('add; break;')
#     if oper == 'break':
#         print(my_list)
#         break #Выход из цикла
#     elif oper == 'add':
#         name, age = map (str,input().split)
#         my_dict = {'name':name,'age':age}
#         my_list.append()
#     else:
#         print('error')
     




   

# # изменение 
# my_dict = {'name':'umar', 'age':15}

# #pop()удаление - .deleted()
# my_dict.pop('name')
# print(my_dict)



# settings = {'model':'mi', 'cores': 8, 'camera':'48mx'}
# #values() - Возвращает список значений
# for i in settings.values():
#     print(i)

# my_list = []

# while True:
#     oper = input('Add; Break; ')
#     if oper=='Break':
#         print(my_list)
#         break # выход из цикла
#     elif oper=='Add':
#         name, age = map(str, input().split())
#         if int(age) < 18:
#             print('No')
#         else:
#             my_dict = {'name':name, 'age': age}# создание словаря
#             my_list.append(my_dict)# добавление в список

#     else:
#         print('Неверный оператор')




# my_list = []
# while True:
#     oper = input('Add; Break; ')
#     if oper=='Break':
#         print(my_list)
#         break # выход из цикла
#     elif oper=='Add':
#         name, age = map(str,input().split())
#         if int(age)<18:
#             print('Ваш возраст не подходит')
#         elif len(name) < 5:
#             print('формат имени не правильный')
#         else:
#             my_dict = {'name':name, 'age': age} # создание словаря
#             my_list.append(my_dict)# добавление в список
#     else:
#         print('Неверный оператор')





#Тернарные операторы

# text = input()
# if text=='Hello':
#     print('Hi')
# else:
#     print('Good bye')

# print('Hi' if text=='Hello' else 'Good bye')
# print(('Good bye', 'Hi')[text=='Hello'])


# num = int(input('Ведите число - '))
# print('Число четное' if num % 2 == 0 else 'Не чотное')

# num1 = int(input('Первое число - '))
# num2 = int(input('Второе число - '))
# print (f'Большое число - {num1}' if num1 > num2 else f'Большое число - {num2}')






#1
# num = int(input())
# f1 = 0
# f2 = 1
# for i in range(num):
#     fNext = f1 + f2
#     f1 = f2
#     f2 = fNext
#     print(f2)




# number = int(input())
# for i in range(1, number//2 + 1):  
#     if number % i == 0:
#         print(i)



# number = int(input())
# for o in range(1, number):
#     sum = 0
#     for i in range(1, o//2 + 1):  
#         if o % i == 0:
#             sum += i
#     else:
#         if o == sum:
#             print(o)

number = int(input())
if number % 2 == 0:
    print('yes')
else:
    print('no')
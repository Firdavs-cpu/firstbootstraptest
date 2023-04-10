# def decorator(func):
#     def wrapper():
#         func_result = func()
#         return f'{func_result}. Успешно выполнена наша функция'
#     return wrapper


# @decorator
# def printHello():
#     def textFormat():
#         text = f'Hello'
#         return text
#     return textFormat()


# print(printHello())  # выведет: "Hello. Успешно выполнена наша функция"




# print(simpleBakti())

# import timeit

# code_to_test = """
# a = range(100000)
# b = []
# for i in a:
#     b.append(i*2)
# """

# elapsed_time = timeit.timeit(code_to_test, number=100)/100
# print(elapsed_time)


# import time

# start_time = time.monotonic()

# # вычисляем сумму всех чисел от 1 до 100000
# total = 0
# for i in range(1, 100001):
#     total += i

# end_time = time.monotonic()

# print(f'Сумма всех чисел от 1 до 100000: {total}')
# print(f'Время выполнения: {(end_time - start_time):.6f} секунд')


# import time

# def sieve_of_eratosthenes(n):
#     primes = [True] * (n+1)
#     primes[0] = primes[1] = False
#     for i in range(2, int(n**0.5)+1):
#         if primes[i]:
#             primes[i*i: n+1: i] = [False] * len(primes[i*i: n+1: i])
#     return [i for i in range(2, n+1) if primes[i]]

# start_time = time.time()
# primes = sieve_of_eratosthenes(100000)
# end_time = time.time()

# print(f"Найдено {len(primes)} простых чисел до 100000.")
# print(f"Время выполнения: {end_time - start_time:.5f} секунд.")




# def decorator(func):

#     import time

#     def wrapper(*args, **kyeargs):
#         start = time.time()
#         func(*args, **kyeargs)
#         end = time.time()
#         print(f'Начало алгоритма {start}, и конец {end}')
#     return wrapper

# @decorator
# def sieve_of_eratosthenes(n):
#     primes = [True] * (n+1)
#     primes[0] = primes[1] = False
#     for i in range(2, int(n**0.5)+1):
#         if primes[i]:
#             primes[i*i: n+1: i] = [False] * len(primes[i*i: n+1: i])
#     print( [i for i in range(2, n+1) if primes[i]])

# sieve_of_eratosthenes(5)






# Геттер, сеттер

class Test:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def name(self):
        if self.name == 'Умар':
            return self.name
        else:
            return 'Имя не правильное'

    @name.setter
    def name(self, new):
        if new != 'Мат':
            self.name = new

    @property
    def surname(self):
        if self.surname == 'Умаров':
            return self.surname.upper()
        else:
            return 'ERROR'

    @surname.setter
    def surname(self, new):
        if new != 'чтото':
            self.surname = new


test1 = Test('Умар', 'Умаров')
test2 = Test('Умoар', 'Умаров')
test1.name = 'Мат'
test2.surname = 'чтото'



print(f'Имя - {test1.name} Фамилия - {test2.surname}')




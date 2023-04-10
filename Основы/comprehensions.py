#list comprehension #похожа на тернарные операторы


# number = [i*2 for i in range(10)]
# number = [i for i in range(10) if i%2==0]
# print(number)

# number1 = [i for i in range(20) if i%2==0]
# print(number1)
# number2 = [i for i in range(0, 20, 2)]
# print(number2)
# number3 = [i*2 for i in range(10)]
# print(number3)


text = input()
char = input()
some = [i for i in text if char != i]
print(some)
# уберите все похожие элементы на char с переменной text c помощью генераторов
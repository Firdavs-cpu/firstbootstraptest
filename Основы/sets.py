# списки - изменяемый тип данных []
# кортежи - не изменяемый ()

# множесто - - изменяемый тип с уникальными элементами{}
# frozenset(Замороженые свойства)

# my_set = {1,2,3,4,4}
# set() - конвертация во множество
# print (my_set)

# text = input('Введите текст - ')
# text2 = set(text)
# print(f'Количество уникальных букв - {len(text2)}')

text = input('Введите числа - ').split()
number_list = list(map(int,text))
print(sum(set(number_list)))

# names = {'Карим','Азиз','Шердос','Фирдавс'}
# name = input()
# if not(name in names):
#     names.add(name)
# else:
#     names.remove(name)
# print(names)




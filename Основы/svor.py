a = float(input('Введите первое число - '))
b = float(input('Введите второе число - '))
operation = input('Введите операцию "+, -, *, /, - ') 

if operation == '+':
    print(a+b)
elif operation == '-':
    print(a-b)
elif operation == '*':
    print(a*b)
elif operation == '/':
    print(a/b)
else:
    print("ERROR")



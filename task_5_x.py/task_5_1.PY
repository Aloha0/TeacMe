sum = 0
x = int(input(': '))
y = int(input(': '))
sign = input('Введите знак')
z = 0
for i in sign:
    if sign == '*':
        print(x * y)
    elif sign == '/':
        print(x / y)
    elif sign == '+':
        print(x + y)
    elif sign == '-':
        print(x - y)
    else:
        print('Ошибка')

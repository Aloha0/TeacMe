n = int(input('Количество гостей '))
if n >=50:
    print('Ресторан')
elif n >=20 and n<50:
    print('Кафе')
elif n <20:
    print('дом')
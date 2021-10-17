
sa = input('Введите строку: ')
midl = int(len(sa) / 2)

if sa[midl] == sa[0]:
    print(sa[1:-1])
else:
    print('no')

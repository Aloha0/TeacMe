'''2. Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь с ключами удвоенной
длины. {‘abc’: 5} -> {‘abcabc’: 5}'''

'''func = lambda x,y: {x*2: y} # c неопределенным кол-вом не понял как сделать
print(func('reg',5,))'''

func = ((lambda *kwargs: {i*2 for i,v in kwargs.items()}) # Не понял как сделать неопр количество аргументов
print(func('dbs','sbfdb','dbd','dbsfb'))  

#Перевод из дюймов в см

def dm(a):
    return a * 2.54

#Перевод из смс в дюймы
def cm(a):
   return a / 2.54
   
#3. Мили в километры 
def mil(a):
    return a / 0.621371


def km(a):
    return a * 0.621371


def ft(a):
    return a / 2.20462
    


def kg(a):
    return a * 2.20462
    

def un(a):
    return a / 0.035274
    

def gr(a):
    return a * 0.035274
    
def gl(a):
    return a / 0.264172
    
def ltr(a):
    return a * 0.264172
    
def pnt(a):
    return a / 2.11338

def litr(a):
    return a * 2.11338
    
#########################################
'''2. Написать программу, со следующим интерфейсом: пользователю предоставляется на
выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
от одного до двенадцати. После программа запрашивает ввести численное значение.
Затем программа выдает конвертированный результат. Использовать функции из первого
задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”'''
while True:
    n = int(input('Выберите вариант перевода: '))
    if n == 0:
        break
    a = int(input('Выберите цифру: '))
    if n == 1:
        print(dm(a))
    elif n == 2:
        print(cm(a))
    elif n == 3:
        print(mil(a))
    elif n == 4:
        print(km(a))
    elif n == 5:
        print(ft(a))
    elif n == 6:
        print(kg(a))
    elif n == 7:
        print(un(a))
    elif n == 8:
        print(gr(a))
    elif n == 9:
        print(gl(a))
    elif n == 10:
        print(ltr(a))
    elif n == 11:
        print(pnt(a))
    elif n == 12:
        print(litr(a))
    else:
        print('Ошибка!')
        print('Введенные данные не корректны, попробуйте еще раз.')
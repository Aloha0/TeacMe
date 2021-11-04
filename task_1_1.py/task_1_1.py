#1 задание
from math import sqrt


a = 24
b = 9

summ = a + b
razn = a - b
proizv = a * b
print(razn)

#2 задание
x = 20
y = 5

x_y = (abs(x) - abs(y)) / (1 + abs(x * y))  #0.1485148514851485
print(x_y)
#3 задание

rebro = 6
v = rebro ** 3 #объем куба 216
s = 4 * rebro ** 2 #площадь его боковой поверхности. 144

#4 задание

arifm = (x + y)/2 #12.5
geometr = pow(x * y, 0.5) # 10.0

#5 задание

katet_1 = 8
katet_2 = 6
gipotenuza = pow((katet_1 ** 2) + (katet_2 ** 2), 0.5) #10
s_treug = katet_1 + katet_2 + gipotenuza #24

prim = abs(5) + abs(-5)
print(prim)

firstname = 'Артем'
lastname = 'Станулевич'
age = '24'

result_1 = 'Привет, меня зовут {1} {0} мне {2} лет'.format(firstname, lastname, age)
print(result_1)
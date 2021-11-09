n =int(input(': '))
sum = 0
proizv = 1

while n > 0:
    dig = n % 10 # извлекаем последнюю цифру n
    sum = sum + dig
    proizv = proizv * dig
    n = n//10 #уменьшаем число на 1 разряд
print(sum)
print(proizv)


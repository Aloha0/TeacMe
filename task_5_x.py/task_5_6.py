'''import random
n = int(input(''))
tm = [random.randint(1,9) for i in range(n)]
for a, i in enumerate(tm):
    if a == len(tm) - 1:
        print(tm)
        break'''
'''import random
list = [random.randint(0, 9) for el in range(20)]
print(list)
for i, el in enumerate(list):
    print(el)
    if i == len(list) - 1:
        break'''
## решаем в классе


index_s = 0
index_f = 0

tm = []
ls = [1,2,3,4,5,4,3,2,4,5,6]      

for i in range(len(ls)-1):
    if ls[i]< ls[i+1]:
        if i + 1 == len(ls)-1:
            index_f = i+1
            tm.append((index_s, index_f))
    else:
        index_f = i
        tm.append((index_s, index_f))
        index_s = i+1

print(tm)
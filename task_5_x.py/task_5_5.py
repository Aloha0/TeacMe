import random
n = 19
m = [random.randint(1,8) for i in range(n)]
print(m)
b = max(m)
print(b)
for i in range(n):
    if i %2 == 0:
        m[i]= b
print(m)
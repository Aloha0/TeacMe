a = {'test':'test_value','europe':'eur', 'dollar':'usd', 'ruble':'rub'}
for i in a.keys():
    a[i] = (i + str(len(i)))
    print(i)
print(a)



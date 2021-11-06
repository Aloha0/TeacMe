n=['hhhhhh','World','hello','123321']
def palin(n):
    for i in n:
        if i == i[::-1]:
            print(i)    
        else:
            print('False')
    return n
palin(n)
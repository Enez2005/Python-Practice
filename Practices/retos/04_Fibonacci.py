a = 0
b = 1

for repite in range(10000):
    if a == 0 and b == 1:
        print(a,b)
        a += b
        b += a
       
    else:
        print(a,b)
        a += b
        b += a
       
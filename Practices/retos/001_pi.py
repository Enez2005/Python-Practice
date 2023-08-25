L = 100000000
aux = 0
for n in range(1,L,4):
    aux += 8 / (n*(n+2))

print(aux)
unordered = [9,4,5,6,10,2,3,4,5,2,3,4,5,51,34,61,7,1,8]

contador = 0

print(unordered)

while contador < len(unordered)-1:
    contador = 0
    for aux in range(len(unordered)-1):
        if unordered[aux] > unordered[aux + 1]:
            x = unordered[aux]
            unordered[aux] = unordered[aux + 1]
            unordered[aux + 1] = x

            print(unordered)

        elif unordered[aux] <= unordered[aux + 1]:
            contador += 1
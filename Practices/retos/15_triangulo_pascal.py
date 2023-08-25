temp = 0
temp2 = 0
x = 1
triangulo = [1]
z = -2
auxz = -2
rango_triangulo = 30

for aux in range(1, rango_triangulo):

    if len(triangulo) < 3:
        triangulo.append(1)
    else:
        triangulo.append(1)
        for aux2 in range(aux - 2):
            triangulo.append(triangulo[aux + aux2 + z] + triangulo[aux + aux2 + z + 1])
            auxz += 1
        triangulo.append(1)
        z = auxz


for elements in range(rango_triangulo - 1):
    temp = temp + elements
    temp2 = temp2 + elements + 1

    print(triangulo[temp : temp2])
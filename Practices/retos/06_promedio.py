""" print("Indroduce la cantidad de valores a promediar: ")

array_cantidad = int(input())
array = []
resultado = 0

print("Introduce los diferentes valores de tu promedio")

for cantidad in range(array_cantidad):
    array.append(input())

for cantidad in range(array_cantidad):
    resultado = resultado + int(array[cantidad])

print(f"El promedio de {array} es:")

print(resultado / array_cantidad)   """

def _sum(array: list):
    aux = 0
    for index in range(len(array)):
        aux += array[index]
    return aux

def _len(array: list):
    aux = 0
    for _ in array:
        aux += 1
    return aux

array = [1, 2, 3, 4, 5]
average = _sum(array) / _len(array)
print("average: ", average)
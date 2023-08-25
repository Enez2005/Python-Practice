print("Indroduce la cantidad de valores de tu array: ")

array_cantidad = int(input())
array = []
resultado = 0

print("Introduce los diferentes valores de tu array")

for cantidad in range(array_cantidad):
    array.append(input())

for cantidad in range(array_cantidad):
    resultado = resultado + int(array[cantidad])

print(f"La suma de {array} es:")

print(resultado)  
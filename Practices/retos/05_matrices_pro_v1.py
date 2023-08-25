print("Introduce la cantidad de filas, y despues la cantidad de columnas de la matriz\n"
      "===========================================================Recuerda===========================================================\n"
      "Para sumar o restar matrices las dos tienen que tener el mismo numero de filas y de columnas\n"
      "Para multiplicar se cumple la regla anterior o la matriz 1 tiene que tener el mismo número de filas que columnas de la matriz\n"
      "y el mismo numero de columnas que filas de la matriz 2\n"
      "==============================================================================================================================")

filas1 = int(input())
columnas1 = int(input())
print("==============================================================================================================================")
filas2 = int(input())
columnas2 = int(input())

matriz1 = []
matriz2 = []
matriz_r = []

if filas1 == filas2 and columnas1 == columnas2:
    print("A tus matrices las puedes sumar, restar o multiplicar, elige una opcion enviando un número.\n1.-Suma\n2.-Resta\n3.-Multiplicación")
    menu = int(input())
    if menu == 1:
        print(f"Tu primera matriz tiene {filas1} filas y {columnas1} columnas, por lo tanto necesita {filas1 * columnas1} datos en cada matriz")
        for datos in range(filas1 * columnas1):
            matriz1.append(int(input()))
        print(f"Tu segunda matriz necesita la misma cantidad de datos ({filas2 * columnas2})")
        for datos in range(filas2 * columnas2):
            matriz2.append(int(input()))
        for datos in range (filas1 * columnas1):
            matriz_r.append(matriz1[datos] + matriz2[datos])
        print(f"El resultado de tu Suma fue:\n")
        x = 0
        for resultado in range (filas1):
            print(matriz1[x:x+columnas1])
            x += columnas1
            
        print("+")
        x = 0
        for resultado in range (filas1):
            print(matriz2[x:x+columnas1])
            x += columnas1

        print("=")
        x = 0
        for resultado in range (filas1):
            print(matriz_r[x:x+columnas1])
            x += columnas1

    elif menu == 2:
        print(f"Tu primera matriz tiene {filas1} filas y {columnas1} columnas, por lo tanto necesita {filas1 * columnas1} datos en cada matriz")
        for datos in range(filas1 * columnas1):
            matriz1.append(int(input()))
        print(f"Tu segunda matriz necesita la misma cantidad de datos ({filas2 * columnas2})")
        for datos in range(filas2 * columnas2):
            matriz2.append(int(input()))
        for datos in range (filas1 * columnas1):
            matriz_r.append(matriz1[datos] - matriz2[datos])
        print(f"El resultado de tu Resta fue:\n")
        x = 0
        for resultado in range (filas1):
            print(matriz1[x:x+columnas1])
            x += columnas1
            
        print("+")
        x = 0
        for resultado in range (filas1):
            print(matriz2[x:x+columnas1])
            x += columnas1

        print("=")
        x = 0
        for resultado in range (filas1):
            print(matriz_r[x:x+columnas1])
            x += columnas1

    elif menu == 3:
        print(f"Tu primera matriz tiene {filas1} filas y {columnas1} columnas, por lo tanto necesita {filas1 * columnas1} datos en cada matriz")
        
    else:
        print("No se ha ingresado una opcion valida.")

elif filas1 == columnas2 and columnas1 == filas2:
    print("Por las dimensiones dadas, solamente puedes multiplicar")
    print(f"Tu primera matriz tiene {filas1} filas y {columnas1} columnas, por lo tanto necesita {filas1 * columnas1} datos en cada matriz")
else:
    print("No se han seguido las reglas dadas al principio, no se puede hacer nada.")

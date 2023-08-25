resultado = "No hay resultado"

print("Escribe el primer número")
primer_input = int(input())

print("Tu primer número es", primer_input,"\nAhora introduce el segundo número")
segundo_input = int(input())

print("Tu Segundo número es", segundo_input)

print("Accede a una opcion mediante un numero\n1.-Suma\n2.-Resta\n3.-Multiplicacion\n4.-Division")

menu_de_opciones = int(input())



if menu_de_opciones == 1:
    resultado = int(primer_input) + int(segundo_input)
    print(primer_input,"+",segundo_input, "=", resultado)
elif menu_de_opciones == 2:
    resultado = int(primer_input) - int(segundo_input)
    print(primer_input,"-",segundo_input, "=", resultado)
elif menu_de_opciones == 3:
    resultado = int(primer_input) * int(segundo_input)
    print(primer_input,"x",segundo_input, "=", resultado)
elif segundo_input == 0 and menu_de_opciones == 4 :
    print("No puedes dividir entre 0")
elif not segundo_input == 0 and menu_de_opciones == 4 :
    resultado = int(primer_input) / int(segundo_input)
    print(primer_input,"/",segundo_input, "=", resultado)

else: print("Esa no era una opcion")

print("El calculo ha terminado")


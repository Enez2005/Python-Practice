# creacion de variables

my_string_variable = "My string variable"
my_int_variable = 3
my_float_variable = 5.3
my_bool_variable = False
palabra_juego = "La palabra aun no ha sido asignada"


print(my_string_variable)
print(my_int_variable)
print(my_float_variable)
print(my_bool_variable)

#para aumentar al Print usar ","

print(my_string_variable, my_int_variable, my_bool_variable )

#convierte del tipo int a str
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

#test de comando de funcion
print(len(my_int_to_str_variable)) #len cuenta el numero de caracteres que me va a devolver

#variables en una sola linea (no hacer esto)
texto, numero, decimal = "hola", 4, 0.2 #para nombrar multiples variables: nombrarlas consecutivamente, darles valor consecutivo 
print(texto, numero, decimal)

#input solicita por un valor
print(palabra_juego)
palabra_juego = input("dime una palabra: ")
print("La palabra", palabra_juego,"tiene", len(palabra_juego),"letras.")
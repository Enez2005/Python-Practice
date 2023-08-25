# Strings

my_string = "Mi String"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea" # \n permite saltos de linea
print(my_new_line_string)

my_tab_string = "\t Este es un string con tabulacion" # \t permite tabulacion
print(my_tab_string)

my_scape_string = "Para hacer tabulacion usar \\t y para hacer salto de linea usar \\n" # \\ permite cancelar la accion y escribir con ella
print(my_scape_string)

# Formateo

name, surname, age = "Esteban", "Eguiguren", 17

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # Usando este formato es mas sencillo saber el tipo correcto
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #mejor manera para no usar formato

# Desempaquetado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(b)

# Division

language_slice = language [1:3]
print(language_slice)

language_slice = language [1:] # Le dice que caracteres mostrar desde donde hasta donde n:n
print(language_slice)

language_slice = language [0:6:2]
print(language_slice)

#Reverse

reversed_language = language[::-1] # ::-1 revierte todo
print(reversed_language)

#funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.upper().isupper())
print(language.startswith("py"))


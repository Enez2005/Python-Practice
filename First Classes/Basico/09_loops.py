# Loops! :D

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
if my_condition == 10:
    print("my_condition Es igual a 10")
    
else: #Es opcional  
    print("my_condition Es mayor a 10")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condicion es 15")
        break

    print(my_condition)
    
print("La ejecucion continua")

#For

my_list = [12, 23, 35, 54, 45, 32, 45]

for element in my_list:
    print(element)

my_tuple = (17, 1.75, "Esteban", "Eguiguren", "Sin nombre")
for element in my_tuple:
    print(element)

my_set = {"Esteban","Eguiguren", 17}
for element in my_set:
    print(element)

my_dict = {"Nombre":"Esteban","Apellido":"Eguiguren","Edad":17, "Lenguajes": {"Python","Swift","Kotlin"}, 1:1.75 }
for element in my_dict:
    print(my_dict)

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for a terminado")

print("La ejecucion continua")

# Diccionarios

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Esteban","Apellido":"Eguiguren","Edad":17, 1: "Python"}
my_dict = {"Nombre":"Esteban",
           "Apellido":"Eguiguren",
           "Edad":17,
            "Lenguajes": {"Python","Swift","Kotlin"},
            1:1.75
            }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))
print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Paris"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Eguiguren" in my_dict)
print("Apellido" in my_dict)
print("Eguiguren" in my_dict["Apellido"] )

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre",1, "Piso"]
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre",1, "Piso"))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, 0)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_list, "Enez")


my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values)
print(dict.fromkeys(list(my_new_dict.values())))
print(tuple(my_new_dict))
print(set(my_new_dict))


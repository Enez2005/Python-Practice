#listas

my_list = list()
my_other_list = []

print(len(my_list))
print(len(my_other_list))

my_list = [12, 23, 35, 54, 45, 32, 45]

print(my_list)
print(len(my_list))

my_other_list = [17, 1.77,  "Esteban", "Eguiguren"]

print(type(my_other_list))
print(type(my_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_other_list.count("Esteban"))
print(my_list.count(45))
#print(my_other_list[-5]) Index Error
#print(my_other_list[4])  Index Error

age, height, name, surname = my_other_list
print(name)

name, surname, age, height = my_other_list[2], my_other_list[3], my_other_list[0], my_other_list[1]
print(name)
print(age)

print(my_list + my_other_list)
print(my_list, my_other_list)


my_other_list.append("sysdeco")
print(my_other_list)

my_other_list.insert(1, "Azul")
print(my_other_list)

my_other_list[1] = "Verde"
print(my_other_list)

my_other_list.remove("Verde")
print(my_other_list)

my_list.remove(45)
print(my_list)

my_list.pop()
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3   ])

"""
my_list = "Hola Python"
print(my_list)
print(type(my_list))

# Recordar, al ser dinamico cambia lo que es, es debilmente typado

my_list = ["Hola Python"]
print(my_list)
print(type(my_list))
"""
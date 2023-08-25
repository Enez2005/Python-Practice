# Tuples

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (17, 1.75, "Esteban", "Eguiguren", "Sin nombre")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4])  Index Error
#print(my_tuple[-6]) Index Error

print(my_tuple.count("Esteban"))
print(my_tuple.index("Eguiguren"))

#my_tuple[1] = 1.80
#print(my_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Sysdeco"
my_tuple.insert(1, "Verde")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#del my_tuple           La variable es eliminada
#print(my_tuple)

# Las tuplas son inmutables, las listas son mutables
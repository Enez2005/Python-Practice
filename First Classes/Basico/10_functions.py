# Funciones

def my_function ():
    print("Esto es una funcion")

my_function()
my_function()
my_function()

def sum_two_values (first_value, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(5, 12)
sum_two_values("7","5")
sum_two_values(5.8, 12.3)

def sum_two_values_with_return (first_value, second_value):
    return first_value + second_value

sum_two_values_with_return(10, 5)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def sum_two_values (first_value, second_value):
    sum_result = first_value + second_value
    return sum_result

def print_name(name, surname):
    print(f"{name} {surname}")  

print_name (surname="Eguiguren",name="Esteban")

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default ("Esteban", "Eguiguren") 
print_name_with_default ("Esteban", "Eguiguren", "Enez")

def print_upper_texts (*texts):
    for element in texts:
        print(element.upper())

print_upper_texts("Hola","python", "Esteban")
print_upper_texts("Hola")
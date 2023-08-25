# Clases

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = "Sin Alias"):
        self.full_name = f"{name} {surname} ({alias})"
        self.__name = name
        self.__surname = surname

    def get_name(self):
        return self.__name #propiedad privada

    def walk(self):
        print(f"{self.full_name} esta caminando")
    


my_person = Person("Esteban","Eguiguren")
print(my_person.full_name)
print(my_person.get_name())

my_person.walk()

my_other_person = Person("Esteban","Eguiguren", "Enez")

print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Hector de leon (El loco de los perros)"
print(my_other_person.full_name)
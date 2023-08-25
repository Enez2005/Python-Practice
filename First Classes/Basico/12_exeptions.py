# Exception Handling
number_one, number_two = 5, 1

number_two = "1"

try:
    print(number_one + number_two)
except:
    print("No se logró la accion")
else:
    # Se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")
finally:
    print("La ejecucion continua")

#captura de excepciones por tipo

try:
    print(number_one + number_two)
except TypeError:
    print("No se logró la accion TypeError")

#captura de la informacion de excepcion
try:
    print(number_one + number_two)
except ValueError as e:
    print(e)
except Exception as exception:
    print(exception)


lista = [12, 23, 52, 32 , 54, 43, 52, 55, 34, 64, 52, 52, 52, 52]

cantidad_elementos = len(lista)

variable = 52

cantidad_variable = lista.count(variable)

print(f"Hay una probablidad de {cantidad_variable / cantidad_elementos * 100}% que se eliga {variable} dentro de la lista")

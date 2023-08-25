palabra = "test"
palabra_separada = []
palabra_oculta = []
errores = 0
aux = len(palabra)

for x in range(aux):
    palabra_separada.append(palabra[x])
    palabra_oculta.append("_")

def jugar(palabra_separada, palabra_oculta, errores):
    eleccion = input()

    if eleccion in palabra_separada:
        aux = [i for i, x in enumerate(palabra_separada) if x == eleccion]

        for elements in aux:
            palabra_oculta[elements] = palabra_separada[elements]


        return palabra_separada, palabra_oculta, errores
    else:
        errores += 1

        
        return palabra_separada, palabra_oculta, errores

while errores <= 7:
    if not palabra_oculta == palabra_separada:
        if errores == 0:
            print("Introduce una letra:")
            palabra_separada, palabra_oculta, errores = jugar(palabra_separada, palabra_oculta, errores)
            print(errores)

        elif errores == 1:
            print("  +------------------\n"
                "  |                 |\n"
                "  |           \n"
                "  |            \n"
                "  |             \n"
                "  |                 \n"
                "  |             \n"
                "  |                   \n"
                "  |                \n"
                "  |              \n"
                "-----\n"
                "Introduce una letra: ")
            palabra_separada, palabra_oculta, errores = jugar(palabra_separada, palabra_oculta, errores)
            print(palabra_oculta)
        elif errores == 2:
            print("  +------------------\n"
                "  |                 |\n"
                "  |               +---+\n"
                "  |               |   |\n"
                "  |               +-+-+\n"
                "  |                 \n"
                "  |             \n"
                "  |                 \n"
                "  |                \n"
                "  |               \n"
                "-----\n"
                "Introduce una letra: ")
            palabra_separada, palabra_oculta, errores = jugar(palabra_separada, palabra_oculta, errores)
            print(palabra_oculta)
        elif errores == 3:
            print("  +------------------\n"
                "  |                 |\n"
                "  |               +---+\n"
                "  |               |   |\n"
                "  |               +-+-+\n"
                "  |                 |\n"
                "  |                 +\n"
                "  |                 |  \n"
                "  |                \n"
                "  |               \n"
                "-----\n"
                "Introduce una letra: ")
            palabra_separada, palabra_oculta, errores = jugar(palabra_separada, palabra_oculta, errores)
            print(palabra_oculta)
        elif errores == 4:
            print("  +------------------\n"
                "  |                 |\n"
                "  |               +---+\n"
                "  |               |   |\n"
                "  |               +-+-+\n"
                "  |                 |\n"
                "  |             ----+\n"
                "  |                 |  \n"
                "  |                \n"
                "  |               \n"
                "-----\n"
                "Introduce una letra: ")
            palabra_separada, palabra_oculta, errores = jugar(palabra_separada, palabra_oculta, errores)
            print(palabra_oculta)
        elif errores == 5:
            print("  +------------------\n"
                "  |                 |\n"
                "  |               +---+\n"
                "  |               |   |\n"
                "  |               +-+-+\n"
                "  |                 |\n"
                "  |             ----+----\n"
                "  |                 |  \n"
                "  |                \n"
                "  |               \n"
                "-----\n"
                "Introduce una letra: ")
            palabra_separada, palabra_oculta, errores = jugar(palabra_separada, palabra_oculta, errores)
            print(palabra_oculta)
        elif errores == 6:
            print("  +------------------\n"
                "  |                 |\n"
                "  |               +---+\n"
                "  |               |   |\n"
                "  |               +-+-+\n"
                "  |                 |\n"
                "  |             ----+----\n"
                "  |                 |  \n"
                "  |                / \n"
                "  |               /   \n"
                "-----\n"
                "Introduce una letra: ")
            palabra_separada, palabra_oculta, errores = jugar(palabra_separada, palabra_oculta, errores)
            print(palabra_oculta)
        elif errores == 7:
            print("  +------------------\n"
                "  |                 |\n"
                "  |               +---+\n"
                "  |               |x x|\n"
                "  |               +-+-+\n"
                "  |                 |\n"
                "  |             ----+----\n"
                "  |                 |  \n"
                "  |                / \\\n"
                "  |               /   \\\n"
                "-----\n"
                "Perdiste :(")
            break
    elif palabra_oculta == palabra_separada:
        print("Has Ganado! ")
        break
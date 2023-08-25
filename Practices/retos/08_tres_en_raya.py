
p1, p2, p3, p4, p5, p6, p7, p8, p9 = 1, 2, 3, 4, 5, 6, 7, 8, 9

controlador = 0
cursor = 0

print("\nX Comienza, elige un numero para colocar")

def imagen(p1, p2, p3, p4, p5, p6, p7, p8, p9):

    print("_____________")
    print(f"| {p1} | {p2} | {p3} |")
    print(f"|---|---|---|")
    print(f"| {p4} | {p5} | {p6} |")
    print(f"|---|---|---|")
    print(f"| {p7} | {p8} | {p9} |")
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯")
    return p1, p2, p3, p4, p5, p6, p7, p8, p9

imagen(p1, p2, p3, p4, p5, p6, p7, p8, p9)

while p1 == 1 or p2 == 2 or p3 == 3 or p4 == 4 or p5 == 5 or p6 == 6 or p7 == 7 or p8 == 8 or p9 == 9:
    cursor = int(input())
    if cursor == 1 and controlador == 0 and type(p1) == int:
        p1 = "x"
        imagen(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print("Tu turno O")
        controlador = 1
    elif cursor == 1 and controlador == 1 and type(p1) == int:
        p1 = "o"
        imagen(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print("Tu turno x")
        controlador = 0
    elif cursor == 2 and controlador == 0 and type(p2) == int:
        p2 = "x"
        imagen(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print("Tu turno O")
        controlador = 1
    elif cursor == 2 and controlador == 1 and type(p2) == int:
        p2 = "o"
        imagen(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print("Tu turno x")
        controlador = 0
    elif cursor == 3 and controlador == 0 and type(p3) == int:
        p3 = "x"
        imagen(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print("Tu turno O")
        controlador = 1
    elif cursor == 2 and controlador == 1 and type(p3) == int:
        p3 = "o"
        imagen(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print("Tu turno x")
        controlador = 0
    elif cursor == 4 and controlador == 0 and type(p4) == int:
        p4 = "x"
        imagen(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print("Tu turno O")
        controlador = 1
    elif cursor == 4 and controlador == 1 and type(p4) == int:
        p4 = "o"
        imagen(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print("Tu turno x")
        controlador = 0
    elif cursor == 5 and controlador == 0 and type(p5) == int:
        p5 = "x"
        imagen(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print("Tu turno O")
        controlador = 1
    elif cursor == 5 and controlador == 1 and type(p5) == int:
        p5 = "o"
        imagen(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print("Tu turno x")
        controlador = 0
    elif cursor == 6 and controlador == 0 and type(p6) == int:
        p6 = "x"
        imagen(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print("Tu turno O")
        controlador = 1
    elif cursor == 6 and controlador == 1 and type(p6) == int:
        p6 = "o"
        imagen(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print("Tu turno x")
        controlador = 0
    elif cursor == 7 and controlador == 0 and type(p7) == int:
        p7 = "x"
        imagen(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print("Tu turno O")
        controlador = 1
    elif cursor == 7 and controlador == 1 and type(p7) == int:
        p7 = "o"
        imagen(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print("Tu turno x")
        controlador = 0
    elif cursor == 8 and controlador == 0 and type(p8) == int:
        p8 = "x"
        imagen(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print("Tu turno O")
        controlador = 1
    elif cursor == 8 and controlador == 1 and type(p8) == int:
        p8 = "o"
        imagen(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print("Tu turno x")
        controlador = 0
    elif cursor == 9 and controlador == 0 and type(p9) == int:
        p9 = "x"
        imagen(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print("Tu turno O")
        controlador = 1
    elif cursor == 9 and controlador == 1 and type(p9) == int:
        p9 = "o"
        imagen(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print("Tu turno x")
        controlador = 0
    else:
        print("Esa casilla ya habia sido elegida, o no es una opcion")
        imagen(p1, p2, p3, p4, p5, p6, p7, p8, p9)

    if p1 == "x" and p2 == "x" and p3 == "x":
        print("Ha ganado X")
        break
    elif p4 == "x" and p5 == "x" and p6 == "x":
        print("Ha ganado X")
        break
    elif p7 == "x" and p8 == "x" and p9 == "x":
        print("Ha ganado X")
        break
    elif p1 == "x" and p4 == "x" and p7 == "x":
        print("Ha ganado X")
        break
    elif p2 == "x" and p5 == "x" and p8 == "x":
        print("Ha ganado X")
        break
    elif p3 == "x" and p6 == "x" and p9 == "x":
        print("Ha ganado X")
        break
    elif p1 == "x" and p5 == "x" and p9 == "x":
        print("Ha ganado X")
        break
    elif p7 == "x" and p5 == "x" and p3 == "x":
        print("Ha ganado X")
        break

    if p1 == "o" and p2 == "o" and p3 == "o":
        print("Ha ganado O")
        break
    elif p4 == "o" and p5 == "o" and p6 == "o":
        print("Ha ganado O")
        break
    elif p7 == "o" and p8 == "o" and p9 == "o":
        print("Ha ganado O")
        break
    elif p1 == "o" and p4 == "o" and p7 == "o":
        print("Ha ganado O")
        break
    elif p2 == "o" and p5 == "o" and p8 == "o":
        print("Ha ganado O")
        break
    elif p3 == "o" and p6 == "o" and p9 == "o":
        print("Ha ganado O")
        break
    elif p1 == "o" and p5 == "o" and p9 == "o":
        print("Ha ganado O")
        break
    elif p7 == "o" and p5 == "o" and p3 == "o":
        print("Ha ganado O")
        break


print("El juego ha terminado")




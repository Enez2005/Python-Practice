def menu1():
    print("-------------------------------------------")
    print("Accede a una opcion mediante un numero\n1.-Inicio\n2.-Opciones\n3.-Creditos\n4.-Salir")
    menu_de_opciones_1 = int(input())
    
    if menu_de_opciones_1 == 1:
        print("En Mantenimiento")
        menu1()
    if menu_de_opciones_1 == 2:
        menu2()
    if menu_de_opciones_1 == 3:
        print("En Mantenimiento")
        menu1()
    if menu_de_opciones_1 == 4:
        return
    else:
        print("Esa no era una opcion")
        menu1()

def menu2():
        print("1.-Volumen \n2.-Imagen\n3.-Gpu\n4.-Volver")
        menu_de_opciones_2 = int(input())

        if menu_de_opciones_2 == 1:
            menu3()
        elif menu_de_opciones_2 == 2:
            print("En Mantenimiento")
            menu2()
        elif menu_de_opciones_2 == 3:
            print("En Mantenimiento")
            menu2()
        elif  menu_de_opciones_2 == 4:
            menu1()
        else: print("Esa no era una opcion")

def menu3():
            print("1.-Subir \n2.-Bajar\n3.-Volver")
            menu_de_opciones_2 = int(input())

            if menu_de_opciones_2 == 1:
                print("En Mantenimiento")
                menu3()
            elif menu_de_opciones_2 == 2:
                print("En Mantenimiento")
                menu3()
        
            elif menu_de_opciones_2 == 3:
                menu2()

            
            else: 
                print("Esa no era una opcion")
                menu3()

menu1()
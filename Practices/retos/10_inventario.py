on = True

ids = []
nombre_productos = []
precio_productos = []

items = {"ID": ids, "Nombre" :nombre_productos, "Precio": precio_productos}

def agregar(ids, nombre_productos, precio_productos):

    id_confirmar = 1

    while not id_confirmar  == "":
        print("Introduce el Nombre de tu producto")
        aux = input()
        print(f"El Nombre de tu producto es {aux}")
        print("Confirma presionando la tecla enter\n"
              "Presiona cualquier otra tecla para volver a iniciar")
        id_confirmar = input()
    
    nombre_productos.append(aux)
    print("-----------------------------------\n"
          "------------Confirmado-------------\n"
          "-----------------------------------\n")

    id_confirmar = 1

    while not id_confirmar  == "":
        print("Introduce el Precio de tu producto")
        aux = input()
        print(f"El Precio de tu producto es {aux}")
        print("Confirma presionando la tecla enter\n"
              "Presiona cualquier otra tecla para volver a iniciar")
        id_confirmar = input()
    
    precio_productos.append(aux)
    print("-----------------------------------\n"
          "------------Confirmado-------------\n"
          "-----------------------------------\n")
    try:
      x = ids[-1] + 1
    except:
      x = 1    
    
    ids.append(x)
      
    print(f"ID: {ids[-1]}, Nombre: {nombre_productos[-1]}, Precio: {precio_productos[-1]}\n")
    
    return ids, nombre_productos, precio_productos

def eliminar(ids, nombre_productos, precio_productos):

      id_confirmar = 0

      while not id_confirmar == "1":
            print("Para eliminar un item escribe su ID o Nombre")
            aux = input()
            try:
                  aux = int(aux)
            except:
                  pass
            if aux in ids:
                  aux2 = ids.index(aux)
                  print(f"Deseas eliminar {nombre_productos[aux2]} con ID: {ids[aux2]}?\n"
                  "1.- Si\n"
                  "2.- No\n")
                  id_confirmar = input()
                  if id_confirmar == "2":
                       return
            elif aux in nombre_productos:
                  aux2 = nombre_productos.index(aux)
                  print(f"Deseas eliminar {nombre_productos[aux2]} con ID: {ids[aux2]}?\n"
                  "1.- Si\n"
                  "2.- No\n")
                  id_confirmar = input()
                  if id_confirmar == "2":
                       return
            else:
                  print("No se pudo encontrar el producto, revisa su id o nombre en la opcion de listar")
                  return       
      
      del ids[aux2]
      del nombre_productos[aux2]
      del precio_productos[aux2]
      
      return ids, nombre_productos, precio_productos     

def listar(ids, nombre_productos, precio_productos):
     print("ID | Nombre Producto | Precio ")

     aux = len(ids)

     for x in range (aux):
            print("---+-----------------+--------")
            aux2 = str(ids[x])
            ids_aux = aux2[:3]
            aux2 = nombre_productos[x]
            nombre_aux = aux2[:17]
            aux2 = precio_productos[x]
            precio_aux = aux2[:8]

            ids_rellenado = ids_aux.ljust(3)
            nombre_rellenado = nombre_aux.ljust(17)
            precio_rellenado = precio_aux.ljust(8)

            print(f"{ids_rellenado}|{nombre_rellenado}|${precio_rellenado}")

def revalorar(ids, nombre_productos, precio_productos):
      id_confirmar = 0
      while not id_confirmar == "1":
            print("Para cambiar el precio de un item escribe su ID o Nombre")
            aux = input()
            try:
                  aux = int(aux)
            except:
                  pass
            if aux in ids:
                  aux2 = ids.index(aux)
                  print(f"Deseas revalorar {nombre_productos[aux2]} con ID: {ids[aux2]}?\n"
                  "1.- Si\n"
                  "2.- No\n")
                  id_confirmar = input()
                  if id_confirmar == "2":
                       return
            elif aux in nombre_productos:
                  aux2 = nombre_productos.index(aux)
                  print(f"Deseas revalorar {nombre_productos[aux2]} con ID: {ids[aux2]}?\n"
                  "1.- Si\n"
                  "2.- No\n")
                  id_confirmar = input()
                  if id_confirmar == "2":
                       return
            else:
                  print("No se pudo encontrar el producto, revisa su id o nombre en la opcion de listar")
                  return       

      print(f"Introduce el nuevo valor de {nombre_productos[aux2]}")
      precio_productos[aux2] = input()
      
      return precio_productos


while on:
      print("\n+++++++++++++++++++++++++++++++++++\n"
            "BIENVENIDO AL SISTEMA DE INVENTARIO\n"
            "+++++++++++++++++++++++++++++++++++\n")
      print("1.- Agregar Nuevo Item\n"
            "2.- Eliminar un Item existente\n"
            "3.- Listar los items existentes\n"
            "4.- Revalorar\n"
            "5.- Salir\n")

      menu = int(input())

      if menu == 1:
            print("Para agregar un nuevo item tienes que dar su: Nombre y Precio")
            agregar(ids, nombre_productos, precio_productos)
      elif menu == 2:
 
            eliminar(ids, nombre_productos, precio_productos)
      elif menu == 3:
            listar(ids, nombre_productos, precio_productos)
      elif menu == 4:
            revalorar(ids, nombre_productos, precio_productos)
      elif menu == 5:
            break
      else:
            print("Esa no era una opcion, por favor vuelve a elegir")
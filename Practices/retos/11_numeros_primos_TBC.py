primos = [2, 3, 5]
no_primos = [1]

on = True

pl = len(primos)
n_pl = len(no_primos)
aux = 1
aux2 = 1

while on == True:
    for x in range(pl):
        for y in range(n_pl):
            aux = primos[x]*primos[x]
            
            if not aux in no_primos and aux < 500:
                no_primos.append(aux)
            
            for z in range(pl):
                aux = primos[x]*primos[z]

                if not aux in no_primos and aux < 500:
                    no_primos.append(aux)
            
            
            if not aux in no_primos and aux < 500:
                no_primos.append(aux)
          
            aux = primos[x]*no_primos[y]
            
            
            if not aux in no_primos and not aux in primos and aux < 500:
                no_primos.append(aux)
            
    for elements in range(pl*n_pl):
        aux2 += 1
        if not aux2 in no_primos and not aux2 in primos:
            primos.append(aux2)
            break


    
    print(primos)
    pl = len(primos)
    n_pl = len(no_primos)



# Funciona Pero Puedo Hacerlo más Eficaz 
#                                                          To Be Continued                                                          #
    
    
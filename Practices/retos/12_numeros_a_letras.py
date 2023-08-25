numero = input()
num_en_list = []

aux = 0

for x in range(len(numero)):
    num_en_list.append(numero[x])

def decimal1():
    if len(num_en_list) >= 2:
        if num_en_list[-1] == "0":
            des1 = ""
        elif num_en_list[-1] == "1":
            des1 = "uno"
        elif num_en_list[-1] == "2":
            des1 = "dos"
        elif num_en_list[-1] == "3":
            des1 = "tres"
        elif num_en_list[-1] == "4":
            des1 = "cuatro"
        elif num_en_list[-1] == "5":
            des1 = "cinco"
        elif num_en_list[-1] == "6":
            des1 = "seis"
        elif num_en_list[-1] == "7":
            des1 = "siete"
        elif num_en_list[-1] == "8":
            des1 = "ocho"
        elif num_en_list[-1] == "9":
            des1 = "nueve"
    return des1

def decimal2():
    if len(num_en_list) >= 3:
        if num_en_list[-2] == "0":
            des2 = ""
        if num_en_list[-2] == "1" and num_en_list[-1] == "0":
            des2 = "diez"
        elif num_en_list[-2] == "1" and num_en_list[-1] == "1":
            des2 = "once"
        elif num_en_list[-2] == "1" and num_en_list[-1] == "2":
            des2 = "doce"
        elif num_en_list[-2] == "1" and num_en_list[-1] == "3":
            des2 = "trece"
        elif num_en_list[-2] == "1" and num_en_list[-1] == "4":
            des2 = "catorce"
        elif num_en_list[-2] == "1" and num_en_list[-1] == "5":
            des2 = "quince"
        elif num_en_list[-2] == "1":
            des1 = decimal1()
            des2 = f"diesi{des1}"
        elif num_en_list[-2] == "2" and num_en_list[-1] == "0":
            des2 = "veinte"
        elif num_en_list[-2] == "2":
            des1 = decimal1()
            des2 = f"veinti{des1}"
        elif num_en_list[-2] == "3" and num_en_list[-1] == "0":
            des2 = "treinta"
        elif num_en_list[-2] == "3":
            des1 = decimal1()
            des2 = f"treinta y {des1}"
        elif num_en_list[-2] == "4" and num_en_list[-1] == "0":
            des2 = "cuarenta"
        elif num_en_list[-2] == "4":
            des1 = decimal1()
            des2 = f"cuarenta y {des1}"
        elif num_en_list[-2] == "5" and num_en_list[-1] == "0":
            des2 = "cincuenta"
        elif num_en_list[-2] == "5":
            des1 = decimal1()
            des2 = f"cincuenta y {des1}"
        elif num_en_list[-2] == "6" and num_en_list[-1] == "0":
            des2 = "sesenta"
        elif num_en_list[-2] == "6":
            des1 = decimal1()
            des2 = f"sesenta y {des1}"
        elif num_en_list[-2] == "7" and num_en_list[-1] == "0":
            des2 = "setenta"
        elif num_en_list[-2] == "7":
            des1 = decimal1()
            des2 = f"setenta y {des1}"
        elif num_en_list[-2] == "8" and num_en_list[-1] == "0":
            des2 = "ochenta"
        elif num_en_list[-2] == "8":
            des1 = decimal1()
            des2 = f"ochenta y {des1}"
        elif num_en_list[-2] == "9" and num_en_list[-1] == "0":
            des2 = "Noventa"
        elif num_en_list[-2] == "9":
            des1 = decimal1()
            des2 = f"noventa y {des1}"
    return des2    

def decimal3():
    if len(num_en_list) >= 3:
        if num_en_list[-3] == "0":
            des3 = ""
        elif num_en_list[-3] == "1" and num_en_list[-2] == "0" and num_en_list[-1] == "0":
            des3 = f"cien"
        elif num_en_list[-3] == "1" and num_en_list[-2] == "0":
            des1 = decimal1()
            des3 = f"ciento {des1}"
        elif num_en_list[-3] == "1":
            des2 = decimal2()
            des3 = f"ciento {des2}"
        elif num_en_list[-3] == "2" and num_en_list[-2] == "0" and num_en_list[-1] == "0":
            des3 = f"doscientos"
        elif num_en_list[-3] == "2" and num_en_list[-2] == "0":
            des1 = decimal1()
            des3 = f"doscientos {des1}"
        elif num_en_list[-3] == "2":
            des2 = decimal2()
            des3 = f"doscientos {des2}"
        elif num_en_list[-3] == "3" and num_en_list[-2] == "0" and num_en_list[-1] == "0":
            des3 = f"trescientos"
        elif num_en_list[-3] == "3" and num_en_list[-2] == "0":
            des1 = decimal1()
            des3 = f"trescientos {des1}"
        elif num_en_list[-3] == "3":
            des2 = decimal2()
            des3 = f"trescientos {des2}"
        elif num_en_list[-3] == "4" and num_en_list[-2] == "0" and num_en_list[-1] == "0":
            des3 = f"cuatrocientos"
        elif num_en_list[-3] == "4" and num_en_list[-2] == "0":
            des1 = decimal1()
            des3 = f"cuatrocientos {des1}"
        elif num_en_list[-3] == "4":
            des2 = decimal2()
            des3 = f"cuatrocientos {des2}"
        elif num_en_list[-3] == "5" and num_en_list[-2] == "0" and num_en_list[-1] == "0":
            des3 = f"quinientos"
        elif num_en_list[-3] == "5" and num_en_list[-2] == "0":
            des1 = decimal1()
            des3 = f"quinientos {des1}"
        elif num_en_list[-3] == "5":
            des2 = decimal2()
            des3 = f"quinientos {des2}"
        elif num_en_list[-3] == "6" and num_en_list[-2] == "0" and num_en_list[-1] == "0":
            des3 = f"seiscientos"
        elif num_en_list[-3] == "6" and num_en_list[-2] == "0":
            des1 = decimal1()
            des3 = f"seiscientos {des1}"
        elif num_en_list[-3] == "6":
            des2 = decimal2()
            des3 = f"seiscientos {des2}"
        elif num_en_list[-3] == "7" and num_en_list[-2] == "0" and num_en_list[-1] == "0":
            des3 = f"setecientos"
        elif num_en_list[-3] == "7" and num_en_list[-2] == "0":
            des1 = decimal1()
            des3 = f"setecientos {des1}"
        elif num_en_list[-3] == "7":
            des2 = decimal2()
            des3 = f"setecientos {des2}"
        elif num_en_list[-3] == "8" and num_en_list[-2] == "0" and num_en_list[-1] == "0":
            des3 = f"ochocientos"
        elif num_en_list[-3] == "8" and num_en_list[-2] == "0":
            des1 = decimal1()
            des3 = f"ochocientos {des1}"
        elif num_en_list[-3] == "8":
            des2 = decimal2()
            des3 = f"ochocientos {des2}"
        elif num_en_list[-3] == "9" and num_en_list[-2] == "0" and num_en_list[-1] == "0":
            des3 = f"novecientos"
        elif num_en_list[-3] == "9" and num_en_list[-2] == "0":
            des1 = decimal1()
            des3 = f"novecientos {des1}"
        elif num_en_list[-3] == "9":
            des2 = decimal2()
            des3 = f"novecientos {des2}"
    return des3

def decimal4():
    if len(num_en_list) == 4:
        if num_en_list[-4] == "1":
            des4 = "Mil"        
        elif num_en_list[-4] == "2":
            des4 = "Dos mil"
        elif num_en_list[-4] == "3":
            des4 = "Tres mil"
        elif num_en_list[-4] == "4":
            des4 = "Cuatro mil"
        elif num_en_list[-4] == "5":
            des4 = "Cinco mil"
        elif num_en_list[-4] == "6":
            des4 = "Seis mil"
        elif num_en_list[-4] == "7":
            des4 = "Siete mil"
        elif num_en_list[-4] == "8":
            des4 = "Ocho mil"
        elif num_en_list[-4] == "9":
            des4 = "Nueve mil"

    elif len(num_en_list) > 4:
        if num_en_list[-4] == "1":
            des4 = "un mil"  
        if num_en_list[-4] == "2":
            des4 = "dos mil"
        elif num_en_list[-4] == "3":
            des4 = "tres mil"
        elif num_en_list[-4] == "4":
            des4 = "cuatro mil"
        elif num_en_list[-4] == "5":
            des4 = "cinco mil"
        elif num_en_list[-4] == "6":
            des4 = "seis mil"
        elif num_en_list[-4] == "7":
            des4 = "siete mil"
        elif num_en_list[-4] == "8":
            des4 = "ocho mil"
        elif num_en_list[-4] == "9":
            des4 = "nueve mil"
    return des4

def decimal5():
    if len(num_en_list) == 5:
        if num_en_list[-5] == "1" and num_en_list[-4] == "0":
            des5 = "Diez mil"
        elif num_en_list[-5] == "1" and num_en_list[-4] == "1":
            des5 = "Once mil"
        elif num_en_list[-5] == "1" and num_en_list[-4] == "2":
            des5 = "Doce mil"
        elif num_en_list[-5] == "1" and num_en_list[-4] == "3":
            des5 = "Trece mil"
        elif num_en_list[-5] == "1" and num_en_list[-4] == "4":
            des5 = "Catorce mil"
        elif num_en_list[-5] == "1" and num_en_list[-4] == "5":
            des5 = "Quince mil"
        elif num_en_list[-5] == "1":
            des4 = decimal4()
            des5 = f"Diesi{des4}"
        elif num_en_list[-5] == "2" and num_en_list[-4] == "0":
            des5 = "Veinte mil"
        elif num_en_list[-5] == "2":
            des4 = decimal4()
            des5 = f"Veinti{des4}"
        elif num_en_list[-5] == "3" and num_en_list[-4] == "0":
            des5 = "Treinta mil"
        elif num_en_list[-5] == "3":
            des4 = decimal4()
            des5 = f"Treinta y {des4}"
        elif num_en_list[-5] == "4" and num_en_list[-4] == "0":
            des5 = "Cuarenta mil"
        elif num_en_list[-5] == "4":
            des4 = decimal4()
            des5 = f"Cuarenta y {des4}"
        elif num_en_list[-5] == "5" and num_en_list[-4] == "0":
            des5 = "Cincuenta mil"
        elif num_en_list[-5] == "5":
            des4 = decimal4()
            des5 = f"Cincuenta y {des4}"
        elif num_en_list[-5] == "6" and num_en_list[-4] == "0":
            des5 = "Sesenta mil"
        elif num_en_list[-5] == "6":
            des4 = decimal4()
            des5 = f"Sesenta y {des4}"
        elif num_en_list[-5] == "7" and num_en_list[-4] == "0":
            des5 = "Setenta mil"
        elif num_en_list[-5] == "7":
            des4 = decimal4()
            des5 = f"Setenta y {des4}"
        elif num_en_list[-5] == "8" and num_en_list[-4] == "0":
            des5 = "Ochenta mil"
        elif num_en_list[-5] == "8":
            des4 = decimal4()
            des5 = f"Ochenta y {des4}"
        elif num_en_list[-5] == "9" and num_en_list[-4] == "0":
            des5 = "Noventa mil"
        elif num_en_list[-5] == "9":
            des4 = decimal4()
            des5 = f"Noventa y {des4}"

    elif len(num_en_list) > 5:
        if num_en_list[-5] == "0":
            des5 = "mil"
        if num_en_list[-5] == "1" and num_en_list[-4] == "0":
            des5 = "diez mil"
        elif num_en_list[-5] == "1" and num_en_list[-4] == "1":
            des5 = "once mil"
        elif num_en_list[-5] == "1" and num_en_list[-4] == "2":
            des5 = "doce mil"
        elif num_en_list[-5] == "1" and num_en_list[-4] == "3":
            des5 = "trece mil"
        elif num_en_list[-5] == "1" and num_en_list[-4] == "4":
            des5 = "catorce"
        elif num_en_list[-5] == "1" and num_en_list[-4] == "5":
            des5 = "quince"
        elif num_en_list[-5] == "1":
            des4 = decimal4()
            des5 = f"diesi{des4}"
        elif num_en_list[-5] == "2" and num_en_list[-4] == "0":
            des5 = "veinte"
        elif num_en_list[-5] == "2":
            des4 = decimal4()
            des5 = f"veinti{des4}"
        elif num_en_list[-5] == "3" and num_en_list[-4] == "0":
            des5 = "treinta"
        elif num_en_list[-5] == "3":
            des4 = decimal4()
            des5 = f"treinta y {des4}"
        elif num_en_list[-5] == "4" and num_en_list[-4] == "0":
            des5 = "cuarenta"
        elif num_en_list[-5] == "4":
            des4 = decimal4()
            des5 = f"cuarenta y {des4}"
        elif num_en_list[-5] == "5" and num_en_list[-4] == "0":
            des5 = "cincuenta"
        elif num_en_list[-5] == "5":
            des4 = decimal4()
            des5 = f"cincuenta y {des4}"
        elif num_en_list[-5] == "6" and num_en_list[-4] == "0":
            des5 = "sesenta"
        elif num_en_list[-5] == "6":
            des4 = decimal4()
            des5 = f"sesenta y {des4}"
        elif num_en_list[-5] == "7" and num_en_list[-4] == "0":
            des5 = "setenta"
        elif num_en_list[-5] == "7":
            des4 = decimal4()
            des5 = f"setenta y {des4}"
        elif num_en_list[-5] == "8" and num_en_list[-4] == "0":
            des5 = "ochenta"
        elif num_en_list[-5] == "8":
            des4 = decimal4()
            des5 = f"ochenta y {des4}"
        elif num_en_list[-5] == "9" and num_en_list[-4] == "0":
            des5 = "noventa"
        elif num_en_list[-5] == "9":
            des4 = decimal4()
            des5 = f"noventa y {des4}"

    

    return des5    

def decimal6():
    if len(num_en_list) >= 6:
        if num_en_list[-6] == "0":
            des6 = ""
        elif num_en_list[-6] == "1" and num_en_list[-5] == "0" and num_en_list[-4] == "0":
            des6 = f"cien mil"
        elif num_en_list[-6] == "1" and num_en_list[-5] == "0":
            des4 = decimal4()
            des6 = f"ciento {des4}"
        elif num_en_list[-6] == "1":
            des5 = decimal5()
            des6 = f"ciento {des5}"
        elif num_en_list[-6] == "2" and num_en_list[-5] == "0" and num_en_list[-4] == "0":
            des6 = f"doscientos mil"
        elif num_en_list[-6] == "2" and num_en_list[-5] == "0":
            des4 = decimal4()
            des6 = f"doscientos {des4}"
        elif num_en_list[-6] == "2":
            des5 = decimal5()
            des6 = f"doscientos {des5}"
        elif num_en_list[-6] == "3" and num_en_list[-5] == "0" and num_en_list[-4] == "0":
            des6 = f"trescientos mil"
        elif num_en_list[-6] == "3" and num_en_list[-5] == "0":
            des4 = decimal4()
            des6 = f"trescientos {des4}"
        elif num_en_list[-6] == "3":
            des5 = decimal5()
            des6 = f"trescientos {des5}"
        elif num_en_list[-6] == "4" and num_en_list[-5] == "0" and num_en_list[-4] == "0":
            des6 = f"cuatrocientos mil"
        elif num_en_list[-6] == "4" and num_en_list[-5] == "0":
            des4 = decimal4()
            des6 = f"cuatrocientos {des4}"
        elif num_en_list[-6] == "4":
            des5 = decimal5()
            des6 = f"cuatrocientos {des5}"
        elif num_en_list[-6] == "5" and num_en_list[-5] == "0" and num_en_list[-4] == "0":
            des6 = f"quinientos mil"
        elif num_en_list[-6] == "5" and num_en_list[-5] == "0":
            des4 = decimal4()
            des6 = f"quinientos {des4}"
        elif num_en_list[-6] == "5":
            des5 = decimal5()
            des6 = f"quinientos {des5}"
        elif num_en_list[-6] == "6" and num_en_list[-5] == "0" and num_en_list[-4] == "0":
            des6 = f"seiscientos mil"
        elif num_en_list[-6] == "6" and num_en_list[-5] == "0":
            des4 = decimal4()
            des6 = f"seiscientos {des4}"
        elif num_en_list[-6] == "6":
            des5 = decimal5()
            des6 = f"seiscientos {des5}"
        elif num_en_list[-6] == "7" and num_en_list[-5] == "0" and num_en_list[-4] == "0":
            des6 = f"setecientos mil"
        elif num_en_list[-6] == "7" and num_en_list[-5] == "0":
            des4 = decimal4()
            des6 = f"setecientos {des4}"
        elif num_en_list[-6] == "7":
            des5 = decimal5()
            des6 = f"setecientos {des5}"
        elif num_en_list[-6] == "8" and num_en_list[-5] == "0" and num_en_list[-4] == "0":
            des6 = f"ochocientos mil"
        elif num_en_list[-6] == "8" and num_en_list[-5] == "0":
            des4 = decimal4()
            des6 = f"ochocientos {des4}"
        elif num_en_list[-6] == "8":
            des5 = decimal5()
            des6 = f"ochocientos {des5}"
        elif num_en_list[-6] == "9" and num_en_list[-5] == "0" and num_en_list[-4] == "0":
            des6 = f"novecientos mil"
        elif num_en_list[-6] == "9" and num_en_list[-5] == "0":
            des4 = decimal4()
            des6 = f"novecientos {des4}"
        elif num_en_list[-6] == "9":
            des5 = decimal5()
            des6 = f"novecientos {des5}"
    return des6

def decimal7():
    if len(num_en_list) == 7:
        if num_en_list[-7] == "0":
            des7 = ""
        if num_en_list[-7] == "1":
            des7 = "Un millon"        
        elif num_en_list[-7] == "2":
            des7 = "Dos millones"
        elif num_en_list[-7] == "3":
            des7 = "Tres millones"
        elif num_en_list[-7] == "4":
            des7 = "Cuatro millones"
        elif num_en_list[-7] == "5":
            des7 = "Cinco millones"
        elif num_en_list[-7] == "6":
            des7 = "Seis millones"
        elif num_en_list[-7] == "7":
            des7 = "Siete millones"
        elif num_en_list[-7] == "8":
            des7 = "Ocho millones"
        elif num_en_list[-7] == "9":
            des7 = "Nueve millones"

    elif len(num_en_list) > 7:
        if num_en_list[-7] == "0":
            des7 = ""
        if num_en_list[-7] == "2":
            des7 = "dos millones"
        elif num_en_list[-7] == "3":
            des7 = "tres millones"
        elif num_en_list[-7] == "4":
            des7 = "cuatro millones"
        elif num_en_list[-7] == "5":
            des7 = "cinco millones"
        elif num_en_list[-7] == "6":
            des7 = "seis millones"
        elif num_en_list[-7] == "7":
            des7 = "siete millones"
        elif num_en_list[-7] == "8":
            des7 = "ocho millones"
        elif num_en_list[-7] == "9":
            des7 = "nueve millones"
    return des7

def decimal8():
    if len(num_en_list) == 8:
        if num_en_list[-8] == "1" and num_en_list[-7] == "0":
            des8 = "Diez millones"
        elif num_en_list[-8] == "1" and num_en_list[-7] == "1":
            des8 = "Once millones"
        elif num_en_list[-8] == "1" and num_en_list[-7] == "2":
            des8 = "Doce millones"
        elif num_en_list[-8] == "1" and num_en_list[-7] == "3":
            des8 = "Trece milones"
        elif num_en_list[-8] == "1" and num_en_list[-7] == "4":
            des8 = "Catorce millones"
        elif num_en_list[-8] == "1" and num_en_list[-7] == "5":
            des8 = "Quince millones"
        elif num_en_list[-8] == "1":
            des7 = decimal7()
            des8 = f"Diesi{des7}"
        elif num_en_list[-8] == "2" and num_en_list[-7] == "0":
            des8 = "Veinte millones"
        elif num_en_list[-8] == "2":
            des7 = decimal7()
            des8 = f"Veinti{des7}"
        elif num_en_list[-8] == "3" and num_en_list[-7] == "0":
            des8 = "Treinta millones"
        elif num_en_list[-8] == "3":
            des7 = decimal7()
            des8 = f"Treinta  {des7}"
        elif num_en_list[-8] == "4" and num_en_list[-7] == "0":
            des8 = "Cuarenta millones"
        elif num_en_list[-8] == "4":
            des7 = decimal7()
            des8 = f"Cuarenta y {des7}"
        elif num_en_list[-8] == "5" and num_en_list[-7] == "0":
            des8 = "Cincuenta millones"
        elif num_en_list[-8] == "5":
            des7 = decimal7()
            des8 = f"Cincuenta y {des7}"
        elif num_en_list[-8] == "6" and num_en_list[-7] == "0":
            des8 = "Sesenta millones"
        elif num_en_list[-8] == "6":
            des7 = decimal7()
            des8 = f"Sesenta  {des7}"
        elif num_en_list[-8] == "7" and num_en_list[-7] == "0":
            des8 = "Setenta millones"
        elif num_en_list[-8] == "7":
            des7 = decimal7()
            des8 = f"Setenta  {des7}"
        elif num_en_list[-8] == "8" and num_en_list[-7] == "0":
            des8 = "Ochenta millones"
        elif num_en_list[-8] == "8":
            des7 = decimal7()
            des8 = f"Ochenta  {des7}"
        elif num_en_list[-8] == "9" and num_en_list[-7] == "0":
            des8 = "Noventa millones"
        elif num_en_list[-8] == "9":
            des7 = decimal7()
            des8 = f"Noventa y {des7}"

    elif len(num_en_list) >7:
        if num_en_list[-8] == "0":
            des8 = "millones"
        if num_en_list[-8] == "1" and num_en_list[-7] == "0":
            des8 = "diez millones"
        elif num_en_list[-8] == "1" and num_en_list[-7] == "1":
            des8 = "once millones"
        elif num_en_list[-8] == "1" and num_en_list[-7] == "2":
            des8 = "doce millones"
        elif num_en_list[-8] == "1" and num_en_list[-7] == "3":
            des8 = "trece millones"
        elif num_en_list[-8] == "1" and num_en_list[-7] == "4":
            des8 = "catorce"
        elif num_en_list[-8] == "1" and num_en_list[-7] == "5":
            des8 = "quince"
        elif num_en_list[-8] == "1":
            des7 = decimal6()
            des8 = f"diesi{des7}"
        elif num_en_list[-8] == "2" and num_en_list[-7] == "0":
            des8 = "veinte millones"
        elif num_en_list[-8] == "2":
            des7 = decimal6()
            des8 = f"veinti{des7}"
        elif num_en_list[-8] == "3" and num_en_list[-7] == "0":
            des8 = "treinta millones"
        elif num_en_list[-8] == "3":
            des7 = decimal6()
            des8 = f"treinta  {des7}"
        elif num_en_list[-8] == "4" and num_en_list[-7] == "0":
            des8 = "cuarenta millones"
        elif num_en_list[-8] == "4":
            des7 = decimal6()
            des8 = f"cuarentay {des7}"
        elif num_en_list[-8] == "5" and num_en_list[-7] == "5":
            des8 = "cincuenta millones"
        elif num_en_list[-8] == "5":
            des7 = decimal6()
            des8 = f"cincuent y {des7}"
        elif num_en_list[-8] == "6" and num_en_list[-7] == "0":
            des8 = "sesenta millones"
        elif num_en_list[-8] == "6":
            des7 = decimal6()
            des8 = f"sesenta  {des7}"
        elif num_en_list[-8] == "7" and num_en_list[-7] == "0":
            des8 = "setenta millones"
        elif num_en_list[-8] == "7":
            des7 = decimal6()
            des8 = f"setenta  {des7}"
        elif num_en_list[-8] == "8" and num_en_list[-7] == "0":
            des8 = "ochenta millones"
        elif num_en_list[-8] == "8":
            des7 = decimal6()
            des8 = f"ochenta  y {des7}"
        elif num_en_list[-8] == "9" and num_en_list[-7] == "0":
            des8 = "noventa millones"
        elif num_en_list[-8] == "9":
            des7 = decimal6()
            des8 = f"noventa y {des7}"

    

    return des8 

# Un solo dígito.

if len(num_en_list) == 1:
    if num_en_list[-1] == "0":
        print("Cero")
    elif num_en_list[-1] == "1":
        print("Uno")
    elif num_en_list[-1] == "2":
        print("Dos")
    elif num_en_list[-1] == "3":
        print("Tres")
    elif num_en_list[-1] == "4":
        print("Cuatro")
    elif num_en_list[-1] == "5":
        print("Cinco")
    elif num_en_list[-1] == "6":
        print("Seis")
    elif num_en_list[-1] == "7":
        print("Siete")
    elif num_en_list[-1] == "8":
        print("Ocho")
    elif num_en_list[-1] == "9":
        print("Nueve")

# Dos Dígitos

elif len(num_en_list) == 2:
    if num_en_list[-2] == "1" and num_en_list[-1] == "0":
        print("Diez")
    elif num_en_list[-2] == "1" and num_en_list[-1] == "1":
        print("Once")
    elif num_en_list[-2] == "1" and num_en_list[-1] == "2":
        print("Doce")
    elif num_en_list[-2] == "1" and num_en_list[-1] == "3":
        print("Trece")
    elif num_en_list[-2] == "1" and num_en_list[-1] == "4":
        print("Catorce")
    elif num_en_list[-2] == "1" and num_en_list[-1] == "5":
        print("Quince")
    elif num_en_list[-2] == "1":
        des1 = decimal1()
        print(f"Diesi{des1}")
    elif num_en_list[-2] == "2" and num_en_list[-1] == "0":
        print(f"Veinte")
    elif num_en_list[-2] == "2":
        des1 = decimal1()
        print(f"Veinti{des1}")
    elif num_en_list[-2] == "3" and num_en_list[-1] == "0":
        print(f"Treinta")
    elif num_en_list[-2] == "3":
        des1 = decimal1()
        print(f"Treinta y {des1}")
    elif num_en_list[-2] == "4" and num_en_list[-1] == "0":
        print(f"Cuarenta")
    elif num_en_list[-2] == "4":
        des1 = decimal1()
        print(f"Cuarenta y {des1}")
    elif num_en_list[-2] == "5" and num_en_list[-1] == "0":
        print(f"Cincuenta")
    elif num_en_list[-2] == "5":
        des1 = decimal1()
        print(f"Cincuenta y {des1}")
    elif num_en_list[-2] == "6" and num_en_list[-1] == "0":
        print(f"Sesenta")
    elif num_en_list[-2] == "6":
        des1 = decimal1()
        print(f"Sesenta y {des1}")
    elif num_en_list[-2] == "7" and num_en_list[-1] == "0":
        print(f"Setenta")
    elif num_en_list[-2] == "7":
        des1 = decimal1()
        print(f"Setenta y {des1}")
    elif num_en_list[-2] == "8" and num_en_list[-1] == "0":
        print(f"Ochenta")
    elif num_en_list[-2] == "8":
        des1 = decimal1()
        print(f"Ochenta y {des1}")
    elif num_en_list[-2] == "9" and num_en_list[-1] == "0":
        print(f"Noventa")
    elif num_en_list[-2] == "9":
        des1 = decimal1()
        print(f"Noventa y {des1}")

#Tres Dígitos

elif len(num_en_list) == 3:
    if num_en_list[-3] == "1" and num_en_list[-2] == "0" and num_en_list[-1] == "0":
        print("Cien")
    elif num_en_list[-3] == "1" and num_en_list[-2] == "0":
        des1 = decimal1()
        print(f"Ciento {des1}")
    elif num_en_list[-3] == "1":
        des2 = decimal2()
        print(f"Ciento {des2}")
    elif num_en_list[-3] == "2" and num_en_list[-2] == "0" and num_en_list[-1] == "0":
        print("Doscientos")
    elif num_en_list[-3] == "2" and num_en_list[-2] == "0":
        des1 = decimal1()
        print(f"Doscientos {des1}")
    elif num_en_list[-3] == "2":
        des2 = decimal2()
        print(f"Doscientos {des2}")
    elif num_en_list[-3] == "3" and num_en_list[-2] == "0" and num_en_list[-1] == "0":
        print("Trescientos")
    elif num_en_list[-3] == "3" and num_en_list[-2] == "0":
        des1 = decimal1()
        print(f"Trescientos {des1}")
    elif num_en_list[-3] == "3":
        des2 = decimal2()
        print(f"Trescientos {des2}")
    elif num_en_list[-3] == "4" and num_en_list[-2] == "0" and num_en_list[-1] == "0":
        print("Cuatrocientos")
    elif num_en_list[-3] == "4" and num_en_list[-2] == "0":
        des1 = decimal1()
        print(f"Cuatrocientos {des1}")
    elif num_en_list[-3] == "4":
        des2 = decimal2()
        print(f"Cuatrocientos {des2}")
    elif num_en_list[-3] == "5" and num_en_list[-2] == "0" and num_en_list[-1] == "0":
        print("Quinientos")
    elif num_en_list[-3] == "5" and num_en_list[-2] == "0":
        des1 = decimal1()
        print(f"Quinientos {des1}")
    elif num_en_list[-3] == "5":
        des2 = decimal2()
        print(f"Quinientos {des2}")
    elif num_en_list[-3] == "6" and num_en_list[-2] == "0" and num_en_list[-1] == "0":
        print("Seiscientos")
    elif num_en_list[-3] == "6" and num_en_list[-2] == "0":
        des1 = decimal1()
        print(f"Seiscientos {des1}")
    elif num_en_list[-3] == "6":
        des2 = decimal2()
        print(f"Seiscientos {des2}")
    elif num_en_list[-3] == "7" and num_en_list[-2] == "0" and num_en_list[-1] == "0":
        print("Setecientos")
    elif num_en_list[-3] == "7" and num_en_list[-2] == "0":
        des1 = decimal1()
        print(f"Setecientos {des1}")
    elif num_en_list[-3] == "7":
        des2 = decimal2()
        print(f"Setecientos {des2}")
    elif num_en_list[-3] == "8" and num_en_list[-2] == "0" and num_en_list[-1] == "0":
        print("Ochocientos")
    elif num_en_list[-3] == "8" and num_en_list[-2] == "0":
        des1 = decimal1()
        print(f"Ochocientos {des1}")
    elif num_en_list[-3] == "8":
        des2 = decimal2()
        print(f"Ochocientos {des2}")
    elif num_en_list[-3] == "9" and num_en_list[-2] == "0" and num_en_list[-1] == "0":
        print("Novecientos")
    elif num_en_list[-3] == "9" and num_en_list[-2] == "0":
        des1 = decimal1()
        print(f"Novecientos {des1}")
    elif num_en_list[-3] == "9":
        des2 = decimal2()
        print(f"Novecientos {des2}")

#Cuatro Dígitos

elif len(num_en_list) == 4:
    if num_en_list[-4] >= "1" and num_en_list[-3] == "0" and num_en_list[-2] == "0":
        des1 = decimal1()
        des4 = decimal4()
        print(f"{des4} {des1}")
    elif num_en_list[-4] >= "1" and num_en_list[-3] == "0":
        des2 = decimal2()
        des4 = decimal4()
        print(f"{des4} {des2}")
    elif num_en_list[-4] >= "1":
        des3 = decimal3()
        des4 = decimal4()
        print(f"{des4} {des3}")

#Cinco Dígitos

elif len(num_en_list) == 5:
    if num_en_list[-5] >= "1" and num_en_list[-4] == "0" and num_en_list[-3] == "0" and num_en_list[-2] == "0":
        des1 = decimal1()
        des5 = decimal5()
        print(f"{des5} {des1}")
    elif num_en_list[-5] >= "1" and num_en_list[-4] == "0" and num_en_list[-3] == "0":
        des2 = decimal2()
        des5 = decimal5()
        print(f"{des5} {des2}")
    elif num_en_list[-5] >= "1" and num_en_list[-4] == "0":
        des3 = decimal3()
        des5 = decimal5()
        print(f"{des5} {des3}")
    elif num_en_list[-5] >= "1":
        des3 = decimal3()
        des5 = decimal5()
        print(f"{des5} {des3}")

#Seis Dígitos

elif len(num_en_list) == 6:
    if num_en_list[-6] >= "1" and num_en_list[-4] == "0" and num_en_list[-3] == "0" and num_en_list[-2] == "0":
        des1 = decimal1()
        des6 = decimal6()
        print(f"{des6} {des1}")
    elif num_en_list[-6] >= "1" and num_en_list[-4] == "0" and num_en_list[-3] == "0":
        des2 = decimal2()
        des6 = decimal6()
        print(f"{des6} {des2}")
    elif num_en_list[-6] >= "1" and num_en_list[-4] == "0":
        des2 = decimal2()
        des6 = decimal6()
        print(f"{des6} {des2}")
    elif num_en_list[-6] >= "1":
        des3 = decimal3()
        des6 = decimal6()
        print(f"{des6} {des3}")
    
#Siete Digitos

elif len(num_en_list) == 7:
    if num_en_list[-7] >= "1" and num_en_list[-6] == "0" and num_en_list[-5] == "0" and num_en_list[-4] == "0" and num_en_list[-3] == "0" and num_en_list[-2] == "0":
        des1 = decimal1()
        des7 = decimal7()
        print(f"{des7} {des1}")
    elif num_en_list[-7] >= "1" and num_en_list[-6] == "0" and num_en_list[-5] == "0" and num_en_list[-4] == "0" and num_en_list[-3] == "0":
        des2 = decimal2()
        des7 = decimal7()
        print(f"{des7} {des2}")
    elif num_en_list[-7] >= "1" and num_en_list[-6] == "0" and num_en_list[-5] == "0" and num_en_list[-4] == "0":
        des3 = decimal3()
        des7 = decimal7()
        print(f"{des7} {des3}")
    elif num_en_list[-7] >= "1" and num_en_list[-6] == "0" and num_en_list[-5] == "0":
        des3 = decimal3()
        des4 = decimal4()
        des7 = decimal7()
        print(f"{des7} {des4} {des3}")
    elif num_en_list[-7] >= "1" and num_en_list[-6] == "0":
        des3 = decimal3()
        des5 = decimal5()
        des7 = decimal7()
        print(f"{des7} {des5} {des3}")
    elif num_en_list[-7] >= "1":
        des3 = decimal3()
        des6 = decimal6()
        des7 = decimal7()
        print(f"{des7} {des6} {des3}")

#Ocho Dígitos

elif len(num_en_list) == 8:
    if num_en_list[-8] >= "1" and num_en_list[-6] == "0" and num_en_list[-5] == "0" and num_en_list[-4] == "0" and num_en_list[-3] == "0" and num_en_list[-2] == "0":
        des1 = decimal1()
        des8 = decimal8()
        print(f"{des8} {des1}")
    elif num_en_list[-8] >= "1" and num_en_list[-6] == "0" and num_en_list[-5] == "0" and num_en_list[-4] == "0" and num_en_list[-3] == "0":
        des2 = decimal2()
        des8 = decimal8()
        print(f"{des8} {des2}")
    elif num_en_list[-8] >= "1" and num_en_list[-6] == "0" and num_en_list[-5] == "0" and num_en_list[-4] == "0":
        des3 = decimal3()
        des8 = decimal8()
        print(f"{des8} {des3}")
    elif num_en_list[-8] >= "1" and num_en_list[-6] == "0" and num_en_list[-5] == "0":
        des3 = decimal3()
        des4 = decimal4()
        des8 = decimal8()
        print(f"{des8} {des4} {des3}")
    elif num_en_list[-8] >= "1" and num_en_list[-6] == "0":
        des3 = decimal3()
        des5 = decimal5()
        des8 = decimal8()
        print(f"{des8} {des5} {des3}")
    elif num_en_list[-8] >= "1":
        des3 = decimal3()
        des6 = decimal6()
        des8 = decimal8()
        print(f"{des8} {des6} {des3}")
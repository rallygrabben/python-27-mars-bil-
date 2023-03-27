import bil 

looping = True


Ford_red = bil.Bil("Ford Sierra", "Röd", 5)
Volvo_Pink = bil.Bil("Volvo 240", "Rosa som fan", 2)
Ferarri_Yellow = bil.Bil("Ferarri 421", "Gul", 1)
Nissan_Green = bil.Bil("Nissan 240sx", "Oliv Grön", 2)
Saab_Brown = bil.Bil("Saab 95", "Brun", 6)

billista = [Ford_red, Volvo_Pink, Ferarri_Yellow, Nissan_Green, Saab_Brown]


# print(Ford_red.getFabrikat())


while looping == True:
    print("----------------------------------------------------------------")
    print("BilAutomat")

    i=0 

    for bil in billista:
    
        print(str(i+1) + ": " + bil.fabrikat + "\t Color:" + bil.color + "\t Count:" + str(bil.lager))
        i = i+1

    bil_nr = input(f"\n\n Vilken bil vill du välja? :")
    bil_nr_int = int(bil_nr) 

    lager_int = billista[bil_nr_int-1].getlager()
    lager_string = str(lager_int)

    bilColor = billista[bil_nr_int-1].color
    bilFabrikat = billista[bil_nr_int-1].fabrikat
    bilCount = lager_int - 1 


    if lager_int > 0:
        print(f"\tEn {bilColor} {bilFabrikat} kommer här!\n\tDet finns {bilCount} kvar!")
        # print("\n En " + billista[bil_nr_int-1].color + " " + billista[bil_nr_int-1].fabrikat + " kommer här!")

        # Minskar i lagret
        nyttlagersaldo_int = lager_int -1
        nyttlagersaldo_str = str(nyttlagersaldo_int)

        billista[bil_nr_int-1].setlager(nyttlagersaldo_int)

    else:
        print("Tyvärr slut på vald bil!")


    svar = input("\n Vill du avsluta programmet? j/n :")
    if (svar == "j"):
        break

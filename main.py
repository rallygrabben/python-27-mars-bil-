import bil 

looping = True


Ford_red = bil.Bil("Ford", "Röd", 5)

print(Ford_red.getFabrikat())


while looping == True:
    print("----------------------------------------------------------------")
    print("BilAutomat")

    svar = input("\n Vill du avsluta programmet? j/n :")
    if (svar == "j"):
        break

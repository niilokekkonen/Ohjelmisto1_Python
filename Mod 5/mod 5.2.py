lukujen_lista = [] #Tyhjä lista


while True: #Kun syöte ei ole tyhjä merkkijono tai kirjain, prosessi katkeaa.
    luvut = (input("Syötä luku tai lopeta painamalla enter:")) #kysyy syötteen
    if luvut == "": #Ohjelma sammuu tyhjästä merkkijonosta
        break
    try: #Muuttaa string -> int ja lisää sen listaan
        lukujen_lista.append(int(luvut)) # lisää syötteen listaan
    except ValueError: #Tekee tämän jos syötteenä on virheellinen arvo
        print("Syöte ei ole kelvollinen luku")

for luku in range(5): # käy läpi listan: lukujen_lista
    lukujen_lista.sort(reverse = True)
    print(lukujen_lista) #Lajittelee listan: lukujen_lista

names = set() #Luo tyhjän joukon


while True: #Kun on tosi tämä silmukka pyörii
    nimi = input("Syötä nimi tai lopeta painamalla enter:").capitalize().strip()#Kysyy syötteen, .capitalize() = iso alkukirjain
    if nimi == "": #Jos syöte on tyhjä merkkijono, ohjelma sammuu
        print("Ohjelma sammuu")
        break
    if nimi not in names: #Jos nimi ei ole joukossa, kertoo sen olevan uusi nimi ja lisää sen joukkoon
        print(f"{nimi} on uusi nimi")
        names.add(nimi)
    else: #Jos nimi on jo joukossa, tulostaa aiemmin syötetty nimi
        print(f"{nimi} on aiemmin syötetty nimi")


for n in names: #käy läpi names joukon
    print(n)



luku = int(input("Syötä kokonaisluku, niin kerrotaan onko se alkuluku:")) #Kysyy syötteen

jaollinen = []

#oletusarvo on, että luku on alkuluku, todennetaan tämä jakamalla
onko_alkuluku = True


for i in range(2,luku):
    print(i)
    if luku % i == 0:#Ei ole alkuluku
        onko_alkuluku = False
        jaollinen.append(i)

if onko_alkuluku:
    print(f"{luku} on alkuluku")
else:
    print(f"{luku} ei ole alkuluku")
    print(f"{luku} on jaollinen seuraavilla luvuilla {jaollinen}")










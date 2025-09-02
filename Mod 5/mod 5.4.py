kaupungit = []

#n = 5 #Voi tehdä myös näin ja tähän lisätä inputin

for kaupunki in range(n): #Kysyy 5 kertaa kaupungin ja lisää kaupungin listaan kaupungit
    k = input(f"Kerro {kaupunki+1} kaupungin nimi:")
    kaupungit.append(k)

for k in kaupungit: #Käy läpi listan kaupungit
    print(k)
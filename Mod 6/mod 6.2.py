import random

max_heitto = int(input("Mikä on nopan isoin luku?:")) #käyttäjältä saatava maksimi tulos

def nopanheitot(max_heitto): #Funktio heittää noppaa ja palauttaa nopasta tulevan luvun
    return random.randint(1,max_heitto) #Nopan heitto


heitot = 1  # Heiton numero
while True:
    heitto = nopanheitot(max_heitto)
    print(f"Heitto numero:{heitot} tulos:{heitto}")  # Tulosta heiton numeron ja nopasta tulleen luvun
    heitot += 1  # Kasvattaa heiton numeroa joka kierroksella yhdellä
    if heitto == max_heitto:  # Jos heitto on 6 ohjelma sammuu ja tämä tulostuu
        print(f"Ohjelma sammuu, numero {max_heitto} sammuttaa ohjelman")
        break





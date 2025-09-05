import random


def nopanheitot(): #Funktio heittää noppaa ja tulostaa nopasta tulevan luvun
    return random.randint(1,6)


heitot = 1
while True:
    heitto = nopanheitot()# Kutsuu funktiota nopanheitot
    print(f"Heitto numero:{heitot} tulos:{heitto}")  # Tulosta heiton numeron ja nopasta tulleen luvun
    if heitto == 6:  # Jos heitto on 6 ohjelma sammuu ja tämä tulostuu
        print(f"Numero 6 sammuttaa ohjelman")
        heitot += 1  # Kasvattaa heiton numeroa joka kierroksella 1
        break













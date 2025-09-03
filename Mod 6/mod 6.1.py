import random


def nopanheitot(): #Funktio heittää noppaa ja tulostaa nopasta tulevan luvun
    heitto = random.randint(1,6)
    heitot = 0
    heitot += 1
    while heitto != 6:
        heitto = random.randint(1, 6) #Noppa
        print(f"Heitto numero:{heitot} tulos:{heitto}")  # Tulosta heiton numeron ja nopasta tulleen luvun
        heitot += 1 #Kasvattaa heiton numeroa joka kierroksella 1
        if heitto == 6:  # Jos heitto on 6 ohjelma sammuu ja tämä tulostuu
            print(f"Heitto numero:{heitot} tulos:{heitto}. numero 6 sammuttaa ohjelman")
    return heitto





nopanheitot() #Kutsuu funktiota nopanheitot










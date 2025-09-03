import random

max_heitto = int(input("Mikä on nopan isoin luku?:")) #käyttäjältä saatava maksimi tulos

def nopanheitot(max_heitto): #Funktio heittää noppaa ja tulostaa nopasta tulevan luvun
    heitto = random.randint(1,max_heitto) #Nopan heitto
    heitot = 1  # Heiton numero
    while heitto < max_heitto:
        print(f"Heitto numero:{heitot} tulos:{heitto}")  # Tulosta heiton numeron ja nopasta tulleen luvun
        heitto = random.randint(1, max_heitto)
        heitot += 1  # Kasvattaa heiton numeroa joka kierroksella yhdellä
        if heitto == max_heitto:  # Jos heitto on 6 ohjelma sammuu ja tämä tulostuu
            print(f"Heitto numero:{heitot} tulos:{heitto}. numero {max_heitto} sammuttaa ohjelman")
            break



nopanheitot(max_heitto)
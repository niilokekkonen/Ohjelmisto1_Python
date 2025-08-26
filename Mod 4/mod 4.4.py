import random

luku = random.randint(1,10)

while True:
    arvaus = int(input("Arvaa luku:"))
    if arvaus < luku:
        print("Liian pieni luku")
    elif arvaus > luku:
        print("Liian suuri luku")
    else:
        print("Arvasit oikein:D")
        break


import random,math


N = 0 #Ympyrän sisälle osuvien pisteiden määrä
I = 0 #Montako pistettä on käsitelty

pistemaara = int(input("Kerro pisteiden kokonaismäärä kokonaislukuna:")) #Montako pistettä on yhteensä


while I < pistemaara:
    rnmd_x = random.uniform(-1, 1) #arvotaan piste X
    rnmd_y = random.uniform(-1, 1) #arvotaan piste Y
    d = rnmd_x * rnmd_x + rnmd_y * rnmd_y #x**2 + y**2
    I += 1
    if d <= 1:
        N += 1



piin_arvo = 4*N/pistemaara
print(f"Piin liki arvo on: {piin_arvo}")
print(f"Tässä on piin arvo: {math.pi}")




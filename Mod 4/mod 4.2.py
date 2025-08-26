inch = 2.54 #tuumat-centit :D
print("Muunna tuumat senteiksi.")
tuumat = (float(input("Syötä tuumat jotka haluat muuntaa:")))

muunnos = inch * tuumat

while tuumat > 0 :
    print(f"{muunnos}cm")
    tuumat = (float(input("Syötä tuumat jotka haluat muuntaa:")))
    muunnos = inch * tuumat

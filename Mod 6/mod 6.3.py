def gallons_liters(gallons):
    gallon_in_liters = 3.785
    liters= gallon * 3.785
    return liters

gallon = float(input("Kerro gallonat, niin saat litrat(esim 11.5): "))



while gallon > 0:
    print(f"{gallons_liters(gallon)} litraa")
    gallon = float(input("Kerro gallonat, niin saat litrat: "))
    if gallon < 0:
        print("Ohjelma sammuu")
        break




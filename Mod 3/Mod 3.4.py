kvuosi = int(input("Kirjoita vuosi:"))

if kvuosi % 400 == 0:
    print("Vuosi on karkausvuosi")
elif kvuosi % 4 == 0 and kvuosi % 100 != 0:
    print("Vuosi on karkaus vuosi")
elif kvuosi % 100 == 0 and kvuosi % 400 != 0:
    print("Vuosi ei ole karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")
print("Kerro kappaleen massa keskiaikaisten mittojen mukaan")

#leiviskä = Yksi leiviskä on 20 naulaa
#naula = Yksi naula on 32 luotia
#luoti = Yksi luoti on 13,3 grammaa

leiviskat = float(input("Kerro leiviskät:"))
naulat = float(input("Kerro naulat:"))
luodit = float(input("Kerro luodit:"))

kaikkile = leiviskat * 20
kaikkin =  leiviskat * 20 + naulat
kokoluodit = (leiviskat * 20 + naulat) * 32 + luodit

yhteis_summa = kokoluodit * 13.3

kilot = int(yhteis_summa // 1000)
ylijaamat = round(yhteis_summa % 1000, 2)
print(f"Tässä lukusi nykyaikaisissa mitoissa: {kilot}kilogrammaa ja {ylijaamat} grammaa")
from math import pi

def pizza_arvo(koko,hinta):
    pinta_ala = pi*(koko/2)**2 #Muuntaa halkaisijan säteeksi ja laskee pinta-alan
    sqr_meters = pinta_ala / 10000 #Muuntaa neliö cm -> neliömetreiksi
    arvo = hinta / sqr_meters #Laskee arvon per neliömetri
    return arvo #Palauttaa arvon


pizzan_koko1 = float(input("Kerro ensimmäisen pizzan halkaisija(cm):")) #Kysyy halkaisijan 1. kerran
hinta1 = float(input("Kerro ensimmäisen pizzan hinta(€):")) #Kysyy hinnan 1. kerran
pizzan_koko2 = float(input("Kerro toisen pizzan halkaisija(cm):")) #Kysyy halkaisijan 2. kerran
hinta2 = float(input("Kerro toisen pizzan hinta(€): "))  #Kysyy hinnan 2. kerrran

pizzan1_arvo = pizza_arvo(pizzan_koko1,hinta1) #Tallentaa funktion kutsun muuttujaan pizzan1_arvo
pizzan2_arvo = pizza_arvo(pizzan_koko2,hinta2)# Sama mutta pizzan2_arvo:lle

print(f"Ensimmäisen pizzan arvo on {pizzan1_arvo:.2f} €/neliömetri") #Kertoo arvon
print(f"Toisen pizzan arvo on {pizzan2_arvo:.2f} €/neliömetri") #kertoo toisen arvon

if pizzan1_arvo < pizzan2_arvo:
    print("Pizza jonka syötit ensimmäisenä on halvempi") #Vertailee kumpi on halvempi
else:
    print("Pizza jonka syötit viimeisenä on halvempi")

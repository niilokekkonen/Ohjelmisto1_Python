seasons = ("tammikuu", #Luo monikon kuukausista
           "helmikuu",
           "maaliskuu",
           "huhtikuu",
           "toukokuu",
           "kesäkuu",
           "heinäkuu",
           "elokuu",
           "syyskuu",
           "lokakuu",
           "marraskuu",
           "joulukuu")

kevät = ("maaliskuu", "huhtikuu", "toukokuu") #Luo monikon joka vuodenajalle, joka sisältää vuodenaikaa vastaavat kuukaudet
kesä = ("kesäkuu", "heinäkuu", "elokuu")
syksy = ("syyskuu", "lokakuu", "marraskuu")
talvi =("joulukuu", "tammikuu", "helmikuu")

month_num = int(input("Kerro kuukauden numero(1-12):")) #Pyytää kuukauden numeron
if 1<= month_num <= 12: #Tarkistaa onko luku 1-12 välillä
    season = seasons[month_num-1] #Poistaa yhden, koska indeksi alkaa nollasta
    if season in talvi: #Vertailee syötettä vuodenaikoihin ja tulostaa kuukautta vastaavan vuodenajan
        print(f"{season} on talvella")
    elif season in kevät:
        print(f"{season} on keväällä")
    elif season in kesä:
        print(f"{season} on kesällä")
    elif season in syksy:
        print(f"{season} on syksyllä")
else:
    print("Virheellinen luku") #Jos luku ei ole 1-12 tulostaa tämän









airports = {"EFHK" :"Helsinki-Vantaan lentoasema", #Luo sanakirjan airports
            "EFIV" : "Ivalon lentoasema",
            "EFJO" : "Joensuun lentoasema",
            "EFKI" : "Kajaanin lentoasema",
            "EFET" : "Enontekiön lentoasema" ,
            "EHAM" : "Amsterdam Schipol",
            "EGLL" : "Lontoo Heathrow"}

while True:
    choice = input("Haluatko hakea lentoaseman(h), lisätä lentoaseman(l) vai "
                   "lopettaa painamalla enter?") #Kysyy mitä käyttäjä haluaa
    if choice == "h": #Jos käyttäjä haluaa hakea tämä ajetaan
        icao_code2 = input("Syötä ICAO koodi(esim. EFHK):").upper().strip() #muuntaa ICAO koodin isoksi ja poistaa tyhjät merkit
        if icao_code2 in airports: #Jos ICAO koodi on listassa tulostaa alemman koodin
            print(f"Lentokentän nimi: {airports[icao_code2]}") #Tulostaa ICAO koodia vastaavan lentokentän nimen
        else:
            print("Lentokenttää ei ole lisätty listaan") #Muuten tulostaa tämän
    elif choice == "l": #Jos käyttäjä haluaa lisätä tämä ajetaan
        icao_code1 = input("Syötä lentoaseman ICAO koodi:").upper().strip() #Kysyy ICAO koodin ja muuttaa kirjaimet isoiksi
        air_name = input("Syötä lentoaseman nimi").strip() #Kysyy lisättävän lentoaseman nimeä
        if icao_code1 not in airports: #Jos ICAO koodi ei ole airports listassa, lisää sen sinne
            airports[icao_code1] = air_name
            print("Lentoasema lisätty listaan")
        else:
            print("Lentoasema on jo listassa") #Jos ICAO koodi on jo listassa tulostaa tämän
    elif choice == "": #Jos käyttäjä haluaa lopettaa tämä ajetaan
        print("Ohjelma sammuu, tervetuloa uudestaan!")
        break


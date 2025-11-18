import mysql.connector

connection = mysql.connector.connect(
    port = 3306, #Oletusarvo
    host = "localhost", #Oletusarvo
    database = "DB_NAME", #Tietokannan nimi
    user = "Admin123", #Käyttäjänimi
    password = "PASS", #Salasana
    autocommit = True #Tekee kyselyt automaattisesti
)

#Funktio joka hakee tietokannasta
def search_ports_by_icao(code):
    sql = (f"SELECT airport.name, municipality FROM airport, country "
           f"WHERE ident = '{code}' AND airport.iso_country = country.iso_country")
    cursor = connection.cursor()
    cursor.execute(sql)  # SQL lauseiden suorittamiseen
    res = cursor.fetchone()  # Hakee tulosjoukosta rivi kerrallaan
    if res:
        return f"{res[0]}, {res[1]}" #Palauttaa arvot, jos ne löytyy tietokannasta
    else:
        return "Ei löydy" #Palauttaa 'ei löydy', jos hakua ei löydy.

while True: #Kyselee niin kauan, kun käyttäjä haluaa.
    i_code = input("Kerro lentoaseman ICAO koodi tai lopeta painamalla enter:").upper().strip() #Pyytää ICAO koodin
    if i_code == "":
        print("Ohjelma sammuu, tervetuloa uudestaan") #Tyhjä merkkijono pysäyttää ohjelman ja tulostaa tämän
        break
    if i_code != "": #Muuten ajaa funktion ja tulostaa hakutuloksen
        search_icao = search_ports_by_icao(i_code)
        print(search_icao)


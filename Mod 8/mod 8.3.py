import mysql.connector, geopy.distance #Import sql driver ja geopy

connection = mysql.connector.connect(
    port = 3306,
    host = "localhost", #Oletusarvo
    database = "DB_NAME", #Tietokannan nimi
    user = "Admin123", #Käyttäjänimi
    password = "PASS", #Salasana
    autocommit = True
) #Yhteys tietokantaan

#Funktio joka hakee tietokannasta ja laskee kenttien välisen etäisyyden
def count_distance_between(icao1, icao2):
    cursor = connection.cursor()
    sql1 = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao1}'"
    sql2 = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao2}'"
    cursor.execute(sql1) #Ajaa sql1 muuttujaan tallenetun SQL koodin
    coord1 = cursor.fetchone() #Palauttaa sen
    cursor.execute(sql2) #Ajaa sql2 muuttujaan tallenetun SQL koodin
    coord2 = cursor.fetchone()#Palauttaa sen
    if coord1 == None or coord2 == None: #Testaa onko kumpikaan arvioista 0
        return "Yritä uudestaan"
    else: #Muuten laskee etäisyyden
        distance_between = geopy.distance.distance(coord1,coord2).km
        return f"Etäisyys kenttien välillä on noin: {distance_between:.0f} km" #Palauttaa etäisyyden


while True:
    ask1 = input("Syötä ensimmäinen ICAO koodi:").upper().strip() #Kysyy ICAO koodin 1
    ask2 = input("Syötä toinen ICAO koodi:").upper().strip() #Kysyy ICAO koodin 2
    print(count_distance_between(ask1,ask2)) #Tulostaa etäisyyden
    ask3 = input("Voit sammuttaa ohjelman kirjoittamalla stop tai jatkaa painamalla enter")
    if ask3 == "stop":
        break
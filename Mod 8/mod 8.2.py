import mysql.connector

connection = mysql.connector.connect(
    port = 3306, #Oletusarvo,
    host = "localhost", #Oletusarvo
    database = "DB_NAME", #Tietokannan nimi
    user = "Admin123", #Käyttäjänimi
    password = "PASS", #Salasana
    autocommit = True #Tekee kyselyt automaattisesti
)

def port_type_and_amount(code):
    cursor = connection.cursor() #Tekee osoittimen ja tallentaa sen muuttujaan cursor
    sql = (f"SELECT type AS tyyppi, COUNT(*) AS lukumäärä "
           f"FROM airport WHERE iso_country = '{code}' GROUP BY type;")
    cursor.execute(sql) #Ajaa sql muuttujassa sijaitsevan komennon
    result = cursor.fetchall() #Vastaanottaa datan tietokannasta
    if result:
        for type,count in result:
            print(type,count)
        return result #Jos löytyy palauttaa tämän arvon
    else:
        return f"Ei löydy, yritä uudestaan" #Jos ei niin palauttaa tämän arvon


while True:
    country_code = input("Syötä maakoodi tai lopeta painamalla enter:").upper().strip()
    if country_code == "":
        break
    elif country_code != "":
       check = port_type_and_amount(country_code)
       if check == "Ei löydy, yritä uudestaan":
           print(check)
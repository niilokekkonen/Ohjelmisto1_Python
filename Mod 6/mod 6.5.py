def list_scrape(lista):
    parilliset = [] #Tyhjä lista parillisia varten
    for luku in lista: #Käy listan läpi
        if luku % 2 == 0: #Tarkistaa jakojäännöksen
            parilliset.append(luku) #Lisää parilliset listaan parilliset
    return parilliset #Palauttaa arvon parilliset

lista_1 = [1,2,3,4,5,6,7,8,]
suorita = list_scrape(lista_1)
print(suorita)


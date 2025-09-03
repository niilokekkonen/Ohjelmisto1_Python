
def m_sum(lista): #funktio, jonka parametri on lista
    total = 0 #Yhteisluku
    for num in lista: # For-loop, joka käy läpi listan
        total = total + num #Lisää muuttujaan 'total' jokaisen luvu
    return total #Palauttaa arvon total

numbers = [5,5,5,5,2] #Lista
yht = m_sum(numbers) # Tallentaa funktion kutsun muuttujaan yht
print(yht) #Tulostaa muuttujan yht



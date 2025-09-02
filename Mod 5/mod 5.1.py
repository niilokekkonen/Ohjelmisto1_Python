from random import randint
nopat =[] # Lista johon nopan heitot tallennetaan

lukum = int(input("Kuinka monta noppaa haluat heittää?:")) # Käyttäjän syöte


for i in range(lukum): #Heittää noppaa haluttavan määrän, sekä lisää ne listaan nopat
    heitto = randint(1,6)
    nopat.append(heitto)


print(nopat)
print(f"Tässä heitettyjen noppien summa: {sum(nopat)}") #sum(nopat) summaa listan "nopat" yhteen.
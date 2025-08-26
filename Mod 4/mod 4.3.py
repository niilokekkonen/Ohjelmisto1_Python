luvut = []


while True:
    num = input("Syötä luku:")
    if num == "":
        break
    try:
        luku = int(num)
        luvut.append(luku)
    except ValueError:
        print("Virhe, syötäthän vain kokonaislukuja :)")
if luvut:
    print(f"Tässä pienin syöttämäsi luku: {min(luvut)}")
    print(f"Tässä suurin syöttämäsi luku: {max(luvut)}")
else:
    print("Et kirjoittanut lukua")


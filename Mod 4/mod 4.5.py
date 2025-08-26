kayt_tun = "python"
salasana = "rules"
yri_set = 5


while yri_set > 0:
    ur_user = str(input("Kirjoita tähän käyttäjä tunnuksesi:"))
    ur_pass = str(input("Kirjoita tähän salasanasi:"))

    if ur_user == kayt_tun and ur_pass == salasana:

        print("Tervetuloa!")
        break
    yri_set -= 1
    if yri_set >= 1:
        print(f"Pääsy evätty, sinulla on {yri_set} yritystä")
    else:
        print("Pääsy evätty ja yritykset loppuivat!")









hytluok = str(input("Kerro hyttiluokkasi, kiitos:")).upper()
LUX = "parvekkeellinen hytti alakannella."
A = "ikkunnallinen hytti laivakannen yläpuolella."
B = "ikkunaton hytti autokannen yläpuolella."
C = "ikkunaton hytti autokannen alapuolella."

if hytluok == "LUX":
    print(f"Sinun hyttisi on {LUX}")
elif hytluok == "A":
    print(f"Sinun hyttisi on {A}")
elif hytluok == "B":
    print(f"Sinun hyttisi on {B}")
elif hytluok == "C":
    print(f"Sinun hyttisi on {C}")
else:
    print("Virheellinen hyttiluokka")

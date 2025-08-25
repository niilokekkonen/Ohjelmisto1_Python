skpli = str(input("Mikä on biologinen sukupuolesi?:")).lower()
hemglob = str(input("Syötä hemoglobiini arvosi,esim 100(g/l):")).lower().replace("g/l", "")
hemglob = int(hemglob)

mies = "mies"
nainen = "nainen"

miehen_min = 134
miehen_max = 195

#naisen normaali hemoglobiini taso = "117-175 g/l."
#miehen normaali hemoglobiini taso = "134-195 g/l."

naisen_min = 117
naisen_max = 175

if skpli == mies and hemglob < miehen_min :
    print("Hemoglobiini tasosi on alhainen.")
elif skpli == mies and miehen_min <= hemglob <= miehen_max:
    print("Hemoglobiini tasosi on normaali.")
elif skpli == mies and hemglob > miehen_max:
    print("Hemoglobiini tasosi on korkea.")
elif skpli == nainen and hemglob < naisen_min:
    print("Hemoglobiini tasosi on alhainen.")
elif skpli == nainen and naisen_min <= hemglob <= naisen_max:
    print("Hemoglobiini tasosi on normaali.")
elif skpli == nainen and hemglob > naisen_max:
    print("Hemoglobiini tasosi on korkea.")
else:
    print("Virhe, yritä uudelleen. Syötä sukupuolesi ja hemoglobiini arvosi uudelleen.")
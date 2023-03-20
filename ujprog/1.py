nevek = []
magassagok = []
nev = input("Adja meg a nevet")
while nev!="vege":
    magassag = input("Mekkora az ember?")

    while magassag.isnumeric()!=True:
        print("nem jó. Ujra")
        magassag = input("Mekkora az ember?")
    magassag=int(magassag)
    nevek.append(nev)
    magassagok.append(magassag)
    nev = input("adja meg a nevet")

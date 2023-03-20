
#//kérjük be emberek magasságát és nevét
#//add: nemeket is
nevek = []
magassagok = []
nemek = []
nev = input("Adja meg a nevet")
while nev!="vege":
    magassag = input("Mekkora az ember?")
    while magassag.isnumeric()!=True:
        print("nem jó. Ujra")
        magassag = input("Mekkora az ember?")
    magassag=int(magassag)
    check = False
    while check!=True:
        nem = input("Neme(fiu vagy lany):")
        if nem == "fiu" or nem == "lany":
            check=True
        else:
            print("Nem jó. Ujra.")
    nevek.append(nev)
    magassagok.append(magassag)
    nemek.append(nem)
    nev = input("adja meg a nevet")
#//írjuk ki
print("Nev Magassag Nem")
for i in range(len(nevek)):
    print(nevek[i],magassagok[i],nemek[i])
#//Számítsunk átlagot
print("Átlag", sum(magassagok)/len(magassagok))
#//fiuk és lányok átlagmagasság
l = 0
f = 0
lo = 0
fo = 0
for i in range(len(nevek)):
    if nemek[i]=="lany":
        l += 1
        lo += magassagok[i]
    else:
        f += 1
        fo += magassagok[i]
print("Lányok átlagmagassága: ",lo/l," Fiúk átlagmagassága: ",fo/f)

nev = []
nem = []
suly = []
fnev = []
nnev = []
fsuly = []
nsuly = []

def f1():
    neve = input("Kérem a nevet: ")
    while neve != "Vége":
        if neve in nev:
            print("Ez a név szerepel a listában már")
            print("________________")
            neve = input("Kérem a nevet: ")
        elif neve not in nev:
            nev.append(neve)
            neme = int(input("Kérem a nemét(1.férfi/2.nő): "))
            if neme < 1 or neme > 2:
                print("Ilyen nem nem létezik.")
                print("________________")
            else:
                nem.append(neme)
                sulya = int(input("Kérem a súlyát: "))
                suly.append(sulya)
                if neme == 1:
                    fsuly.append(sulya)
                    fnev.append(neve)
                elif neme == 2:
                    nsuly.append(sulya)
                    nnev.append(neve)
                print("________________")
            neve = input("Kérem a nevet: ")

def f2():
    print()
    print("________________")
    nehez = max(fsuly)
    hanyf = fsuly.index(nehez)
    kif = fnev[hanyf]
    print(kif, "a legnehezebb férfi, és ő", nehez, "kg.")

def f3():
    print()
    print("________________")
    konnyu = min(nsuly)
    hanyn = nsuly.index(konnyu)
    kin = nnev[hanyn]
    print(kin, "a legkönnyebb nő, és ő", konnyu, "kg.")

def f4():
    print()
    print("________________")
    print(nev)
    keres = input("Kit akarunk törölni: ")
    if keres in nev:
        hany = nev.index(keres)
        del nev[hany]
        del suly[hany]
        del nem[hany]
    else:
        print("Nem eleme a listának")

    print()
    print(nev)
    print(suly)

print("Beolvasás(1), Legnehezebb férfi(2), Legkönnyebb nő(3), Törlés(4)")
v = int(input(":"))
if v==1:
    f1()
elif v==2:
    f2()
elif v==3:
    f3()
elif v==4:
    f4()
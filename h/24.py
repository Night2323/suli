nevek = []
tsz = []
fá = []

def felvetel(nevek,tsz,fá):
    nev = input("Név:")
    if nev in nevek:
        print("Már benne van!")
        felvetel(nevek, tsz, fá)
    else:
        t = input("Tesók száma:")
        á = input("Félévi átlag:")
        nevek.append(nev)
        tsz.append(t)
        fá.append(á)
    alap(nevek, tsz, fá)

def torol(nevek,tsz,fá):
    nev = input("Törlendő név:")
    if nev in nevek:
        a = nevek.index(nev)
        del nevek[a]
        del tsz[a]
        del fá[a]
    else:
        print("Nincs ilyen név!")
    alap(nevek, tsz, fá)

def modosit(nevek,tsz):
    nev = input("Név:")
    if nev in nevek:
        tsz[nevek.index(nev)] = input("Módosított testvérszám:")
    else:
        print("Nincs ilyen név!")
    alap(nevek, tsz, fá)

def legjobb(nevek,fá):
    legnagyobb = fá.index(max(fá))
    print(nevek[legnagyobb])
    print(max(fá))
    alap(nevek, tsz, fá)

def legtobb(tsz):
    c = 0
    for i in range(len(tsz)):
        if tsz[i]>2:
            c = c+1
        else:
            pass
    return c

def kiir(nevek,tsz,fá,f,g):
    for i in range(f,g):
        try:
            print(nevek[i],"-",tsz[i],"-",fá[i])
        except:
            pass
    n = input("Tovább[enter]/Kilép[exit]")
    if n == "":
        f = f + 5
        g = g + 5
        kiir(nevek,tsz,fá,f,g)
    else:
        alap(nevek,tsz,fá)


def alap(nevek,tsz,fá):
    f = 0
    g = 5
    print("------------------------------------------")
    print("[1]:Adatfelvétel\n[2]:Törlés\n[3]:Tesók száma módosítása\n[4]:Legjobb átlag\n[5]:2-nél testvérrel rendelkező tanulók száma\n[6]:Adatok kiírása\n[7]:Kilépés")
    v = int(input(":"))
    if v == 1:
        felvetel(nevek, tsz, fá)
    elif v == 2:
        torol(nevek, tsz, fá)
    elif v == 3:
        modosit(nevek, tsz)
    elif v == 4:
        legjobb(nevek, fá)
    elif v == 5:
        print(legtobb(tsz))
    elif v == 6:
        print("Név - Tesók száma - Átlag")
        kiir(nevek,tsz,fá,f,g)
    elif v == 7:
        quit()
    print("------------------------------------------")
    alap(nevek, tsz, fá)


alap(nevek, tsz, fá)
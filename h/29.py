nev = []
tel = []
nem = []
fnev = []
ftel = []
fnem = []

def beolvas(nev,tel,nem):
    a = int(input("Beolvasandó emberek száma:"))
    for i in range(a):
        nev.append(input("Név:"))
        tel.append(input("Telefonszám:"))
        nem.append(input("Nem:"))
    alap(nev,tel,nem)



def rend(nev,tel,nem):
    for i in range(len(nev) - 1):
        for j in range(i + 1, len(nev)):
            if nev[j] < nev[i]:
                nev[j], nev[i] = nev[i], nev[j]
                tel[j], tel[i] = tel[i], tel[j]
                nem[j], nem[i] = nem[i], nem[j]
    alap(nev,tel,nem)

def kiir(nev,tel,nem):
    for i in range(len(nev)):
        print(nev[i],tel[i],nem[i])
    alap(nev,tel,nem)

def telker(nev,tel,nem):
    tk = int(input("keresendő telefonszám:"))
    for i in range(len(tel)):
        if tel[i] == tk:
            print(nev[i])
    alap(nev, tel, nem)

def fiuk(nev,tel,nem,fnev,ftel,fnem):
    for i in range(len(nem)):
        if nem[i] == "fiu":
            fnev.append(nev[i])
            ftel.append(tel[i])
            fnem.append(nem[i])
    alap(nev,tel,nem)

def hany(nev,tel,nem,fnev,ftel,fnem):
    print("Fiuk száma:",len(fnev),"Lányok száma:",len(nev)-len(fnev))




def alap(nev,tel,nem):
    v = int(input("1.beolvasás\n2.rendezés\n3.kiir\n4.Telefonszám keresés\n5. Fiuk lista\n6.Hányan vannak"))
    if v == 1:
        beolvas(nev,tel,nem)
    elif v == 2:
        rend(nev,tel,nem)
    elif v == 3:
        kiir(nev,tel,nem)
    elif v == 4:
        telker(nev,tel,nem)
    elif v == 5:
        fiuk(nev,tel,nem,fnev,ftel,fnem)
    elif v == 6:
        hany(nev,tel,nem,fnev,ftel,fnem)
    else:
        quit()

alap(nev,tel,nem)
név = []
tel = []
nem = []

def beolv(név,tel,nem):
    n = int(input("Beolvasások száma:"))
    for i in range(n):
        a = input("Név:")
        b = int(input("Telefonszám:"))
        c = input("Nem:")
        név.append(a)
        tel.append(b)
        nem.append(c)
    alap()

def sort(név,tel,nem):
    asjfh = név
    név2 = név
    tel2 = tel
    nem2 = nem
    print(név2,tel2,nem2)
    asjfh.sort()
    for i in range(len(asjfh)):
        for x in range(len(név2)):
            if i := x:
                név[i] = név2[x]
                tel[i] = tel2[x]
                nem[i] = nem2[x]
    alap()

def kiir(név,tel,nem):
    for i in range(len(név)):
        print(név[i],tel[i],nem[i])
    alap()

def ki(név,tel,nem):
    for i in tel:
        if i == 06202113434:
            print(név[tel.index(tel[i])])
    alap()

def fik(név,tel,nem):
    fnév = []
    ftel = []
    fnem = []
    for i in range(len(név)):
        if nem[i]=="fiu":
            fnév.append(név[i])
            ftel.append(tel[i])
            fnem.append(nem[i])
    print(fnév,ftel,fnem)
    alap()

def alap():
    v = int(input(":"))
    if v==1:
        beolv(név,tel,nem)
    elif v==2:
        sort(név,tel,nem)
    elif v==3:
        kiir(név,tel,nem)
    elif v==4:
        ki(név,tel,nem)
    elif v==5:
        fik(név,tel,nem)

alap()


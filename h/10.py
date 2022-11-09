from random import randrange
# Sipos-Szabó Dénes
def alap():
    v = int(input("1. Első feladat\n2. Második feladat\n3. Kilépés\n"))
    if v == 1:
        f11()
    elif v == 2:
        f2()
    elif v == 3:
        quit()


def f11():
    egesz = int(input("Egész szám: "))
    tort = float(input("Tört szám: "))
    if egesz > tort:
        egesz, tort = tort, egesz
        print(egesz, ",", tort)
        f121(egesz, tort)
    else:
        pass
    f122(egesz, tort)


def f121(egesz, tort):
    egesz, tort = tort, egesz
    if egesz/2 == int(egesz/2):
        print(tort/egesz)
    else:
        pass

def f122(egesz, tort):
    if egesz/2 == int(egesz/2):
        print(tort/egesz)
    else:
        pass


def f2():
    a = randrange(5,10)
    b = randrange(5,10)
    e = a*b
    print(a,"*",b,"=")
    v = int(input())
    if v == e:
        print("Helyes.")
    else:
        print("Nem jó. Helyes:",e)

alap()

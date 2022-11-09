from random import randrange

def alap():
    v = int(input("1. Első feladat\n2. Második feladat\n3. Harmadik feladat\n4. Negyedik feladat\n5. Kilépés\n"))
    if v==1:
        f1()
    elif v==2:
        f2()
    elif v==3:
        f3()
    elif v==4:
        f4()
    elif v==5:
        quit()

def f1():
    nev = input("Név: ")
    print("Szia ",nev)
    szam1 = randrange(1, 100)
    szam2 = randrange(1, 100)
    veg = szam1 * szam2
    print(szam1, " * ", szam2," = ?")
    tipp = int(input())
    if veg == tipp:
        print("gratu")
    else:
        print("nope. Helyes eredmény: ", veg)
    alap()

def f2():
    print("Feleségnek a mocsai szőke lányok a jók!")
    hsz = input("Hajszín: ")
    lh = input("Lakhely: ")
    if hsz=="szőke" and lh=="mocsa":
        print("Jó lesz")
    else:
        print("Nem lesz jó")
    alap()

def f3():
    szam = int(input("Szám: "))
    if szam / 2==int(szam / 2):
        print("A szám páros")
    else:
        print("A szám páratlan")
    alap()

def f4():
    szam = int(input("Szám: "))
    if szam / 3 == int(szam / 3):
        print("A szám osztható hárommal maradék nélkül")
    else:
        print("A szám nem osztható hárommal maradék nélkül")
    alap()

alap()


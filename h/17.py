from random import randrange

def f1():
    nev = " "
    while nev!="Feri":
        nev = input("Név: ")
    print("Üdvözlöm Józsi, Komárom szülöttje!")

def f2():
    sz = 0
    fsz = 0
    while sz != 1:
        a = randrange(1, 20)
        b = randrange(1, 20)
        c = 0
        print(a, "*", b, "=")
        t = int(input("Tipp:"))
        if t == a * b:
            print("Helyes.")
            c = c + 1
        else:
            print("Nem jó. A helyes válasz:", a * b)
        k = int(input("Tovább?(1:igen, 2:nem)"))
        if k == 1:
            fsz = fsz + 1
        elif k == 2:
            sz = sz + 1
    d = (c / fsz) * 100
    if d < 50:
        print("1-es")
    elif 60 > d >= 50:
        print("2-es")
    elif 80 > d >= 60:
        print("3-as")
    elif 90 > d >= 80:
        print("4-es")
    elif d >= 50:
        print("5-ös")

def f3():
    a = 0
    while a!=100:
        a = a+1
        print(a)

def alap():
    print("Első feladat(1), Második feladat(2), Harmadik feladat(3)")
    v = int(input(":"))
    if v==1:
        f1()
    elif v==2:
        f2()
    elif v==3:
        f3()
alap()
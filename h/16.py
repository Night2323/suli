from random import randrange


def a():
    for i in range(1, 5):
        a = randrange(1, 20)
        b = randrange(1, 20)
        c = 0
        print(a, "+", b, "=")
        t = int(input("Tipp:"))
        if t == a + b:
            print("Helyes.")
            c = c + 1
        else:
            print("Nem jó. A helyes válasz:", a + b)
    d = (c / 5) * 100
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

def b():
    a = randrange(1, 10)
    b = randrange(1, 10)
    c = randrange(1, 10)
    def feladat(a,b,c):
        print(a,b,c)
        if a>b and a>c:
            return a
        elif b>a and b>c:
            return b
        elif c>b and c>a:
            return c
        else:
            return "egyenlőek"
    print(feladat(a,b,c),"a legnagyobb")



def c():
    for i in range(1, 20):
        a = randrange(1, 20)
        b = randrange(1, 20)
        c = 0
        print(a, "+", b, "=")
        t = int(input("Tipp:"))
        if t == a + b:
            print("Helyes.")
            c = c + 1
        else:
            print("Nem jó. A helyes válasz:", a + b)
    d = (c / 5) * 100
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


def d():
    sz=0
    fsz=0
    while sz!=1:
        a = randrange(1, 20)
        b = randrange(1, 20)
        c = 0
        print(a, "+", b, "=")
        t = int(input("Tipp:"))
        if t == a + b:
            print("Helyes.")
            c = c + 1
        else:
            print("Nem jó. A helyes válasz:", a + b)
        k=int(input("Tovább?(1:igen, 2:nem)"))
        if k==1:
            fsz = fsz+1
        elif k==2:
            sz = sz+1
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


def alap():
    v = int(input("1. feladat(1), 2. feladat(2), 3.feladat(3), 4.feladat(4)"))
    if v == 1:
        a()
    elif v == 2:
        b()
    elif v == 3:
        c()
    elif v == 4:
        d()


alap()

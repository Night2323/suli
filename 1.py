from random import randrange
from math import *


def osszead():
    szam1 = randrange(1,100)
    szam2 = randrange(1,100)
    veg = szam1+szam2
    print(szam1," + ",szam2)
    tipp = int(input())
    if veg==tipp:
        print("gratu")
    else:
        print("nope. Helyes eredmény: ",veg)
    print("---------------------------------------------------------")
    alapmuveletek()

def kivon():
    szam1 = randrange(1,100)
    szam2 = randrange(1,100)
    veg = szam1 - szam2
    print(szam1, " - ", szam2)
    tipp = int(input())
    if veg == tipp:
        print("gratu")
    else:
        print("nope. Helyes eredmény: ",veg)
    print("---------------------------------------------------------")
    alapmuveletek()

def szoroz():
    szam1 = randrange(1,100)
    szam2 = randrange(1,100)
    veg = szam1 * szam2
    print(szam1, " * ", szam2)
    tipp = int(input())
    if veg == tipp:
        print("gratu")
    else:
        print("nope. Helyes eredmény: ",veg)
    print("---------------------------------------------------------")
    alapmuveletek()

def oszt():
    szam1 = randrange(1,1000)
    szam2 = randrange(1,100)
    veg = szam1 / szam2
    maradek = szam1 % szam2
    veg = int(veg)
    print(maradek)
    print(szam1, " / ", szam2," + maradek")
    maradektipp = input
    tipp = int(input("Eredmény: "))
    maradektipp = int(input("Maradék: "))
    if veg == tipp and maradek == maradektipp:
        print("gratu")
    else:
        print("nope. Helyes eredmény: ",veg,", ",maradek," maradékkal.")
    print("---------------------------------------------------------")
    alapmuveletek()

def alapmuveletek():
    print("1. Összeadás\n2. Kivonás\n3. Szorzás\n4. Osztás\n5. Vissza")
    valasztas = int(input())
    print("---------------------------------------------------------")
    if valasztas==1:
        osszead()
    elif valasztas==2:
        kivon()
    elif valasztas==3:
        szoroz()
    elif valasztas==4:
        oszt()
    elif valasztas==5:
        alap()

def kerter():
    print("1. Háromszög\n2. Négyzet\n3. Kör\n4. Vissza")
    valasztas = int(input())
    print("---------------------------------------------------------")
    if valasztas == 1:
        haromszog()
    elif valasztas == 2:
        negyzet()
    elif valasztas == 3:
        kor()
    elif valasztas == 4:
        alap()

def kor():
    print("1.Kerület\n2.Terület\n3.Vissza")
    pi = float(3.14)
    valasztas = int(input())
    print("---------------------------------------------------------")
    if valasztas == 1:
        korker(pi)
    elif valasztas == 2:
        korter(pi)
    elif valasztas == 3:
        kerter()

def korker(pi):
    r = randrange(1,60)
    print("r: ",r)
    veg = 2*r*pi
    tipp = int(input())
    vegint = int(veg)
    if veg>vegint+0.5:
        vegveg = int(veg+1)
    else:
        vegveg = int(veg)
    if tipp == vegveg:
        print("grat")
    else:
        print("nope")
    print("---------------------------------------------------------")
    kor()

def korter(pi):
    r = randrange(1,60)
    print("r: ",r)
    print(r**2)
    veg = r**2*pi
    vegint = int(veg)
    if veg>vegint+0.5:
        vegveg = int(veg+1)
    else:
        vegveg = int(veg)
    tipp = int(input())
    if tipp == vegveg:
        print("grat")
    else:
        print("nope")
    print("---------------------------------------------------------")
    kor()


def negyzet():
    print("1.Kerület\n2.Terület\n3.Vissza")
    valasztas = int(input())
    print("---------------------------------------------------------")
    if valasztas == 1:
        negyker()
    elif valasztas == 2:
        negyter()
    elif valasztas == 3:
        kerter()

def negyker():
    a = randrange(1,100)
    b = randrange(1,100)
    print("a: ",a)
    print("b: ",b)
    veg = (a+b)*2
    tipp = int(input())
    if tipp == veg:
        print("grat")
    else:
        print("nope")
    print("---------------------------------------------------------")
    negyzet()

def negyter():
    a = randrange(1,100)
    b = randrange(1,100)
    print("a: ", a)
    print("b: ", b)
    veg = a*b
    tipp = int(input())
    if tipp == veg:
        print("grat")
    else:
        print("nope")
    print("---------------------------------------------------------")
    negyzet()

def haromszogker():
    a = randrange(1,30)
    b = randrange(1,30)
    c = randrange(1,30)
    veg = a+b+c
    print("a: ", a)
    print("b: ", b)
    print("c: ", c)
    tipp = int(input())
    if tipp==veg:
        print("grat")
    else:
        print("nope")
    print("---------------------------------------------------------")
    haromszog()

def haromszogeszter():
    a = randrange(1,30)
    b = randrange(1,30)
    while (b+b)<a:
        b = randrange(1,30)
    c = b
    print("a: ", a)
    print("b: ", b)
    print("c: ", c)
    maa = a/2
    ma = sqrt((b*b)-(maa*maa))
    veg = (a/2)*ma
    tipp = int(input())
    vegint = int(veg)
    if veg>vegint+0.5:
        vegveg = int(veg+1)
    else:
        vegveg = int(veg)
    if tipp == vegveg:
        print("grat")
    else:
        print("nope")
    print("---------------------------------------------------------")
    haromszog()

def haromszog():
    print("1. Háromszög kerület\n2. Egyenlő szárú háromszög területe\n3. Vissza")
    valasztas = int(input())
    print("---------------------------------------------------------")
    if valasztas == 1:
        haromszogker()
    elif valasztas == 2:
        haromszogeszter()
    elif valasztas == 3:
        kerter()





def alap():
    print("1. Alap műveltek\n2. Kerület/terület számítás\n3. Kilépés")
    alap = int(input())
    print("---------------------------------------------------------")
    if alap==1:
        alapmuveletek()
    elif alap==2:
        kerter()
    elif alap==3:
        quit()

alap()
from random import *

def f11():
    b = int(input("Kérek egy számot: "))
    c = 0
    if b < 0:
        f11()
    else:
        for d in range(1, b):
            c += d
        print(c)

def f12():
    szo = input("Szó: ")
    szol = list(szo)
    for i in szol:
        print(i)

def f3():
    a = 0
    b = 5
    c = 0
    while a<b:
        a+=1
        sz1 = randrange(1,10)
        sz2 = randrange(1,10)
        v = sz1 * sz2
        print(sz1,"*",sz2,"=")
        t = int(input("Tipp: "))
        if t==v:
            print("Gratulálok helyes válasz.")
            c+=1
        else:
            print("Nem jó válasz. Helyes válasz: ",v)
    d = c / b
    if d < 0.5:
        print("Osztályzat: 1")
    elif d >= 0.5 and d < 0.6:
        print("Osztályzat: 2")
    elif d >= 0.6 and d < 0.7:
        print("Osztályzat: 3")
    elif d >= 0.7 and d < 0.9:
        print("Osztályzat: 4")
    elif d >= 0.9:
        print("Osztályzat: 5")

def f4():
    a = 0
    b = randrange(10,20)
    c = 0
    while a<b:
        a+=1
        sz1 = randrange(1,10)
        sz2 = randrange(1,10)
        v = sz1 * sz2
        print(sz1,"*",sz2,"=")
        t = int(input("Tipp: "))
        if t==v:
            print("Gratulálok helyes válasz.")
            c+=1
        else:
            print("Nem jó válasz. Helyes válasz: ",v)
    d = c / b
    if d < 0.5:
        print("Osztályzat: 1")
    elif d >= 0.5 and d < 0.6:
        print("Osztályzat: 2")
    elif d >= 0.6 and d < 0.7:
        print("Osztályzat: 3")
    elif d >= 0.7 and d < 0.9:
        print("Osztályzat: 4")
    elif d >= 0.9:
        print("Osztályzat: 5")





v = int(input("11-es feladat(1), 12-es feladat(2), 3. feladat(3), 4. feladat(4)"))
if v==1:
    f11()
elif v==2:
    f12()
elif v==3:
    f3()
elif v==4:
    f4()

from random import *

def f1():
    mondat = input("Mondat: ")
    mondatl = list(mondat)
    for i in range(len(mondat)):
        if mondatl[i] == "a" or mondatl[i] == "e" or mondatl[i] == "i" or mondatl[i] == "u" or mondatl[i] == "ü" or mondatl[i] == "o" or mondatl[i] == "á" or mondatl[i] == "é" or mondatl[i] == "ó" or mondatl[i] == "ő" or mondatl[i] == "ö" or mondatl[i] == "ű":
            mondatl[i] = ""
    print("".join(mondatl))

def f2():
    mondat = input("Mondat: ")
    i = len(mondat)
    while i !=0:
        i = i-1
        print(end=mondat[i])

def f3():
    mondat = input("Mondat: ")
    ujszo=""
    for i in range(len(mondat)):
        ujszo=mondat[i::-1]
    print(ujszo)

def f4():
    a = randrange(10)
    b = randrange(10,21)
    c=0
    for i in range(a,b):
        c = c+i
    print(c)

def f5():
    a = randrange(10)
    b = randrange(10, 21)
    c = 0
    for i in range(a,b):
        if i % 2 == 0:
            c = c+1
        else:
            pass
    print(c)

def alap():
    v = int(input("1.Feladat(1), 2.Feladat(2), 3.Feladat(3), 4.Feladat(4), 5.Feladat(5)"))
    if v == 1:
        f1()
    elif v == 2:
        f2()
    elif v == 3:
        f3()
    elif v == 4:
        f4()
    elif v == 5:
        f5()
    else:
        quit()

alap()
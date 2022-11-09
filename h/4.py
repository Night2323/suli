from random import randrange

def alap():
    valasztas = int(input("1: 1. feladat\n2: 2.Feladat\n3: Kilépés\n"))
    if valasztas == 1:
        feladat1()
    elif valasztas == 2:
        feladat2()
    elif valasztas == 3:
        quit()

def feladat1():
    a = randrange(30,60)
    b = randrange(1,30)
    ossz = a+b
    kivon = a-b
    szorz = a*b
    oszt = a/b
    oszt2 = a%b
    oszt3 = int(a/b)
    print(a," + ",b," = ",ossz)
    print(a," - ",b," = ",kivon)
    print(a," * ",b," = ",szorz)
    print(a," / ",b," = ",oszt)
    print(a," % ",b," = ",oszt2)
    print(a," / ",b," = ",oszt3)
    alap()

def feladat2():
    a = int(input("A oldal: "))
    b = int(input("B oldal: "))
    ker = (a+b)*2
    ter = a*b
    print("A téglalap kerülete: ",ker,"\nA téglalap területe: ",ter)
    alap()

alap()
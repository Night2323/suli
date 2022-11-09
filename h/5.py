from math import *

def alap():
    valasztas = int(input("1: 1. feladat\n2: 2. Feladat\n3: Kilépés\n"))
    if valasztas == 1:
        feladat1()
    elif valasztas == 2:
        feladat2()
    elif valasztas == 3:
        quit()

def feladat1():
    print("Hello")
    a = int(input("Első szám:"))
    b = int(input("Második szám:"))
    veg1 = a+b
    print(a," + ",b," = ",veg1)
    veg2 = a-b
    print(a," - ",b," = ",veg2)
    veg3 = a*b
    print(a," * ",b," = ",veg3)
    veg4 = a/b
    print(a," / ",b," = ",veg4)
    veg5 = a**b
    print(a," ** ",b," = ",veg5)
    sqrta = sqrt(a)
    print("Gyök",a," = ",sqrta)
    sqrtb = sqrt(b)
    print("Gyök",b," = ",sqrtb)
    veg4 = int(a/b)
    print(a," / ",b," = ",veg4)
    print("Viszlát")

def feladat2():
    a = [1,2,3,4,5,6,7,8,9,10]
    b = int(input("Szám: "))
    for x in a:
        print(x," * ",b," = ",b*x)


alap()
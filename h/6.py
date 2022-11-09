from math import *

def feladat1():
    nev = input("Név\n")
    print("Szia", nev)
    height = input("Milyen magas vagy?\n")
    weight = input("Milyen nehéz vagy?\n")
    ec = input("Milyen színű a szemed?\n")
    hc = input("Milyen színű a hajad?\n")
    print("A neved",nev,", ",height,"magas vagy, ",weight,"a súlyod, ",ec,"szemed van és",hc,"színű a hajad")

def feladat2():
    a = int(input("Első szám:"))
    b = int(input("Második szám:"))
    veg1 = a + b
    print(a, " + ", b, " = ", veg1)
    veg2 = a - b
    print(a, " - ", b, " = ", veg2)
    veg3 = a * b
    print(a, " * ", b, " = ", veg3)
    veg4 = a / b
    print(a, " / ", b, " = ", veg4)
    veg5 = a ** b
    print(a, " ** ", b, " = ", veg5)
    sqrta = sqrt(a)
    print("Gyök", a, " = ", sqrta)
    sqrtb = sqrt(b)
    print("Gyök", b, " = ", sqrtb)
    veg4 = int(a / b)
    print(a, " / ", b, " = ", veg4)

valasztas = int(input("1: 1. feladat\n2: 2. Feladat\n3: Kilépés\n"))
if valasztas == 1:
    feladat1()
elif valasztas == 2:
    feladat2()
elif valasztas == 3:
    quit()
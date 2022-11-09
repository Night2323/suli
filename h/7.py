def feladat1():
    a = int(input("Szám:"))
    if a==0:
        print("A szám egyenlő nullával.")
    elif a>0:
        print("A szám nagyobb mint nulla.")
    elif a<0:
        print("A szám kisebb mint nulla.")
    alap()

def feladat2():
    a = input("Első szám:")
    b = input("Második szám:")
    c = input("Harmadik szám:")
    alma = [a,b,c]
    print("A legnagyobb szám:",max(alma))
    alap()

def alap():
    valasztas = int(input("1: 1. feladat\n2: 2.Feladat\n3: Kilépés\n"))
    if valasztas == 1:
        feladat1()
    elif valasztas == 2:
        feladat2()
    elif valasztas == 3:
        quit()

alap()
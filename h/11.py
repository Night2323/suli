

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

def f13():
    b = int(input("Kérek egy számot: "))
    if b < 0:
        f13()
    else:
        for d in range(b):
            if d % 2 == 0:
                print("0", end="")
            elif d % 2 == 1:
                print("1", end="")

def f14():
    a = int(input("Kisebb szám: "))
    b = int(input("Nagyobb szám: "))
    if a>=b:
        print("Nem lehet nagyobb az első szám mint a második!")
        f14()
    elif a<b:
        for i in range(a,b+1):
            print(i)

def f15():
    N = int(input("Magasság: "))
    M = int(input("Szélesség: "))
    for i in range(N):
        for v in range(M):
            print(end="* ")
        print("")



v = int(input("11-es feladat(1), 12-es feladat(2), 13-as feladat(3), 14-es feladat(4), 15-ös feladat(5)"))
if v==1:
    f11()
elif v==2:
    f12()
elif v==3:
    f13()
elif v==4:
    f14()
elif v==5:
    f15()
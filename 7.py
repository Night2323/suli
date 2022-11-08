from random import randrange
def f1():
    nev = input("Név:")
    a = int(input("Szám: "))
    if a/2==int(a/2):
        print(nev,"a szám páros.")
    else:
        print(nev,"a szám páratlan.")

def f2():
    a = randrange(5,10)
    b = randrange(5,10)
    v = int(input("Szorozni(1) vagy összeadni(2)?"))
    if v==1:
        e = a*b
        print(a,"*",b,"=")
        val = int(input())
        if val == e:
            print("Helyes")
        else:
            print("Nem jó. A helyes válasz:",e)
    else:
        e = a + b
        print(a, "+", b, "=")
        val = int(input())
        if val == e:
            print("Helyes")
        else:
            print("Nem jó. A helyes válasz:", e)

def valaszto():
    vv = int(input())
    if vv==1:
        f1()
    else:
        f2()



a = 6
b = 7
a, b = b, a
print(a)
print(b)
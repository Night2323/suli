from random import randrange

nev = input("Név:")
penz=500

def alap(penz,nev):

    v = int(input("1: 1. feladat\n2: 2. feladat\n3: kilépés\n"))
    if v==1:
        f1(nev)
    elif v==2:
        f2(penz,nev)
    elif v==3:
        quit()

def f1(nev):
    mag=int(input("Magasság: "))
    if mag<=150:
        print(nev,",törpe vagy.")
    elif mag>150 and mag<180:
        print(nev,",",190-mag,"cm hiányzik a 190cm-hez.")
    elif mag>=180:
        print(nev,"menny el kosarasnak a",mag,"cm magasságoddal.")
    alap(penz,nev)

def f2(penz,nev):
    jel=input("Jelszó: ")
    if jel=="Feri":
        f2a(penz)
    else:
        print("Sajnálom",nev,"nem ez a jelszó")
    alap(penz,nev)

def f2a(penz):
    v=int(input("Szeretnél pénzre játszani? 1:igen 2:nem\n"))
    if v==1:
        print(penz,"Ft-od van jelenleg")
        if penz>=500:
            pass
        else:
            print("Nincs elegendő pénzed a játékhoz.")
            alap(penz,nev)
        penz=penz-500
        a=randrange(2)
        t=int(input("Fej(0)vagy Írás(1)\n"))
        if a==0:
            g2="fej"
            g1="írás"
        else:
            g2="írás"
            g1="fej"
        if a==t:
            print("Gratulálok",g1,"volt a helyes ezért nyertél 1000Ft-ot")
            penz=penz+1000
        else:
            print("Sajnálom a helyes válasz",g2,"volt")
        f2a(penz)
    elif v==2:
        print("Holnapra tanulj")
    alap(penz,nev)



alap(penz,nev)
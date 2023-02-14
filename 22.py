ListNev = []
ListTel = []
def f1(a):
    tel = open(a, "w", encoding="UTF-8")
    nev = input("Név: ")
    while nev!="vege":
        telo = input("Telefonszám: ")
        tel.write(nev+";"+telo+"\n")
        nev = input("Név:")


def f2(a):
    tel = open(a, "a", encoding="UTF-8")
    nev = input("Név: ")
    while nev != "vege":
        telo = input("Telefonszám: ")
        tel.write(nev + ";" + telo + "\n")
        nev = input("Név:")

def f3(a,ListNev,ListTel):
    tel = open(a,"r",encoding="UTF-8")
    sor = tel.readline()
    while sor!="":
        sor.strip()
        print(sor.replace(";"," - "))
        temp = sor.split(";")
        ListNev.append(temp[0])
        ListTel.append(temp[1])
        sor = tel.readline()

a = input("Fájl neve(név.kit):")
print("Törlés és írás(1), Hozzáadás(2), Olvasás(3)")
v = int(input(":"))
if v==1:
    f1(a)
elif v==2:
    f2(a)
elif v==3:
    f3(a,ListNev,ListTel)
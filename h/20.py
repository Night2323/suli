from random import randrange
nevek = []
cimek = []
nev = ""
while nev != "Vége":
    nev = input("Név:")
    cim = input("Cím:")
    nevek.append(nev)
    cimek.append(cim)

keres = input("Keresendő név:")
if keres in nevek:
    print(cimek[nevek.index(keres)])

uj = input("Név: ")
if uj not in nevek:
    nevek.append(uj)
    cimek.append(input("Cím: "))

delet = input("Kitörlendő név:")
if delet in nevek:
    cimek.pop(nevek.index(delet))
    nevek.remove(delet)

list = []
a = 0
while a != 5:
    num = randrange(90)
    if num not in list:
        list.append(num)
    else:
        a-=1
    a+=1
    print(a)

print(list)

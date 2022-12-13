nevek = []
nemek = []
sulyok = []
f = []
a = 0
i = True
#----------------
while i!=False:
    print("------------")
    nev = input("Név:")
    if nev == "vége" or nev == "Vége":
        i=False
    else:
        if nev in nevek:
            print("Már benne van.")
        else:
            nem = input("Nem:")
            suly = int(input("Súly:"))
            nevek.append(nev)
            nemek.append(nem)
            sulyok.append(suly)
#----------------
for i in range(len(nemek)):
    if nemek[i] == "nő":
        a = a + sulyok[i]
print(a)
#----------------
for i in range(len(nemek)):
    if nemek[i] == "férfi":
        f.append(sulyok[i])
print(sum(f)/len(f))
#----------------
print(sum(sulyok))
#----------------
d = input("Törlendő név:")
if d in nevek:
    n = nevek.index(d)
    print(n)
    nevek.remove(nevek[n])
    nemek.remove(nemek[n])
    sulyok.remove(sulyok[n])
else:
    print("nincs ilyen név a listában")
print(nevek,nemek,sulyok)
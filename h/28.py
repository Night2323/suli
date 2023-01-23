def legnehezebb(nev,cim,suly,n):
    print("A legnehezebb ember neve:",nev[n-1],"aki",suly[n-1],"kg és",cim[n-1],"a lakhelye.")

nev = []
cim = []
suly = []
knev = []
kcim = []
ksuly = []
enev = []
ecim = []
esuly = []
neve = input("Hogy hívják: ")
while neve != "Vége":
    sulya = int(input("Hány kiló: "))
    cime = input("Hol lakik: ")
    nev.append(neve)
    suly.append(sulya)
    cim.append(cime)
    if cime == "Komárom":
        knev.append(neve)
        kcim.append(cime)
        ksuly.append(sulya)
    else:
        enev.append(neve)
        ecim.append(cime)
        esuly.append(sulya)

    neve = input("Hogy hívják: ")

n = len(suly)
for i in range(n-1):
    for j in range(i+1,n):
        if suly[j] < suly[i]:
            suly[j], suly[i] = suly[i], suly[j]
            cim[j], cim[i] = cim[i], cim[j]
            nev[j], nev[i] = nev[i], nev[j]
for i in range(n):
    print(nev[i],cim[i],suly[i])

legnehezebb(nev,cim,suly,n)

c = len(ksuly)
for i in range(c):
    print(knev[i],kcim[i],ksuly[i])

komaromi = len(knev)
egyeb = len(enev)
osszesen = len(nev)
print("Komáromban",komaromi,"ember lakik, máshol",egyeb,"ember lakik és összesen",osszesen,"ember van.")


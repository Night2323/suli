nev = []
cim = []
suly = []
InNev = "a"
while InNev!="vége":
    InNev = input("Név:")
    if InNev == "vége":
        pass
    else:
        nev.append(InNev)
        InCim = input("Cím:")
        cim.append(InCim)
        InSuly = input("Súly:")
        suly.append(InSuly)

for i in range(len(suly)-1):
    for j in range(i+1,len(suly)):
        if i < j:
            nev[i], nev[j] = nev[j], nev[i]
            cim[i], cim[j] = cim[j], nev[i]
            suly[i], suly[j] = cim[j], suly[i]

for i in range(len(nev)):
    print(nev[i],cim[i],suly[i])

def legneh(cim,suly):
    return cim[suly.index(max(suly))]

print(legneh(cim,suly))

KomNev = []
KomCim = []
KomSuly = []


for i in range(len(nev)):
    if cim[i]=="komárom":
        KomNev.append(nev[i])
        KomCim.append(cim[i])
        KomSuly.append(suly[i])

for i in range(len(KomNev)):
    print(KomNev[i],KomCim[i],KomSuly[i])

print("Adatok száma:",len(nev),"Komáromiak száma:",len(KomNev),"Más helyen lakók száma:",len(nev)-len(KomNev))
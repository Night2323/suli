nevek = []
nemek = []
sulyok = []
i = True

def nembeiro(nem,check):
    nem = input("Nem(férfi/nő):")
    if nem=="férfi" or nem=="nő":
        check = True
    else:
        print("Nem jó.")
    return check

while i!=False:
    print("------------")
    nev = input("Név:")
    if nev == "vége" or nev == "Vége":
        i=False
    else:
        if nev in nevek:
            print("Már benne van.")
        else:
            check = False
            nem = ""
            while nembeiro(nem,check)!=True:
                pass
            suly = int(input("Súly:"))
            nevek.append(nev)
            nemek.append(nem)
            sulyok.append(suly)


noknevek = []
noksulyok = []
ferfiaknevek = []
ferfiaksulyok = []
for i in range(len(nevek)):
    if nemek[i]=="férfi":
        d = nevek[i]
        ferfiaknevek.append(d)
        e = sulyok[i]
        ferfiaksulyok.append(e)
    elif nemek[i]=="nő":
        d = nevek[i]
        noknevek.append(d)
        e = sulyok[i]
        noksulyok.append(e)

print(noknevek,noksulyok)
print(ferfiaknevek,ferfiaksulyok)

print(ferfiaknevek[ferfiaksulyok.index(max(ferfiaksulyok))],max(ferfiaksulyok))
print(noknevek[noksulyok.index(min(noksulyok))],min(noksulyok))
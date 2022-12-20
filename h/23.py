nevek = []
nemek = []
sulyok = []
i = True

while i!=False:
    print("------------")
    nev = input("Név:")
    if nev == "vége" or nev == "Vége":
        i=False
    else:
        if nev in nevek:
            print("Már benne van.")
        else:
            check=False
            nem = ""
            while check!=True:
                nem = input("Nem(férfi/nő):")
                if nem == "férfi" or nem == "nő":
                    check=True
                else:
                    print("Nem jó.")
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
        ferfiaknevek.append(nevek[i])
        ferfiaksulyok.append(int(sulyok[i]))
    elif nemek[i]=="nő":
        noknevek.append(nevek[i])
        noksulyok.append(int(sulyok[i]))

print(noknevek,noksulyok)
print(ferfiaknevek,ferfiaksulyok)

print(ferfiaknevek[ferfiaksulyok.index(max(ferfiaksulyok))],max(ferfiaksulyok))
print(noknevek[noksulyok.index(min(noksulyok))],min(noksulyok))


n = int(input("Beolvasások száma"))
i = 0
while i!=n:
    print(n-i,"beolvasás van még.")
    nev = input("Név:")
    nem = input("Nem(fiu vagy lany):")
    suly = input("Suly:")
    if nem == "fiu":
        FileF = open("20f.txt", "a", encoding="UTF-8")
        FileF.write(nev+";"+nem+";"+suly+"\n")
        FileF.close()
        i += 1
    elif nem == "lany":
        FileL = open("20l.txt", "a", encoding="UTF-8")
        FileL.write(nev+";"+nem+";"+suly+"\n")
        FileL.close()
        i += 1
    elif nem != "lany" or nem !="fiu":
        print("nincs ilyen nem")
#név nem suly
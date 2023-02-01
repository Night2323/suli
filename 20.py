n = int(input("Beolvasások száma"))
for i in range(n):


    nev = input("Név:")
    nem = input("Nem:")
    suly = input("Suly:")
    if nem == "fiu":
        FileF = open("20f.txt", "a", encoding="UTF-8")
        FileF.write(nev+";"+nem+";"+suly)
        FileF.close()
    elif nem == "lany":
        FileL = open("20l.txt", "a", encoding="UTF-8")
        FileL.write(nev+";"+nem+";"+suly)
        FileL.close()
    else:
        print("nincs ilyen nem")
        i = i-1



#név nem suly
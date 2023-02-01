file=open("nevek.txt","a",encoding="UTF-8")
nev=input("Adjon egy nevet!")
while nev!="vege":
    suly=input("Súly:")
    file.write(nev+";"+suly+"\n")
    nev = input("Adjon egy nevet!")
file.close()
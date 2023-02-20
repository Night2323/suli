LiSorsz = []
LiNev = []
LiNemz = []
LiLeg = []
file = open("dobas.txt","r",encoding="UTF-8")
sor = file.readline()
while sor!="":
    sor = sor.strip()
    print(sor.replace(";"," - "))
    temp = sor.split(";")
    LiSorsz.append(temp[0])
    LiNev.append(temp[1])
    LiNemz.append(temp[2])
    LiLeg.append(temp[3])
    sor = file.readline()

print(len(LiSorsz),"versenyző adata van a fájlban.")
a = 0
i = 1
while i!=len(LiLeg)-1:
    i+=1
    a = a + float(LiLeg[i])
    print(a)
print(round(a/(len(LiLeg)-1),3),"az átlaga a legnagyobb dobásoknak.")

b = input("Név:")
c = float(input("Dobás mérete:"))
ListHely = []
ListSpSzam = []
ListSaNev = []
ListVszNev = []


file = open("Helsinki.txt","r",encoding="windows-1250")
sor = file.readline()
while sor!="":
    sor = sor.strip()
    print(sor.replace(";"," - "))
    temp = sor.split(";")
    ListHely.append(temp[0])
    ListSpSzam.append(temp[1])
    ListSaNev.append(temp[2])
    ListVszNev.append(temp[3])
    sor = file.readline()

for i in range(len(ListHely))
    if ListHely[i]=="1" or ListHely[i]=="2" or ListHely[i]=="3":
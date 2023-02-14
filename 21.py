id = []
name = []
date = []
enekes = open("enekes.txt","r",encoding="UTF-8")
fejlec = enekes.readline()
print(fejlec)
sor = enekes.readline()
while sor!="":
    sor=sor.strip()
    templist=sor.split(";")
    sor=sor.replace(";"," - ")
    id.append(int(templist[0]))
    name.append(templist[1])
    date.append(int(templist[2]))
    print(sor)
    sor = enekes.readline()
print(id,name,date)
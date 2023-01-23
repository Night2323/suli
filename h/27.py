ir = []
vá = []
ira = 1
while ira!=0:
    ira = int(input("Irányítószám: "))
    if ira==0:
        pass
    else:
        ir.append(ira)
        vá.append(input("Város: "))
print(" ",ir,"\n",vá)

pir = []
pvá = []
for i in range(len(ir)):
    if ir[i]%2!=0:
        pir.append(ir[i])
        pvá.append(vá[i])
    else:
        pass

print(" ",pir,"\n",pvá)

print(len(ir),"város van a listában.")

print(vá[ir.index(max(ir))],"-nek van a legnagyobb irányítőszáma.")

pir.sort()


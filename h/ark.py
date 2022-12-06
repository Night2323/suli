crntlvl = int(input("Jelenlegi szint: "))
crntxp = int(input("Jelenlegi xp szint: "))
for i in range(70):
    lvl = i*500
    if lvl+250>crntxp-250>lvl-250:
        print(crntlvl-i,"szint az eredeti")


alma = [10,10,10,10,10,10]
print(alma.count(1))
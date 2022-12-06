from random import randrange

def alma():
    list = []
    for i in range(10):
        list.append(randrange(1000000))
    print(list)
    tipp = int(input("Elem:"))
    bve = tipp in list
    if bve==True:
        print("benne van a(z)",tipp)
        quit()
    elif bve==False:
        print("Nincs benne a(z)",tipp)
        for i in list:
            korte = [tipp,i]
            korte = korte.sort()
            a = 1000000
            if a>korte[1]-korte[2]:
                a = korte[1] - korte[2]
        print(a,"távolságra voltál a legközelebbitől")

    alma()

alma()
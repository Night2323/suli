def f1():
    N = int(input("Mennyi elem legyen a lista?: "))
    lista = [0] * N
    for i in range(N):
        lista[i] = input("Kérek egy értéket: ")

    c = len(lista)
    for b in range(c):
        print(lista[b])

def f2():
    lista = []
    N = int(input("Mennyi adatot tegyünk be?: "))
    for i in range(N):
        a = input("Kérek egy számot: ")
        lista.append(a)

    c = len(lista)
    for b in range(c):
        print(lista[b])


def f3():
    N = int(input("Kérek egy számot: "))
    lista = []
    while N != -1:
        lista.append(N)
        N = int(input("Kérek egy számot: "))

    c = len(lista)
    for b in range(c):
        print(lista[b])

print("1. feladat(1), 2. feladat(2), 3. feladat(3)")
v = int(input(":"))
if v==1:
    f1()
elif v==2:
    f2()
elif v==3:
    f3()
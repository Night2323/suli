from random import randrange

def f15():
    N = int(input("Magasság: "))
    M = int(input("Szélesség: "))
    for i in range(N):
        for v in range(M):
            print(end="* ")
        print("")

def f17(a,b,c):
    if a<10 and b<10 and c<10:
        return True
    else:
        return False

def f20(a):
    e = 0
    while e!=int(a/3):
        e = e+1
        for i in range(3):
            if i==2:
                print(end="+")
            else:
                print(end="-")
    for l in range(a%3):
        print("-")



def alap():
    v = int(input("15.(1),17.(2),20.(3)"))
    a = randrange(1, 20)
    b = randrange(1, 20)
    c = randrange(1, 20)
    if v==1:
        f15()
    elif v==2:
        print(f17(a,b,c))
    elif v==3:
        f20(a)

alap()

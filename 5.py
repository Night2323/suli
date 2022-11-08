def f2():
    a = int(input("a:"))
    b = int(input("b:"))
    if a/2 == int(a/2) and b/2 == int(b/2):
        print(a*b)
    else:
        print(a+b)
    print("__________________________________")
    alap()

def f1():
    a = int(input("a:"))
    b = int(input("b:"))
    if a>b:
        print(a-b)
    else:
        print(b-a)
    print("_________________________________")
    alap()

def alap():
    v = int(input("F1:1 F2:2\n"))
    if v==1:
        f1()
    elif v==2:
        f2()
    elif v==3:
        quit()

alap()
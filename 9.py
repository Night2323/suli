from time import *
from datetime import *
def alap():
    v=int(input())
    if v==1:
        f1()
    elif v==2:
        f2()



def f1():
    alma = 0
    while alma < 10:
        alma = alma + 1
        sleep(2)
        print(alma)
        print(datetime.now())

def f2():
    alma=0
    while alma<1000:
        alma = alma+1
        if alma==1:
            print(datetime.now())
        elif alma==1000:
            print(datetime.now())
    print("------------------------------------")
    for alma in range(0,1001):
        if alma == 1:
            print(datetime.now())
        elif alma ==  1000:
            print(datetime.now())
alap()

#401291,414238
#414238,420218
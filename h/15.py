from random import *
import re

def f20(a):
    e = 0
    while e!= int(a/3):
        e = e+1
        for i in range(3):
            if i==2:
                print(end="+")
            else:
                print(end="-")
    for l in range(a%3):
        print("-")

def f22():
    szo = input("Szó: ")
    szo = szo.replace(" ","")
    print(szo)

def f11():
    a = int(input("Szám: "))
    b = 0
    i=a
    while i!=1:
        i = i-1
        b = b+i
    print(b)

def f8():
    a = int(input("Szám: "))
    for i in range(1,a):
        if i%3==0:
            print(i)



def alap():
    v = int(input("20.(1),22.(2),11.(3),8.(4)"))
    a = randrange(1,20)
    if v==1:
        f20(a)
    elif v==2:
        f22()
    elif v==3:
        f11()
    elif v==4:
        f8()

alap()
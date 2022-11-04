from random import randrange
from math import sqrt

def randommasodfoku():
    a = randrange(5)
    b = randrange(20)
    c = randrange(-10,10)
    print(str(a)+"x^2+"+str(b)+"x+"+str(c))
    print("x=(",-b,"+- sqrt(",b,"^ 2 - 4 *",a,"*",c,")  / ( 2 *",a,")")
    try:
        x1 = ((-1*b)+sqrt(b**2-4*a*c))/2*a
        x2 = ((-1*b)-sqrt(b**2-4*a*c))/2*a
        print("x1 =",x1,"és x2 =",x2)
    except:
        print("Nincs helyes válasz.")

def masdodfokszamolo():
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    print(str(a) + "x^2+" + str(b) + "x+" + str(c))
    print("x=(", -b, "+- sqrt(", b, "^ 2 - 4 *", a, "*", c, ")  / ( 2 *", a, ")")
    try:
        x1 = ((-1 * b) + sqrt(b ** 2 - 4 * a * c)) / 2 * a
        x2 = ((-1 * b) - sqrt(b ** 2 - 4 * a * c)) / 2 * a
        print("x1 =", x1, "és x2 =", x2)
    except:
        print("Nincs helyes válasz.")

randommasodfoku()
masdodfokszamolo()
def dectobin():
    decimal = int(input("Szám:"))
    binary = bin(decimal).replace("0b","")
    print(binary)

def bintodec():
    binary = input("Szám:")
    decimal = int(binary,2)
    print(decimal)

def a():
    v = int(input("Dec to bin(1),Bin to dec(2):"))
    if v==1:
        dectobin()
    elif v==2:
        bintodec()
    a()
a()
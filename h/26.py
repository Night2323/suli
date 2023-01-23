def osztható(a):
    if a%2==0 and a%3==0:
        return True
    else:
        return False

def fő():
    a = int(input("Szám:"))
    print("A beolvasott szám:",a,"és a visszatérési érték:",osztható(a))

fő()
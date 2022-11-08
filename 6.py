def fizseb(g):
    s = float(input("s(m)="))
    t = float(input("t(sec)="))
    v = s/t
    print("v=s/t=",s,"/",t,"=",v)
    print("---------------------------------------------------------")
    fiz()

def fizgyors(g):
    v = float(input("v(m/s)="))
    t = float(input("t(sec)="))
    a = v/t
    print("a=v/t=", v, "/", t, "=", a)
    print("---------------------------------------------------------")
    fiz()

def fizsu(g):
    m = float(input("m(kg)="))
    G = m*g
    print("G=m*g=",m,"*",g,"=",G)
    print("---------------------------------------------------------")
    fiz()

def fiz():
    g = float(input("9.81 vagy 10"))
    if g==10 or g==9.81:
        pass
    else:
        print("buta")
        fiz()
    print("1. Sebesség\n2. Gyorsulás\n3. Súly")
    v = int(input())
    print("---------------------------------------------------------")
    if v==1:
        fizseb(g)
    elif v==2:
        fizgyors(g)
    elif v==3:
        fizsu(g)
        
fiz()
    

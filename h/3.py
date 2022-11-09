szam = int(input("0-4095: "))
if szam>4095:
    print("nem")
else:
    if szam > 2048:
        szam2 = szam - 2048
        a = int(1)
    else:
        a = int(0)
        szam2 = szam

    if szam2 > 1024:
        szam3 = szam2 - 1024
        b = int(1)
    else:
        szam3 = szam2
        b = int(0)

    if szam3 > 512:
        szam4 = szam3 - 512
        c = int(1)
    else:
        szam4 = szam3
        c = int(0)

    if szam4 > 256:
        szam5 = szam4 - 256
        d = int(1)
    else:
        szam5 = szam4
        d = int(0)

    if szam5 > 128:
        szam6 = szam5 - 128
        e = int(1)
    else:
        szam6 = szam5
        e = int(0)

    if szam6 > 64:
        szam7 = szam6 - 64
        f = int(1)
    else:
        szam7 = szam6
        f = int(0)

    if szam7 > 32:
        szam8 = szam7 - 32
        g = int(1)
    else:
        szam8 = szam7
        g = int(0)

    if szam8 > 16:
        szam9 = szam8 - 16
        h = int(1)
    else:
        szam9 = szam8
        h = int(0)

    if szam9 > 8:
        szam10 = szam9 - 8
        i = int(1)
    else:
        szam10 = szam9
        i = int(0)

    if szam10 > 4:
        szam11 = szam10 - 4
        j = int(1)
    else:
        szam11 = szam10
        j = int(0)

    if szam11 > 2:
        szam12 = szam11 - 2
        k = int(1)
    else:
        szam12 = szam11
        k = int(0)

    if szam12 == 1:
        l = int(1)
    else:
        l = int(0)

    print(a, b, c, d, e, f, g, h, i, j, k, l)


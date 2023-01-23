e = int(input("Kérem adja meg az életkorát: "))
if e < 18:
    print("Ön",e,"éves tehát kiskorú!")
elif e == 18:
    print("Ön pont 18 éves!")
elif e > 18:
    print("Ön",e,"éves tehát nagykorú")
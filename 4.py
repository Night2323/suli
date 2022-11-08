allat = input("Állatfaj: ")
seb = int(input("Sebessége(km/h): "))
hol = str()
if seb<=50:
    hol = "városban"
elif seb>50 and seb<=90:
    hol = "oszáguton"
elif seb>90 and seb<=120:
    hol = "autópályán"
elif seb>120:
    hol = "német autópályán"

print("A(z)",allat,"a legnagyobb sebességével",hol,"haladhat.")
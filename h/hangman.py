kesze = False
kitalalt = []
erszo = input("Szó: ")
szo = list(erszo)
for i in range(len(szo)):
    kitalalt.append("_")

while kesze==False:
    if "_" in kitalalt:
        kesze = False
    else:
        kesze = True

    def bve(kitalalt, szo):
        tipp = input("Következő tipp:")
        while tipp in szo:
            a = szo.index(tipp)
            kitalalt[a] = tipp
            szo[a] = "talalt"
        return kitalalt
        return szo

    bve(kitalalt, szo)
    print("".join(kitalalt))



#megkelkáposztástalaníhatatlanságoskodásaitokért

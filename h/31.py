class base():
    def __init__(self):
        self.ListNev = []
        self.ListVaros = []
        self.ListOrsz = []
        self.ListMag = []
        self.ListEm = []
        self.ListDate = []
        self.a = 0
        self.olvas()


    def olvas(self):
        file = open("legmagasabb.txt","r",encoding="UTF-8")
        sor = file.readline()
        sor = file.readline()
        while sor!="":
            sor = sor.strip()
            temp = sor.split(";")
            self.ListNev.append(temp[0])
            self.ListVaros.append(temp[1])
            self.ListOrsz.append(temp[2])
            self.ListMag.append(temp[3].replace(",","."))
            self.ListEm.append(float(temp[4]))
            self.ListDate.append(temp[5])
            sor = file.readline()
            self.a = 1
        self.hany()

    def hany(self):
        print(len(self.ListNev)-1,"épület található.")
        self.emsum()

    def emsum(self):
        print(sum(self.ListEm),"emelet van összesen az épületekben.")
        d = self.ListMag.index(max(self.ListMag))
        print("Legmagasabb épület:")
        print(" Név:",self.ListNev[d])
        print(" Város:",self.ListVaros[d])
        print(" Ország:", self.ListOrsz[d])
        print(" Magasság:", self.ListMag[d])
        print(" Emeletek száma:", self.ListEm[d])
        print(" Építés éve:", self.ListDate[d])
        self.olasze()

    def olasze(self):
        if "Olaszország" in self.ListVaros:
            print("Van olasz város")
        else:
            print("nincs")

base()
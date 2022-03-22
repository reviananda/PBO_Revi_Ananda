class Segiempat() :
    def __init__(self, panjang, lebar) :
        self.panjang = panjang
        self.lebar = lebar
    
    def hitungLuas(self) :
        print(f"Luas Segiempat : {self.panjang * self.lebar}")

class Bujursangkar(Segiempat) :
    def __init__(self,sisi) :
        self.side = sisi
        Segiempat.__init__(self, sisi, sisi)
   

   
    def hitungLuas(self) :
        print(f"Luas Bujur Sangkar = {self.side * self.side}")

b = Bujursangkar(4)
s = Segiempat(2, 4)
b.hitungLuas()
s.hitungLuas()
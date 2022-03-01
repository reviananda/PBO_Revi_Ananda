class Titik :
    def _init_(self,x,y) :
        self.x = x
        self.y = y

class Garis :
    def _init_(self, titik_pertama, titik_kedua) :
        self.titik_pertama = titik_pertama
        self.titik_kedua = titik_kedua

    def panjang(self) :
        panjangX = self.titik_kedua.x - self.titik_pertama.x
        panjangY = self.titik_kedua.y - self.titik_pertama.y
        panjang = (panjangX*2 + panjangY2) * 0.5
        return panjang

titikA = Titik(0,0)
titikB = Titik(3,4)
garis_AB = Garis(titikA,titikB)
print('Panjang garis AB adalah {}'.format(garis_AB.panjang()))
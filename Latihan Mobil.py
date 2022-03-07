#Protected
class Mobil :
    def _init_(self, jendela, pintu, mesin) :
        self._jendela = jendela
        self._pintu = pintu 
        self._mesin = mesin

audi = Mobil(4, 4, "Disel")

class Truk(Mobil) :
    def _init_ (self, jendela, pintu, mesin, tipe) :
        super()._init_(jendela, pintu, mesin) 
        self.tipebak = tipe

truk = Truk(4, 2, "Disel", "Bak Terbuka")
print(truk._mesin)
print(truk.tipebak)
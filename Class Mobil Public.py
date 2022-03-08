#public
class Mobil :
    def _init_(self, jendela, pintu, mesin) :
        self.jendela = jendela
        self. pintu = pintu 
        self.mesin = mesin

audi = Mobil(4, 4, "Disel")
print(audi.jendela)
print(audi.pintu)
print(audi.mesin)
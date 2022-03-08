#private
class Mobil() :
    def _init_(self, jendela, pintu, mesin) :
        self.__jendela = jendela
        self.__pintu = pintu
        self.__mesin = mesin

    def Tampil(self) :
        print(f"Jendela : {self.__jendela}")
        print(f"Pintu : {self.__pintu}")
        print(f"Mesin : {self.__mesin}")

audi = Mobil(4,4,"Diesel")
audi.Tampil()
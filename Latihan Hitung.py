class Hitung :
    def _init_ (self) :
         self.__angkaRahasia = 0

    def tampilHitung(self) :
        self.__angkaRahasia += 1
        print(self.__angkaRahasia)

hitungan = Hitung()
hitungan.tampilHitung()
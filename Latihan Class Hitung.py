class Hitung :
    def __init__ (self) :
         self.__angkaRahasia = 0

    def tampilHitung(self) :
        self.__angkaRahasia += 1
        print(self.__angkaRahasia)

hitungan = Hitung()
hitungan.tampilHitung()
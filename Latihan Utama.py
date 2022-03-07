class Utama :
    def _init_ (self) :
        self._a = 2

class Turunan(Utama) :
    def _init_(self) :
        #Memanggil konstuktor kelas utama
        Utama._init_(self)

        #Modify the protected variable
        self._a = 3

objek1 = Turunan()
objek2 = Utama()

#Memanggil variable protected
print(f"Mengakses variable protected dari objek1 : {objek1._a}")
print(f"Mengakses variable protected dari objek1 : {objek2._a}")
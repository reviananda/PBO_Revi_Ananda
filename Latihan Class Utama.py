class Utama :
    def __init__ (self) :
        self._a = 2

class Turunan(Utama) :
    def __init__(self) :
        #Memanggil konstuktor kelas utama
        Utama.__init__(self)

        #Modify the protected variable
        self._a = 3

objek1 = Turunan()
objek2 = Utama()

#Memanggil variable protected
print(f"Mengakses variable protected dari objek1 : {objek1._a}")
print(f"Mengakses variable protected dari objek1 : {objek2._a}")
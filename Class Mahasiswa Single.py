#Parent Class
class Induk :
    def fungsiinduk(self) :
        print("Fungsi pada parent class.")

#Class turunan 
class Anak(Induk) :
    def fungsianak(self) :
        print("Fungsi pada anak.")

#Objek
child = Anak()

child.fungsiinduk()

child.fungsiinduk()
#Parent Class
class Induk :
    def fungsiinduk(self) :
        print("Fungsi pada parent class.")

#Class turunan 1
class Anak1(Induk) :
    def fungsianak1(self) :
        print("Fungsi pada anak 1.")

#Class turunan 2
class Anak2(Induk) :
    def fungsianak2(self) :
        print("Fungsi pada anak 2.")

#Objek
child1 = Anak1()
child2 = Anak2()

child1.fungsiinduk()
child1.fungsianak1()

child2.fungsiinduk()
child2.fungsianak2()
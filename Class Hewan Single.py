# Single Inheritance

#Parent Class
class Hewan :   
    def bersuara(self) :
        print("Kucing Bersuara")

# Anak class mewarisi parent class
class Kucing(Hewan) :
    def suara(self) :
        print("meong...meong")

#Objek
cat = Kucing()
cat.suara()
cat.bersuara()
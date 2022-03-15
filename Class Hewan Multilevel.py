#Parent Class
class Hewan :
    def bersuara(self) :
        print("Kucing Bersuara")

#Anak class mewarisi class hewan
class Kucing(Hewan) :
    def suara(self) :   
        print("meong...meong")

#Anak class Anakkucing mewarisi dari class hewan
class AnakKucing(Kucing) :
    def minum(self) :   
        print("Minum Susu")

#Objek
kitten = AnakKucing()
kitten.bersuara()
kitten.suara()
kitten.minum()
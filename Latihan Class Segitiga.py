class Segitiga :
    def __init__(self, alas, tinggi) :
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi

segitigaBesar = Segitiga(100, 80)
print(f"Alas : {segitigaBesar.alas}")
print(f"Tinggi : {segitigaBesar.tinggi}")
print(f"Luas : {segitigaBesar.luas}")
class Mahasiswa :
    def __init__ (self, nama, nim, prodi) :
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

mahasiswa1 = Mahasiswa("Yuna", "8167216716", "Ilmu Komputer")
mahasiswa2 = Mahasiswa("Jeno", "1789276401", "Teknik Elektro")
mahasiswa3 = Mahasiswa("Nancy", "156289176", "Akuntansi")
mahasiswa4 = Mahasiswa("Felix", "6271892643", "Teknik Listrik")

mahasiswa = [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4]
print("\nList Mahasiswa")
for mhs in mahasiswa :
    teks = '{} adalah mahasiswa {} dengan nim {}'. format(mhs.nama, mhs.prodi, mhs.nim )
    print(teks)
print("\n")
#private
class Mahasiswa :
    def __init__ (self, nama, nim, prodi, fakultas) :
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.fakultas = fakultas

mahasiswa1 = Mahasiswa("Yuna", "8167216716", "Ilmu Komputer", "MIPA")
mahasiswa2 = Mahasiswa("Jeno", "1789276401", "Teknik Elektro", "Teknik")
mahasiswa3 = Mahasiswa("Nancy", "156289176", "Akuntansi", "Ekonomi")
mahasiswa4 = Mahasiswa("Felix", "6271892643", "Pendidikan Dokter", "Kedokteran")

mahasiswa = [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4]
print("\nList Mahasiswa")
for mhs in mahasiswa :
    teks = '{} adalah mahasiswa {} dengan nim {} fakultas {}'. format(mhs.nama, mhs.prodi, mhs.nim, mhs.fakultas)
    print(teks)
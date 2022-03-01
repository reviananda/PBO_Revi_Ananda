class Mahasiswa:
    def __init__(self,nama,nim,prodi,thn_masuk):
    self.nama = nama
    self.nim = nim
    self.prodi = prodi
    self.thn_masuk = thn_masuk

m1 = Mahasiswa("Udin","10120371","Sistem Informasi",2020)
teks = "{} adalah mahasiswa {} angkatan {} dengan nim {}".format(m1.nama,m1.prodi.m1,thn_masuk,m1.nim)
print(teks)
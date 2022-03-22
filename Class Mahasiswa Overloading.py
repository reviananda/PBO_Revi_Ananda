#Implementasi Overloading Class Mahasiswa

class mahasiswa:
  def __init__(self, nama, nim):
    self.nama = nama
    self.nim = nim

  def tampilMhs(self):
    print(f"Nama\t\t: {self.nama} \nNIM \t\t: {self.nim}")

    # Method Overloading

  def hitungSks(self, jmlSks = None, sks = None):
    if jmlSks != None and sks != None:
        totalSks = jmlSks + sks
        print(f"Total SKS\t: {totalSks}")
    else:
      totalSks = jmlSks
      print(f"Total SKS\t: {totalSks}")

    if totalSks>=100:
      print("Diperbolehkan Mengambil Skripsi")
    else:
      print("Tidak Diperbolehkan Mengambil Skripsi")
#
mahasiswa1 = mahasiswa("Eren", 123180015)
mahasiswa2 = mahasiswa("Mikasa", 123190007)

mahasiswa1.tampilMhs()
mahasiswa1.hitungSks(80, 34)

mahasiswa2.tampilMhs()
mahasiswa2.hitungSks(83)
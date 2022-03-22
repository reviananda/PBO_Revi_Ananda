class pegawai:
  jumlah = 0

  def __init__(self, nama, gaji):
    self.nama = nama
    self.gaji = gaji
    pegawai.jumlah += 1

  def tampilJumlah(self):
    print(f"Total Pegawai : {pegawai.jumlah}")

  def tampilPegawai(self):
    print(f"Nama Pegawai : {self.nama}")

  def tunjangan(self, istri = None, anak = None):
    if anak != None and istri != None:
      total = anak + istri
      print(f"Tunjangan anak + istri = {total}")
    else:
      total = istri
      print(f"Tunjangan istri = {total}")

pegawai1 = pegawai("Eren", 2000)
pegawai2 = pegawai("Luffy", 6000)

pegawai1.tampilPegawai()
pegawai2.tampilPegawai()

pegawai1.tunjangan(2500, 2000)
pegawai2.tunjangan(2500)

print("Total Gaji = %d" % pegawai.jumlah)
rataGaji = (pegawai1.gaji + pegawai2.gaji) / pegawai.jumlah
print(f"Rata-Rata Gaji = {str(rataGaji)}")
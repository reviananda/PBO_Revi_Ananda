#private
class Buku :
    def __init__(self, judul, pengarang, tahun_terbit, penerbit) :
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.penerbit = penerbit

buku1 = Buku("Arti Kehilangan", "Ade Rahayu", 2015, "Euthenia")
buku2 = Buku("Negeri 5 Menara", "Ahmad Fuadi", 2009, "Gramedia")
buku3 = Buku("Laskar Pelangi", "Andrea Hirata", 2005, "Bentang Pustaka")
buku4 = Buku("Sepatu Dahlan", "Khrisna Pabichara", 2012, "Noura Books")

bukus = [buku1, buku2, buku3, buku4]
print("List Buku")
for buku in bukus :
    teks = 'Buku {} karangan {} pertama kali diterbitkan tahun {} yang diterbitkan oleh {}'.format(buku.judul, buku.pengarang, buku.tahun_terbit, buku.penerbit)
    print(teks) 
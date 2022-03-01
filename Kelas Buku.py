class Buku :
    def __init__(self, judul, pengarang, tahun_terbit) :
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

buku1 = Buku("Arti Kehilangan", "Ade Rahayu", 2015)
buku2 = Buku("Negeri 5 Menara", "Ahmad Fuadi", 2009)
buku3 = Buku("Laskar Pelangi", "Andrea Hirata", 2005)
buku4 = Buku("Sepatu Dahlan", "Khrisna Pabichara", 2012)

bukus = [buku1, buku2, buku3, buku4]
print("List Buku")
for buku in bukus :
    teks = 'Buku {} karangan {} pertama kali diterbitkan tahun {}'.format(buku.judul, buku.pengarang, buku.tahun_terbit)
    print(teks) 
print("\n")
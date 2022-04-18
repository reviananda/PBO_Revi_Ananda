class Perpustakaan :
    def __init__(self, kode, judul, subjek, lokasi, info) :
        self.kode = kode
        self.judul = judul      
        self.subjek = subjek
        self.lokasi = lokasi
        self.info = info

class Buku(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, isbn, pengarang, jmlhal, ukuran):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.isbn = isbn
        self.pengarang = pengarang
        self.jmlhal = jmlhal        
        self.ukuran = ukuran         

class Majalah(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, volume, issue):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.volume = volume
        self.issue = issue

class DVD(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, aktor, genre):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.aktor = aktor
        self.genre = genre      

buku = Buku("123", "Pemrograman Python", "Buku Cetak", "Rak 1", "Dipinjam", "945-884-98-05", "Yogi Syarif", 20, "25x15")
majalah = Majalah("234", "Dunia Komputer", "Majalah Cetak", "Rak 2", "Ada", "VII", "Komputer")
dvd = DVD("312", "Shingeki no kyojin", "softcopy", "Rak 3", "Ada", "Mikasa", "Anime")
objects = [buku, majalah, dvd]  

for object in objects : 
    print(f"Judul : {object.judul}")
    print(f"Kategori : {object.subjek}")
    print(f"Lokasi : {object.lokasi}")  
    print(f"Status : {object.info}\n")
#private
class Menu :
    def __init__(self, nama, deskripsi, harga, jumlahPorsi) :
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
        self.jumlahPorsi = jumlahPorsi

makanan1 = Menu("Sate & Gulai", "Nasi dengan 4 tusuk sate kambing dan gulai kambing dengan tambahan potongan bawang merah, daun jeruk, dan jeruk nipis", 25000, 30)
makanan2 = Menu("Gudeg", "Nasi dengan lauk ayam kampung, telur, kuah santan kental, dan sambal krecek", 20000, 40)
makanan3 = Menu("Soto Banjar", "Nasi dengan kuah soto khas Banjar dengan potongan daging ayam yang dicampur bumbu rempah-rempah", 15000, 45)
makanan4 = Menu("Sup Konro", "Nasi dengan sup iga sapi yang disajikan dengan kuah berwarna coklat", 17000, 35)

minuman1 = Menu("Jus Jambu", "Jus jambu merah tanpa gula", 8500, 40)
minuman2 = Menu("Jus Alpukat", "Jus alpukat dengan gula merah", 15000, 40)
minuman3 = Menu("Jus Alpukat Ektra Milk", "Jus alpukat dengan campuran susu cokelat dan tapuran kepingan choco", 15000, 40)
minuman4 = Menu("Red & Smooth", "Smoothie pisang susu dengan strawberry", 17500, 40)

makanan = [makanan1, makanan2, makanan3, makanan4]
minuman = [minuman1, minuman2, minuman3, minuman4]

print("Daftar Menu Makanan")
for makan in makanan :
    teks = '{} harga Rp {}, {}, sedia {} porsi'. format(makan.nama, makan.harga, makan.deskripsi, makan.jumlahPorsi)
    print(teks)
print("\nDaftar Menu Minuman")
for minum in minuman :
    teks = '{} harga Rp {}, {}, sedia {} porsi'. format(minum.nama, minum.harga, minum.deskripsi, minum.jumlahPorsi)
    print(teks)
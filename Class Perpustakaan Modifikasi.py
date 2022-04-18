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
           

    def Tampil(self) :
        print(f"Judul : {self.judul} <{self.kode}>")
        print(f"Pengarang : {self.pengarang}")
        print(f"Jumlah Halaman : {self.jmlhal}")
        print(f"Kategori : {self.subjek}\n")

class Majalah(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, volume, issue):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.volume = volume
        self.issue = issue

    def Tampil(self) :  #Overriding
        print(f"Judul : {self.judul} <{self.kode}>")
        print(f"Volume : {self.volume}")
        print(f"Issue : {self.issue}")
        print(f"Kategori : {self.subjek}\n")

class DVD(Perpustakaan) :
    def __init__(self, kode, judul, subjek, lokasi, info, aktor, genre):
        super().__init__(kode, judul, subjek, lokasi, info)
        self.aktor = aktor
        self.genre = genre      

    def Tampil(self) :  #Overriding
        print(f"Judul : {self.judul} <{self.kode}>")
        print(f"Aktor : {self.aktor}")
        print(f"Genre : {self.genre}")
        print(f"Kategori : {self.subjek}\n") 

#Objek Buku
buku1 = Buku("1001", "UML", "Buku Cetak", "Rak 1", "Dipinjam", "978-602-623-277-9", "Munawar", 268, "21x26")
buku2 = Buku("1002","Ensiklopedia Keragaman Budaya", "Buku Referensi", "Rak 1", "Ada", "978-979-053-118-5", "Nurul Akhmad", 132, "25x20")
buku3 = Buku("1003","Kamus Indonesia-Korea", "Buku Referensi", "Rak 1", "Ada", "978-602-667-313-8", "Tri Istiyani", 300, "15x20")
buku4 = Buku("1004","Atlas Dunia", "Buku Referensi", "Rak 1", "Dipinjam", "978-602-434-291-3", "National Geographic Kids", 208, "24x30,5")

#Objek Majalah
majalah1 = Majalah("1111", "Vogue", "Majalah Cetak", "Rak 2", "Ada", "202", "Gaya Hidup")
majalah2 = Majalah("1112", "Bazaar", "Majalah Cetak", "Rak 2", "Dipinjam", "18", "Fashion")
majalah3 = Majalah("1113", "Elle", "Majalah Cetak", "Rak 2", "Ada", "16", "Mode & Gaya Hidup")
majalah4 = Majalah("1114", "Muslimah", "Majalah Cetak", "Rak 2", "Ada", "12", "Kecantikan")  
majalah5 = Majalah("1115", "Infokomputer", "Majalah Cetak", "Rak 2", "Dipinjam", "III", "Komputer")

#Objek DVD
dvd1 = DVD("1221", "Only You", "softcopy", "Rak 3", "Ada", "Han Yi Joon", "DraKor")
dvd2 = DVD("1222", "Medical Brothers", "softcopy", "Rak 3", "Ada", "Kim Su Hyung", "DraKor")
dvd3 = DVD("1223", "My Sassy Girl", "softcopy", "Rak 3", "Ada", "Cha Tae Hyun", "DraKor")   
dvd4 = DVD("1224", "Like Land and Sky", "softcopy", "Rak 3", "Ada", "Jung Mu Young", "DraKor")

while True :
    print("=======================\n    SEARCH ITEM \n=======================")
    print("1. BUKU ")  
    print("2. MAJALAH")
    print("3. DVD")
    print("0. selesai")
    menu = input("Pilihan Menu : ") 

    if menu == '1' :
        print("\nMENU BUKU\n===============\n1. Tampil Buku")
        print("2. Cari Buku")   
        pilihan = input("Pilihan : ")  
        buku = [buku1, buku2, buku3, buku4]

        if pilihan == '1' :
            print("\n==============================================")
            for buku in buku :
                buku.Tampil()

        elif pilihan == '2' :
            kode = input("Masukan Kode Buku\t: ")
            for x in buku :
                if kode == x.kode :
                    print("\n==============================================")
                    print(f"Judul : {x.judul}")
                    print(f"Letak : {x.lokasi}")    
                    print(f"Status : {x.info}\n")
                    print("==============================================")

    elif menu == '2' :
        print("\nMENU MAJALAH\n===============\n1. Tampil Data Majalah")
        print("2. Cari Majalah")        
        pilihan = input("Pilihan : ") 
        majalah = [majalah1, majalah2, majalah3, majalah4, majalah5] 

        if pilihan == '1' :
            print("\n==============================================")
            for majalah in majalah :
                majalah.Tampil()

        elif pilihan == '2' :
            kode = input("Masukan Kode Majalah\t: ")
            for x in majalah :
                if kode == x.kode :
                    print("\n==============================================")
                    print(f"Judul : {x.judul}")
                    print(f"Letak : {x.lokasi}")
                    print(f"Status : {x.info}\n")
                    print("==============================================")

    elif menu == '3' :
        print("\nMENU DVD\n===============\n1. Tampil Data DVD")
        print("2. Cari DVD")
        pilihan = input("Pilihan : ")  
        dvd = [dvd1, dvd2, dvd3, dvd4]  

        if pilihan == '1' :
            print("\n==============================================")
            for dvd in dvd :
                dvd.Tampil()

        elif pilihan == '2' :
            kode = input("Masukan Kode DVD\t: ")
            for x in dvd :
                if kode == x.kode :
                    print("\n==============================================")
                    print(f"Judul : {x.judul}")
                    print(f"Letak : {x.lokasi}")
                    print(f"Status : {x.info}\n")
                    print("==============================================")

    elif menu == '0' :
        print("TERIMA KASIH :)\n")
        break

    else : 
        print("\nPilihan Tidak Ada Menu\n")
    input("\nEnter Untuk Melanjutkan......")
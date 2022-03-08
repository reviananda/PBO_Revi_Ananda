#Private dan Public
class Pegawai :
    __nama = ""
    __alamat = ""
    __gaji = 0

    def __init__(self, nama, alamat) :
        self.__nama = nama
        self.__alamat = alamat

    def __hitungGaji(self) :
        upahLembur = 20000
        gajiPokok = 2000000
        jumLembur = int(input("Total Jam Lembur : "))
        self.__gaji = (upahLembur * gajiPokok) * jumLembur

    def tampilDetail(self) :
        print("\n--Menghitung dan Menampilkan detail Gaji Pegawai--")
        print(f"Nama : {self.__nama}")
        print(f"Alamat : {self.__alamat}")
        self.__hitungGaji()
        print(f"Total Gaji : {self.__gaji}")

pegawai1 = Pegawai("Mikasa Ackerman", "Wall Rose")
pegawai1.tampilDetail()

pegawai2 = Pegawai("Saya Kisaragi", "Prefektur Nagano")
pegawai2.tampilDetail()
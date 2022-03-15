def rupiah(uang):
    x = str(uang)
    if len(x) <= 3:
        return "Rp" + x
    else :
        a = x[:-3]
        b = x[-3:]
        return rupiah(a) + '.' + b

class ComputerPart:
    def __init__(self, pabrikan, nama, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

class Processor(ComputerPart):
    def __init__(self, pabrikan, nama, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

    def Tampil(self):
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"harga : {rupiah(self.harga)}")

class RandomAccessMemory(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga
        self.kapasitas = kapasitas

    def Tampil(self):
            print(f"{self.nama} produk dari {self.pabrikan}")
            print(f"Kapasitas : {self.kapasitas}")
            print(f"Harga : {rupiah(self.harga)}")

class HardDiskSATA(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga
        self.kapasitas = kapasitas
        self.rpm = rpm

    def Tampil(self):
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Kapasitas : {self.kapasitas}")
        print(f"RPM : {self.rpm}")
        print(f"Harga : {rupiah(self.harga)}")

p = Processor("AMD", "Ryzen 7 3700X", 4439000)
ram = RandomAccessMemory("V-Gen", "DDR4 XLR8 3800MHz", 650000, "8GB")
hdd = HardDiskSATA("Toshiba", "PC P300 HardDisk Internal 1 TB/7200 rpm", 619000, "1 TB", "7200 rpm")

parts = [p, ram, hdd]
print("\n\t\t\t\tHIERARCHIAL COMPUTER PART")
print("=====================================================================================================")
for part in parts :
    part.Tampil()
    print("")
print("=====================================================================================================")
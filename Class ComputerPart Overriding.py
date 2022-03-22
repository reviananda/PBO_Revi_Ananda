class ComputerPart:
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama    
        self.harga = harga

class Processor(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, core, speed) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.harga = harga
        self.core = core
        self.speed = speed
        
    def Tampil(self) :  
        print("\nTampil dari sub class Processor")
        print(f"{self.pabrikan} membuat seri produk yaitu {self.nama}")
        print("Dengan Spesifikasi Berikut:")
        print(f"Jumlah Core = {self.core}")
        print(f"Boost Clock: {self.speed}")
        print(f"Harga : {harga_brg(self.harga)}")

class RandomAccessMemory(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, kapasitas) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.harga = harga
        self.kapasitas = kapasitas

    def Tampil(self) :  
        print("Tampil dari sub class RandomAccessMemory")
        print(f"{self.pabrikan} membuat seri produk yaitu {self.nama}")
        print("Dengan Spesifikasi Berikut:")
        print(f"Kapasitas : {self.kapasitas}")
        print(f"Harga : {harga_brg(self.harga)}")

class HardDiskSATA(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.harga = harga
        self.kapasitas = kapasitas
        self.rpm = rpm
    
    def Tampil(self) :
        print("Tampil dari sub class HardDiskSATA")
        print(f"{self.pabrikan} membuat seri produk yaitu {self.nama}")
        print("Dengan Spesifikasi Berikut:")
        print(f"Kapasitas : {self.kapasitas}")
        print(f"RPM : {self.rpm}")
        print(f"Harga : {harga_brg(self.harga)}")
        
class GraphicsCard(ComputerPart) :
    def __init__(self, pabrikan, nama, harga, kapasitas, MHz) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.harga = harga
        self.kapasitas = kapasitas
        self.MHz = MHz
    
    def Tampil(self) :
        print("Tampil dari sub class GraphicsCard")
        print(f"{self.pabrikan} membuat seri produk yaitu {self.nama}")
        print("Dengan Spesifikasi Berikut:")
        print(f"Kapasitas : {self.kapasitas}")
        print(f"MHz : {self.MHz}")
        print(f"Harga : {harga_brg(self.harga)}")

def harga_brg(harga) :
    x = str(harga)
    if len(x) <= 3 :
        return "Rp." + x
    else :  
        a = x[:-3]
        b = x[-3:]
        return harga_brg(a) + '.' + b
        

proci = Processor('AMD', 'Ryzen 7 3700X', 4439000, 8, '4.4GHz')
ram = RandomAccessMemory('V-Gen', 'DDR4 XLR8 3800MHz', 650000, '8GB')
hdd = HardDiskSATA('Toshiba', 'PC P300 HardDisk Internal 1 TB/7200 rpm', 619000, '1TB', 7200)
vga = GraphicsCard('NVIDIA', 'Gigabyte NVIDIA Geforce GT 710', 795000, 2, 954)

parts = [proci, ram, hdd, vga]   
print("\n\t\t\t\tPart Komputer Overriding")
print("---------------------------------------------------------------------------------\n")
for part in parts :
    part.Tampil()
    print("")   
print("---------------------------------------------------------------------------------")
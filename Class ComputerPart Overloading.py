def rupiah(uang) :
    x = str(uang)
    if len(x) <= 3 :
        return "Rp." + x
    else :  
        a = x[:-3]
        b = x[-3:]
        return rupiah(a) + '.' + b
    
class ComputerPart:
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama    
        self.harga = harga

class Processor(ComputerPart) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama 
        self.harga = harga
            
    def Tampil(self) :  
        print("\nTampil dari sub class Processor")
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Harga\t\t: {rupiah(self.harga)}")

class RandomAccessMemory(ComputerPart) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama    
        self.harga = harga

    def Tampil(self, kapasitas) :  
        print("\nTampil dari sub class RandomAccessMemory")
        print(f"{self.nama} produk dari {self.pabrikan}\nKapasitas\t: {kapasitas}")
        print(f"Harga\t\t: {rupiah(self.harga)}")

class HardDiskSATA(ComputerPart) :
    def __init__(self, pabrikan, nama, harga) :
        self.pabrikan = pabrikan
        self.nama = nama    
        self.harga = harga

    
    def Tampil(self, kapasitas, rpm) :  
        print("\nTampil dari sub class HardDiskSATA")
        print(f"{self.nama} produk dari {self.pabrikan}\nKapasitas\t: {kapasitas}")
        print(f"RPM\t\t: {rpm}\nHarga\t\t: {rupiah(self.harga)}")


p = Processor('AMD', 'Ryzen 7 3700X', 4439000)
ram = RandomAccessMemory('V-Gen', 'DDR4 XLR8 3800MHz', 650000)
hdd = HardDiskSATA('Toshiba', 'PC P300 HardDisk Internal 1 TB/7200 rpm', 619000)

print("\n\t\t\tOVERLOADING COMPUTER PART")
print("=================================================================================")
p.Tampil()
ram.Tampil("8GB")
hdd.Tampil("1TB", 7200)
print("=================================================================================\n")
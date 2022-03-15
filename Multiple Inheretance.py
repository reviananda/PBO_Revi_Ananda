def rupiah(uang):
    x = str(uang)
    if len(x) <= 3:
        return "Rp" + x
    else :
        a = x[:-3]
        b = x[-3:]
        return rupiah(a) + '.' + b

class ComputerPart1:
    def __init__(self, pabrikan, nama):
        self.pabrikan = pabrikan
        self.nama = nama

class ComputerPart2:
    def __init__(self, harga):
        self.harga = harga

class Processor(ComputerPart1, ComputerPart2):
    def __init__(self, pabrikan, nama, harga):
      ComputerPart1.__init__(self, pabrikan, nama)
      ComputerPart2.__init__(self, harga)

    def Tampil(self):
      print(f"{self.nama} produk dari {self.pabrikan}")
      print(f"Harga : {rupiah(self.harga)}")

class RandomAccessMemory(ComputerPart1, ComputerPart2):
    def __init__(self, pabrikan, nama, harga):
      ComputerPart1.__init__(self, pabrikan, nama)
      ComputerPart2.__init__(self, harga)

    def Tampil(self):
      print(f"{self.nama} produk dari {self.pabrikan}")
      print(f"Harga : {rupiah(self.harga)}")

class HardDiskSATA(ComputerPart1, ComputerPart2):
    def __init__(self, pabrikan, nama, harga):
      ComputerPart1.__init__(self, pabrikan, nama)
      ComputerPart2.__init__(self, harga)

    def Tampil(self):
      print(f"{self.nama} produk dari {self.pabrikan}")
      print(f"Harga : {rupiah(self.harga)}")

p = Processor("AMD", "Ryzen 7 3700X", 4439000)
ram = RandomAccessMemory("V-Gen", "DDR4 XLR8 3800MHz", 650000)
hdd = HardDiskSATA("Toshiba", "PC P300 HardDisk Internal 1 TB/7200 rpm", 619000)

parts = [p, ram, hdd]
print("\n\t\t\t\t\tMULTIPLE COMPUTER PART")
print("=========================================================================================================")
for part in parts :
    part.Tampil()
    print("")
print("=========================================================================================================\n")
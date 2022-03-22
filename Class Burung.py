class burung:
  def intro(self):
    print("Di dunia ini ada beberapa type berbeda dari spesies burung")

  def terbang(self):
    print("Hampir semua burung dapat terbang, namun ada beberapa yang tidak bisa terbang")

class elang(burung):
  def terbang(self):
    print("Elang dapat terbang")

class burungUnta(burung):
  def terbang(self):
    print("Burung unta tidak dapat terbang")

obj_burung = burung()
obj_elang = elang()
obj_burung_unta = burungUnta()

obj_burung.intro()
obj_burung.terbang()

obj_elang.intro()
obj_elang.terbang()

obj_burung_unta.intro()
obj_burung_unta.terbang()
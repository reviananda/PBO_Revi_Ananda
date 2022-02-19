#Membuat list
buah = ('semangka', 'apel', 'melon', 'pepaya',)
print(buah)
#Mengubah list menjadi set
buah = set(['semangka', 'apel', 'rambutan', 'melon', 'pepaya'])
print(buah)
#Membuat Set dengan berbagai tipe data
set_buah = {'melon', 'pepaya', 50, True, ('A', 'B')}
print(set_buah)

print("")
himpunan_huruf = {'a', 'b', 'c'}
print(himpunan_huruf)
#Fungsi Add
himpunan_huruf.add('d')
himpunan_huruf.add('e')
print(himpunan_huruf)
#Fungsi Update
himpunan_huruf.update({ 'f', 'g' })
print(himpunan_huruf)
print("")
himpunan = {'Karina', 'Giselle', 100, ('a', 'b'), False, True}
print(himpunan)
#Fungsi Remove
himpunan.remove(100)
print(himpunan)
#Fungsi Discard
himpunan.discard(('a', 'b'))
print(himpunan)
#Fungsi Pop
nilaiYangDihapus = himpunan.pop()
print('nilaiYangDihapus =', nilaiYangDihapus)
print(himpunan)
#Fungsi Clear
himpunan.clear()
print(himpunan)

boygrup = {
  'Felix', 'Jay', 'Jake', 'Mark'
}
girlgrup = {
  'Lisa', 'Yeri', 'Wendy', 'Irene'
}
print("")
#Fungsi Union (Gabungan)
print(boygrup.union(girlgrup))
#Fungsi Intersection (Irisan)
print(boygrup.intersection(girlgrup))
#Fungsi Difference (Selisih)
print('\nanggota boygrup yang bukan anggota girlgrup')
print(boygrup - girlgrup)
print(boygrup.difference(girlgrup))

print('\ndibalik, anggota girlgrup yang bukan anggota boygrup:')
print(girlgrup - boygrup)
print(girlgrup.difference(boygrup))
#Symmetric Difference
print('\nanggota yang hanya ikut satu grup saja:')
print(girlgrup.symmetric_difference(girlgrup))
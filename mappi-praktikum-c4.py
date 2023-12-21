import os
os.system('clear')

nim = ['2','3','1','0','3','1','0','8','9']
print(nim)

print('item indeks 0 (pertama)',nim[0])
print('item indeks 1 (kedua)',nim[1])

print(f'item indeks 0 (pertama){nim[0]}')
print(f'item indeks 1 (kedua) {nim[1]}')
print(f'item indeks terakhir {nim[len(nim)-1]}')
print(f'item indeks terakhir  {nim[-1]}')
print(f'item indeks (pertama) {nim[len(nim)]}')

#latihan list
data = ['Andi Mappinawan',2023,'Aktif']
nilai = [90,89,93,97]

print(f'Nama:  +,  data[0]')
print(f'angkatan:, data[1]')
print(f'status:, + data[2]')
print()
#>> Von Neumann status Kuliah: Aktif
#>> Data terbesar nilai adalah: 97
#>> Data terkecil nilai adalah: 89
#>> Rata-rata nilai adalah: 92.25

#LATIHAN NESTED LIST
data = [('Thomas',2023,'Aktif'),

(90,89,93,97),
(20,22),
('S1-Reguler','Ganjil')]

matkul = ['Matkul1',]


print(data[0][0])
print(data[-1][0])
print(data[2][0:])

# Nama mahasiswa: Von Neumann
print
# Inisial Von Neumann: V N
# NIM Von Neumann: 231031089
# Program pendidikan Andi Mappinawan: S1-Reguler Sistem Inkformasi B
# Angkatan Von Neumann: ganjil-2023
# Total sks Non Neumann: 11
# jumlah sks von Neumann: 5
# Nilai terendah Von Neumann: 99
# Nilai terendah Von Neumann: 76
# Rata-Rata nilai Von Neumann: 92.25



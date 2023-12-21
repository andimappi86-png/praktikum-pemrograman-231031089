def nilai_minimal(list):
 #Mencari nilai terkecil
 nilai_terkecil=list[0]
 # print(f'{list} -> {nilai_terbesar}')
 if len(list)>1:
 #proses rekursif
 next_nilai_minimal=nilai_minimal(list[1:])
 if next_nilai_terkecil<nilai_terkecil: 
 nilai_minimal=next_nilai_terkecil
 # print(f'{list} -> {nilai_terbesar}')
 return nilai_terkecil
#Program Utama mulai di sini
a=[3,20,100,-35,50.5]
print(a)
print('Nilai Terkecil =',nilai_minimal(a))

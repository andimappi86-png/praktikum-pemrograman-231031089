import os

def judul():
    os.system('cls')
    #judul
    print('PROGRAM MENGHITUNG VOLUME DAN LUAS PERMUKAAN')
    print('BANGUN RUANG BALOK')
    print()

def inputan():
    p = float (input('Masukkan panjang: '))
    l = float (input('Masukkan lebar: '))
    t = float (input('Masukkan tinggi: '))
    return p,l,t

def perhitungan(p,l,t):
    vol = p * l * t
    luas = 2 * (p*l + p*t + l*t)
    luas_non_tutup = luas - p*l
    return vol,luas,luas_non_tutup

def tampilkan(jenis,nilai):
    print(f'nilai dari {jenis} adalah : {nilai}')


def pilihan():
    pilih = input('Apakah lanjutkan? [y/n]')
    if pilih == 'y':
        a = True
    else:
        a = False
        print('sampai jumpa lagi.')
def main():

    judul()
    #inputan
    p,l,t = inputan()

    #perhitungan
    vol,luas,luas_non_tutup = perhitungan(p,l,t)

    #tampilan
    tampilkan('volume',vol)
    tampilkan('luas permukaan',luas)
    tampilkan('luas permukaan tanpa tutup',luas_non_tutup)

    a = pilihan()                 #pilihan

a = True
while a:
    main()
nama = ' andi mappinawan'
nim  = '231031089'
meet = 'Praktikum 3 (String)'
prodi= 'Sistem Informasi C'
email= 'andimappi86@gmail.com'
ttl = '8-6-2005'
alamat = 'BTN Grand Sulawesi'
asal = 'Barru'
hobi = 'Olahraga'
tinggi = 160

sp = 40
print('-'*sp)
print(nama.upper().center(sp))
print(nim.center(sp))
print('\n'*2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.lower().rjust(sp))
print('-'*sp)

print(f'''\tHalo, nama saya {nama} dengan NIM {nim} dari prodi {prodi}, ini adalah file {meet}. Terima kasih.\n''')

print(f'''Biodata saya,
Nama\t: {nama.upper()}
NIM\t: {nim}
Prodi\t: {prodi}
TTL\t: {ttl}
Alamat\t: {alamat}
Asal\t: {asal}
hobi\t: {hobi}
tinggi\t: {tinggi}cm
      ''')







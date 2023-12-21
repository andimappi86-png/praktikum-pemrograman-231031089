print ("NAMA : ANDI MAPPINAWAN")
print ("NIM : 231031089")
print ()
print ("PRODI : SISTEM INFORMASI")
print ("TANGGAL LAHIR : 08-JUNI-2005")

#operasi aritmatika

a=72
print ('Nilai a =',a)
a=72
a+=1
print ('nilai a-=1 akan menjadi',a)
a=72
a+=72
print ('nilai a*=2 akan menjadi',a)
a=72
a/=72
print ('nilai a/=2 akan menjadi',a)
a=72
a%=72
print ('nilai a%=2 akan menjadi',a)
a=72
a//=72
print ('nilai a//=2 akan menjadi',a)
a=72
a**=72
print ('nilai a**=2 akan menjadi',a)
#OR
b=True
print ('Nilai b =',b)
b |= False
print ('Nilai b|= False akan menjadi ',b )
b = False
print ('Nilai b =',b )
b |= False
print ('Nilai b|= False akan menjadi ',b )
# AND
b = True
print ('Nilai b =',b )
b &= False
print ('Nilai b&= False akan menjadi ',b )
b = False
print ('Nilai b =',b )
b &= False
print ('Nilai b&= False akan menjadi ',b)
 # XOR
b = True
print ('Nilai b =',b)
b ^= False
print ('Nilai b^= False akan menjadi ',b )
b = False
print ('Nilai b =',b)
b ^= False
print ('Nilai b^= False akan menjadi ',b )
# Shifting

c =0b0100
print ('Nilai c =',format (c , '04b') )
c >>=1
print ('Nilai c > >=1 akan menjadi ',format (c , '04b') )
c =0b0100
c <<=1
print ('Nilai c < <=1 akan menjadi ',format (c , '04b') )

#operator komparasi/prbandingan

a =8 # isi dengan ujung NIM
b =13 # Ubah dengan hasil jumlah ujung NIM dengan 5
print (' ================== Besar dari 13 ')
hasil = a >13
print (a ,'> 13 adalah ', hasil )
hasil = b >13
print (b ,'> 13 adalah ', hasil )

print (' ================== kecil dari 13 ')
hasil = a <13
print (a ,'< 13 adalah ', hasil )
hasil = b <13
print (b ,'< 13 adalah ', hasil )

print (' ================== Besar atau sama dari 13 ')
hasil = a >=13
print (a ,' >= 13 adalah ', hasil )
hasil = b >=13
print (b ,' >= 13 adalah ', hasil )

print (' ================== Besar atau sama dari 13 ')
hasil = a <=13
print (a ,' <= 13 adalah ', hasil )
hasil = b <=13
print (b ,' <= 13 adalah ', hasil )

print (' ================== Sama dengan 13 ')
hasil = a ==13
print (a ,'== 13 adalah ', hasil )
hasil = b ==13
print (b ,'== 13 adalah ', hasil )

print (' ================== Tidak sama dengan 13 ')
hasil = a !=13
print (a ,'!= 13 adalah ', hasil )
hasil = b !=13
print (b ,'!= 13 adalah ', hasil )

#operator logika

print (' ============= NOT ============= ')
a = True
c = not a
print ('a adalah',a )
print (' ------c = not a- - - -- - - NOT ')
print ('c adalah ',c )

print (' ============= OR ============= ')
a = True
b = True
c = a or b
print (a ,'OR ',b ,'menjadi ',c )

a = True
b = False
c = a or b
print (a ,'OR ',b ,'menjadi ',c )

a = False
b = True
c = a or b
print (a ,'OR ',b ,'menjadi ',c )

a = False
b = False
c = a or b
print (a ,'OR ',b ,'menjadi ',c )

print (' ============= AND ============= ')
a = True
b = True
c = a and b
print (a ,'AND ',b ,'menjadi ',c )

a = True
b = False
c = a and b
print (a ,'AND ',b ,'menjadi ',c )

a = False
b = True
c = a and b
print (a ,'AND ',b ,'menjadi ',c )

a = False
b = False
c = a and b
print (a ,'AND ',b ,'menjadi ',c )

print (' ============= XOR ============= ')
a = True
b = True
c = a ^ b
print (a ,'^',b ,'menjadi ',c )

a = True
b = False
c = a ^ b
print (a,'^',b ,'menjadi',c)

a = False
b = True
c = a ^ b
print (a ,'^',b ,'menjadi ',c )

a = False
b = False
c = a ^ b
print (a ,'^',b ,'menjadi ',c )
# TUGAS
# Buat kode untuk masing masing operator berikut
print (' ============= NAND ============= ')
print (' ============= NOR ============== ')
print (' ============= NXOR ============= ')

#operator identitas

print (' ============== IS ')
a =5
b =5
print ('Nilai a =',a ,'Identitas =',hex (id( a ) ) )
print ('Nilai b =',b ,'Identitas =',hex (id( b ) ) )
hasil = a is b
print ('a is b = ', hasil )

a =5
b =6
print ('Nilai a =',a ,'Identitas =',hex (id( a ) ) )
print ('Nilai b =',b ,'Identitas =',hex (id( b ) ) )
hasil = a is b
print ('a is b = ', hasil )

print (' ============== IS NOT ')
a =5
b =5
print ('Nilai a =',a ,'Identitas =',hex (id( a ) ) )
print ('Nilai b =',b ,'Identitas =',hex (id( b ) ) )
hasil = a is not b
print ('a is not b = ', hasil )
a =5
b =6
print ('Nilai a =',a ,'Identitas =',hex (id( a ) ) )
print ('Nilai b =',b ,'Identitas =',hex (id( b ) ) )
hasil = a is not b
print ('a is not b = ', hasil )

#operator membership

print (' ======================= IN ')
nama_lengkap = ' Bacharuddin Jusuf Habibie '
test = 'a'
cek = test in nama_lengkap
print ( test +' terdapat di '+ nama_lengkap +' adalah '+ str( cek ) )

test = 'rud '
cek = test in nama_lengkap
print ( test +' terdapat di '+ nama_lengkap +' adalah'+ str( cek ) )

test = 'bac '
cek = test in nama_lengkap
print ( test +' terdapat di '+ nama_lengkap +' adalah'+ str( cek ) )

print (' ======================= NOT IN ')
nama_lengkap = ' Bacharuddin Jusuf Habibie '
test = 'a'
cek = test not in nama_lengkap
print ( test +' tidak terdapat di '+ nama_lengkap +' adalah'+str ( cek ) )

test = 'rud '
cek = test not in nama_lengkap
print ( test+' tidak terdapat di '+nama_lengkap+' adalah '+str ( cek ))

# TUGAS
# Dengan cara yang sama buat operator in dan not in , ubah nama lengkap menjadi nama masing - masing dengan uji test
test1 = ab # pilih dua huruf berurut yang ada pada nama anda
test2 = ba # balik dua huruf tersebut
test3 = 'a'
test4 = 'i'
test5 = 'u'
test6 = 'e'
test7 = 'o'

#Operator Bitwise

a =22 # ubah menjadi tanggal lahir anda
a +=60
b =99 # ubah menjadi bulan lahir anda
b += 90
print (' ============================= OR ')
print ('Nilai ',a ,'dalam biner = ', format (a ,'08b') )
print ('Nilai ',b ,'dalam biner = ', format (b ,'08b') )
print (' - - - - - - - - - - - - - - - - - - - - - - - - - - - -(|)')
hasil = a | b
print ('Nilai ',a ,'|',b ,'dalam biner = ', format ( hasil ,'08b') )

print (' ============================= AND ')
print ('Nilai ',a ,'dalam biner = ', format (a ,'08b') )
print ('Nilai ',b ,'dalam biner = ', format (b ,'08b') )
print (' - - - - - - - - - - - - - - - - - - - - - - - - - - - -(&)')
hasil = a & b
print ('Nilai ',a ,'&',b ,'dalam biner = ', format ( hasil ,'08b') )

print (' ============================= XOR ')
print ('Nilai ',a ,'dalam biner = ', format (a ,'08b') )
print ('Nilai ',b ,'dalam biner = ', format (b ,'08b') )
print (' - - - - - - - - - - - - - - - - - - - - - - - - - - - -(^)')
hasil = a ^ b
print ('Nilai ',a ,'^',b ,'dalam biner = ', format ( hasil ,'08b') )

print (' ============================= NOT ')
print ('Nilai ',a ,'dalam biner = ', format (a ,'08b') )
print (' - - - - - - - - - - - - - - - - - - - - - - - -(~a)')
hasil = ~a
print ('Nilai ~',a ,'dalam biner = ', format ( hasil ,'08b') )
       
print ('Nilai ',b ,'dalam biner = ', format (b ,'08b') )
print (' - - - - - - - - - - - - - - - - - - - - - - - -(b)')
hasil = ~b
print ('Nilai ~',b ,'dalam biner = ', format ( hasil ,'08b') )
       
print ('============================= > > ')
print ('Nilai ',a ,'dalam biner = ', format (a ,'08b') )
print (' - - - - - - - - - - - - - - - - - - - - - - - - - -( > >2)')
hasil = a >> 2
print ('Nilai ',a ,' > >2 dalam biner = ', format ( hasil ,'08b') )

print ('Nilai ',b ,'dalam biner = ', format (b ,'08b') )
print (' - - - - - - - - - - - - - - - - - - - - - - - - - -( > >2)')
hasil = b >> 2
print ('Nilai ',b ,' > >2 dalam biner = ', format ( hasil ,'08b') )

print ('============================= < < ')
print ('Nilai ',a ,'dalam biner = ', format (a ,'08b') )
print (' - - - - - - - - - - - - - - - - - - - - - - - - - -( < <2)')
hasil = a << 2
print ('Nilai ',a ,' < <2 dalam biner = ', format ( hasil ,'08b') )

print ('Nilai ',b ,'dalam biner = ', format (b ,'08b') )
print (' - - - - - - - - - - - - - - - - - - - - - - - - - -( < <2)')
hasil = b << 2
print ('Nilai ',b ,' < <2 dalam biner = ', format ( hasil ,'08b') )
       
# TUGAS
print (' ============================= NOT AND ')
print (' ============================= NOT OR ')
print (' ============================= NOT XOR ')
print (' ============================= NOT ( > >2) ')
print (' ============================= NOT ( < <2) ')



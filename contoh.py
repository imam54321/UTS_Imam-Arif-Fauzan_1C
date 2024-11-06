nama_siswa=input('Masukan Nama Siswa: ')
semester=int(input('Masukan angka semester siswa: '))
nomor=int(input('Masukan NIM Siswa: '))
nilai= int(input('Masukan nilai {0-100}: '))
list=[nama_siswa, semester, nomor, nilai] 
print(list)
if nilai >= 90:
    grade = 'A'
elif nilai >= 80:
    grade = 'B'
elif nilai >= 75:
    grade = 'C'
elif nilai >= 60:
    grade = 'D'
elif nilai >= 45:
    grade='E'
print(f'Grade: {grade} ')

if  nilai >= 75:
    print("Selamat Anda Dinyatakan Lulus")
else:
    print("Maaf anda belum Lulus tapi jangan patah semangat belajar")
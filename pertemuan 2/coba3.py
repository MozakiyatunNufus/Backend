#Penulisan String Pada Python
judul = "Belajar Pemrograman Python sampai Bisa"
penulis = 'Dosen Stikom Banyuwangi'

judul = """Belajar Pemrograman Python sampai Bisa"""
penulis = '''Dosen Stikom Banyuwangi'''


# Penulisan Case Pada Python
judul = "Belajar Dasar-Dasar Python"
judul = "Belajar Membuat Program Python"

## Snake Case Digunakan pada:
module_name, package_name, method_name, function_name, ,global_var_name,

## CamelCase digunakan pada:
className, ExceptionName

## ALL CAPS digunakan pada:
GLOBAL_CONSTANT_NAME


# blok percabangan if
if username == 'stikombanyuwangi':
    print("Selamat Datang Admin")
    print("Silakan ambil tempat duduk")

# blok percabangan for
for i in range(10):
    print i


# membuat variabel
nama_variabel = <nilai>
#contoh
variabel_ku = "ini isi variabel"
variabel2 = 20
print variabel_ku
print variabel2


# Type Data Pada Python
nama_ku = "Ali Baba"
umur = 20
tinggi = 183.22


# Jenis-jenis Type Data Pada Python
harga = 12000 #tipe int
berat = 23.12 #float
jarak = 3e3 # float 3000.0, huruf e artinya eksponen 10


# Type Data Teks
nama = "Ivan"
jenis_kelamin ='L'
alamat = """
     Jl. Suka Karya, No 32. RT Kode,
     Kelurahan Mawar, Jakarta
"""
agama = 'islam'


# Type Data Boolean
bergerak = True
nyala = 1 #sebenarnya tipenya int, tapi bisa juga menjadi bool
# Program bio data penduduk desa x
# membuat variabel beserta isinya (nilainya)
nama = "Hartono"
alamat = 'Mataram'
umur = 19
tinggi = 170.5
menikah = False
# mencetak isi variabel
print ("Nama : ", nama )
print ("Alamat : ", alamat)
print ("Umur : ", umur)
print ("Tinggi : ", tinggi)
if(menikah):
    print ("Status: menikah")
else:
    print ("Status: belum menikah")


#Proses Input Pada Python
nama = input("Masukkan nama Anda: ")
#Proses Output: Menampilkan pesan selamat datang
print("Halo,", nama, "! Selamat datang di program Python.")
#Proses Input : Meminta angka dari pengguna
angkat_str = input("Masukkan sebuah angka: ")
#Koversi tipe data dari string ke integer (bilangan bulat)
angka = int(angka_str)
#Proses Output: Menampilkan pesan apakah angka tersebut genap atau ganjil 
if angka % 2 == 0:
    print(angka, "adalah bilangan genap.")
else:
    print(angka, "adalah bilangan ganjil.")


# Proses Output Pada Python
nama = "STIKOM Banyuwangi"
print ("Helloe",nama)



#Fungsi (Function) Pada Python
#mendefinisikan fungsi
def sapa():
    print("Halo, Selamat datang.!")

sapa();
#parameter dan argumen
def sapa(nama)
    print("Halo", nama ,"..!")

sapa("STIKOM")


#Nilai Kembalian(Return)
def tambah(a, b):
    hasil = a + b
    return hasil
total = tambah(3, 5)
print("Hasil penjumlahan:", total)

#Membuat Modul
def sapa(nama):
    print("Halo", nama , "..!")
#Menginpor Modul
# skrip.py
import modul_sapa
modul_sapa.sapa("STIKOM")
# skrip.py
from modul_sapa import sapa
sapa("STIKOM")

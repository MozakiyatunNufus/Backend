# Import semua modul
import Penambahan
import Pengurangan
import Perkalian
import Pembagian

# Masukkan angka pertama
a = float(input("Masukkan angka pertama : "))

# Masukkan angka kedua
b = float(input("Masukkan angka kedua   : "))

print()  # Baris kosong untuk tampilan lebih rapi

# Penambahan dari a dan b adalah c
c = Penambahan.tambah(a, b)
print(f"Penambahan dari {a} dan {b} adalah {c}")

# Pengurangan dari a dan b adalah c
c = Pengurangan.kurang(a, b)
print(f"Pengurangan dari {a} dan {b} adalah {c}")

# Perkalian dari a dan b adalah c
c = Perkalian.kali(a, b)
print(f"Perkalian dari {a} dan {b} adalah {c}")

# Pembagian dari a dan b adalah c
try:
    c = Pembagian.bagi(a, b)
    print(f"Pembagian dari {a} dan {b} adalah {c}")
except ZeroDivisionError as e:
    print(f"Pembagian dari {a} dan {b} adalah Error: {e}")
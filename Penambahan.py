def tambah(a, b):
    """
    Fungsi untuk menambahkan dua angka
    
    Args:
        a: Angka pertama
        b: Angka kedua
    
    Returns:
        Hasil penambahan a + b
    """
    c = a + b
    return c


# Contoh penggunaan jika file ini dijalankan langsung
if __name__ == "__main__":
    print("=== MODUL PENAMBAHAN ===")
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    
    hasil = tambah(angka1, angka2)
    print(f"\nPenambahan dari {angka1} dan {angka2} adalah {hasil}")
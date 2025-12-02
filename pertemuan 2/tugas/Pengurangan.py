def kurang(a, b):
    """
    Fungsi untuk mengurangkan dua angka
    
    Args:
        a: Angka pertama
        b: Angka kedua
    
    Returns:
        Hasil pengurangan a - b
    """
    c = a - b
    return c


# Contoh penggunaan jika file ini dijalankan langsung
if __name__ == "__main__":
    print("=== MODUL PENGURANGAN ===")
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    
    hasil = kurang(angka1, angka2)
    print(f"\nPengurangan dari {angka1} dan {angka2} adalah {hasil}")
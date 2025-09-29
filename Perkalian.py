def kali(a, b):
    """
    Fungsi untuk mengalikan dua angka
    
    Args:
        a: Angka pertama
        b: Angka kedua
    
    Returns:
        Hasil perkalian a * b
    """
    c = a * b
    return c


# Contoh penggunaan jika file ini dijalankan langsung
if __name__ == "__main__":
    print("=== MODUL PERKALIAN ===")
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    
    hasil = kali(angka1, angka2)
    print(f"\nPerkalian dari {angka1} dan {angka2} adalah {hasil}")
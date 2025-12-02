def bagi(a, b):
    """
    Fungsi untuk membagi dua angka
    
    Args:
        a: Angka pertama (pembilang)
        b: Angka kedua (penyebut)
    
    Returns:
        Hasil pembagian a / b
    
    Raises:
        ZeroDivisionError: Jika b adalah 0
    """
    if b == 0:
        raise ZeroDivisionError("Tidak dapat membagi dengan nol")
    c = a / b
    return c


# Contoh penggunaan jika file ini dijalankan langsung
if __name__ == "__main__":
    print("=== MODUL PEMBAGIAN ===")
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    
    try:
        hasil = bagi(angka1, angka2)
        print(f"\nPembagian dari {angka1} dan {angka2} adalah {hasil}")
    except ZeroDivisionError as e:
        print(f"\nError: {e}")
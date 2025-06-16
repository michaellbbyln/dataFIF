from calc import tambah, kurang, kali, bagi

def main():
    while True:
        print("---KALKULATOR---")
        print("1. Tambah")
        print("2. Kurang")
        print("3. Kali")
        print("4. Bagi")
        print("5. Keluar")
        
        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == '5':
            print("Terima kasih telah menggunakan kalkulator ini.")
            break
        if pilihan in ['1', '2', '3', '4']:
            try:
                a = float(input("Masukkan angka pertama: "))
                b = float(input("Masukkan angka kedua: "))
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.")
                continue

            if pilihan == '1':
                hasil = tambah(a, b)
                print(f"Hasil penjumlahan: {hasil}")
            elif pilihan == '2':
                hasil = kurang(a, b)
                print(f"Hasil pengurangan: {hasil}")
            elif pilihan == '3':
                hasil = kali(a, b)
                print(f"Hasil perkalian: {hasil}")
            elif pilihan == '4':
                hasil = bagi(a, b)
                print(f"Hasil pembagian: {hasil}")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main() #make sure agar fungsi main() hanya dipanggil ketika file ini dijalankan langsung, bukan ketika diimpor sebagai modul.
#main()
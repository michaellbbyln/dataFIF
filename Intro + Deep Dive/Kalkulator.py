def panggil():
    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        return a,b
    except ValueError: 
        print("Input tidak valid. Silakan masukkan angka.")


def penjumlahan():
    try:
        a,b = panggil()
        hasil = a + b
        print(f"Hasil penjumlahan {a} + {b} = {hasil}")
        return hasil
    
    except TypeError:
        print("Terjadi kesalahan tipe data. Pastikan input adalah angka.")
    

def pengurangan():
    try:
        a,b =panggil
        hasil = a - b
        print(f"Hasil pengurangan {a} - {b} = {hasil}")
        return hasil
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")
    except TypeError:
        print("Terjadi kesalahan tipe data. Pastikan input adalah angka.")
    
def perkalian():
    try:
        a,b = panggil()
        hasil = a * b
        print(f"Hasil perkalian {a} * {b} = {hasil}")
        return hasil
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")
    except TypeError:
        print("Terjadi kesalahan tipe data. Pastikan input adalah angka.")
    
def pembagian():
    try:
        a,b = panggil()
        hasil = a / b
        print(f"Hasil pembagian {a} / {b} = {hasil}")
        return hasil
    except ValueError: 
        print("Input tidak valid. Silakan masukkan angka.")
    except ZeroDivisionError:
        print("Pembagian dengan nol tidak diperbolehkan.")
    except TypeError:
        print("Terjadi kesalahan tipe data. Pastikan input adalah angka.")
    

print("---KALKULATOR---")
kondisi = True
while kondisi == True:
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")
    while pilihan not in ['1', '2', '3', '4', '5']:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")
        
    if pilihan == '1':
        penjumlahan()
    elif pilihan == '2':
        pengurangan()
    elif pilihan == '3':
        perkalian()
    elif pilihan == '4':
        pembagian()
    else:
        print("Terima kasih telah menggunakan kalkulator ini.")
        kondisi = False
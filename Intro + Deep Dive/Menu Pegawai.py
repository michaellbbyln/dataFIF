kondisi = True
listnama= []
listumur = []
def tampilkan_pegawai():
    print("MENU PEGAWAI")
    print("1. Input Pegawai")
    print("2. Tampilkan Pegawai")
    print("3. Exit")
    #pilihan = input("Masukkan pilihan (1/2/3): ")
    #return pilihan

while kondisi == True:
    #pilihan=tampilkan_pegawai()
    tampilkan_pegawai()
    pilihan = input("Masukkan pilihan (1/2/3): ")
    while pilihan not in ['1', '2', '3']:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
        pilihan = input("Masukkan pilihan (1/2/3): ")
    if pilihan == '1':
        nama = input("Masukkan nama pegawai: ")
        umur = input("Masukkan jabatan pegawai: ")
        print(f"Pegawai {nama} dengan jabatan {umur}.")
        listnama.append(nama)
        listumur.append(umur)
    elif pilihan == '2':
        print("Daftar Pegawai:")
        print("List Nama Pegawai:", listnama)
        print("List Umur Pegawai:", listumur)
        # Di sini seharusnya ada kode untuk menampilkan daftar pegawai
        # Misalnya, jika ada list pegawai, bisa ditampilkan di sini
        print("Belum ada pegawai yang terdaftar.")
    else:
        print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
        kondisi = False

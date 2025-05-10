#program ini tidak 100% hasil saya
#saya cuma meminta AI untuk membuat alur logic lalu saya mencoba membuat sebisa saya dan AI membantu menyempurnakannya
daftar_belanja = []
while True:
    print("1. Tambah Barang")
    print("2. Lihat Daftar Belanja")
    print("3. Delete Barang")
    print("4. Keluar")
    
    pilihan = input("Pilih 1-4: ")

    if pilihan == "1":
        barang = input("Masukkan Nama Barang: ")
        daftar_belanja.append(barang)
    elif pilihan == "2":
        if len(daftar_belanja) == 0:
            print("Daftar Masih Kosong")
        else:
            print ("Daftar Belanja:")
            for i, barang in enumerate(daftar_belanja, start=1):
                print(f"{i}. {barang}")
    elif pilihan == "3":
        if len (daftar_belanja) == 0:
            print ("Daftar Masih kosong, tidak ada yang bisa dihapus")
        else:
            for i, barang in enumerate(daftar_belanja, start=1):
                print(f"{i}, {barang}")
            try:
                nomor = int(input("Masukkan nomor yang mau dihapus:"))
                if 1 <= nomor <= len (daftar_belanja):
                    barang_dihapus = daftar_belanja.pop(nomor -1)
                    print(f"{barang_dihapus} Berhasil dihapus")
                else:
                    print("Nomor tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")
    elif pilihan == "4":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")


'''
=================================================
Graded Challenge 1

Nama  : M. Ilham Hudaya
Batch : HCK-23

Program sederhana untuk mensupport Toko Makmur 
=================================================
'''
class barang: #class ini berfungsi untuk inisialisasi nama barang dan harga barang
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
    
class KeranjangBelanja: #class ini berfungsi untuk menambah, menghapus, menampilan, dan menghitung total belannjaan
    def __init__(self): #menginisialisasikan objek
        self.keranjang = [] #list kosong untuk menyimpan barang yang ingin ditambahkan

    def tambah_barang(self, nama, harga): #untuk menambahkan barang ke dalam keranjang dengan membuat dictionary berisi nama dan harga barang. 
        self.keranjang.append({"nama": nama, "harga": harga})
        print(f'Barang "{nama}" berhasil dimasukkan ke keranjang.')

    def hapus_barang(self, nama):#untuk menghapus barang berdasarkan nama dari keranjang
        for barang in self.keranjang:
                self.keranjang.remove(barang)
                print(f'Barang "{nama}" berhasil dihapus di keranjang belanja.')
                return
        print(f'Barang "{nama}" tidak dbarangukan di keranjang.')

    def tampilkan_keranjang(self):# untuk menampilkan semua barang di dalam keranjang yang telah di input pada fungsi tambah_barang
        if not self.keranjang:
            print("Keranjang belanja kosong.")
        else:
            print("Barang di Keranjang:")
            for i, barang in enumerate(self.keranjang):
                print(f'{i}. {barang["nama"]} - Rp {barang["harga"]:.2f}')

    def total_belanja(self): # menghitung total harga semua barang dalam keranjang menggunakan sum() dan menampilkan hasilnya

        total = 0
        total = sum(barang["harga"] for barang in self.keranjang)
        return total


def menu(): #menampilkan menu utama program dan menjalankan loop yang memungkinkan pengguna untuk berinteraksi dengan KeranjangBelanja
    keranjang = KeranjangBelanja()
    while True:
        print("\nSelamat Datang di Keranjang Belanja Toko Makmur!")
        print("\nMenu:")
        print("1. Menambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Barang di Keranjang")
        print("4. Lihat Total Belanja")
        print("5. Exit")
        
        pilihan = input("Pilihan: ")
        
        if pilihan == "1":
            nama_barang = input("Masukan nama barang: ")
            try:
                harga_barang = float(input("Masukan harga: "))
                keranjang.tambah_barang(nama_barang, harga_barang)
            except ValueError:
                print("Harga harus berupa angka. Silakan coba lagi.")
        elif pilihan == "2":
            nama_barang = input("Masukan nama barang yang ingin dihapus: ")
            keranjang.hapus_barang(nama_barang)
            
        elif pilihan == "3":
            keranjang.tampilkan_keranjang()
            
        elif pilihan == "4":
            total = keranjang.total_belanja()
            print(f'total belanja: Rp {total}')
            
        elif pilihan == "5":
            print("Sampai Jumpa! Terima kasih sudah belanja di Toko Makmur.")
            break

        else:
            print("Pilihannya salah. Coba lagi ya.")
            break

menu()

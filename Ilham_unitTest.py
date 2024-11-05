

import unittest

class KeranjangBelanja:
    def __init__(self):
        self.keranjang = []

    def tambah_barang(self, nama, harga):
        self.keranjang.append({"nama": nama, "harga": harga})
        return f'Barang "{nama}" berhasil dimasukkan ke keranjang.'

    def hapus_barang(self, nama):
        for barang in self.keranjang:
                self.keranjang.remove(barang)
                return f'Barang "{nama}" berhasil dihapus di keranjang belanja.'
        return f'Barang "{nama}" tidak ditemukan di keranjang.'
        
    def total_belanja(self):
        return sum(barang["harga"] for barang in self.keranjang)


class TestKeranjangBelanja(unittest.TestCase):
    def setUp(self): #untuk dapat membuat objek KeranjangBelanja()
        self.keranjang = KeranjangBelanja()

    def test_tambah_barang(self): #Memeriksa apakah barang berhasil ditambahkan pada keranjang
        result = self.keranjang.tambah_barang("Apel", 3400)
        self.assertEqual(result, 'Barang "Apel" berhasil dimasukkan ke keranjang.')
        self.assertEqual(len(self.keranjang.keranjang), 1)
        self.assertEqual(self.keranjang.keranjang[0]["nama"], "Apel")
        self.assertEqual(self.keranjang.keranjang[0]["harga"], 3400)

    def test_hapus_barang(self): #Memeriksa apakah barang berhasil dihapus dari keranjang
        self.keranjang.tambah_barang("jeruk", 2100)
        result = self.keranjang.hapus_barang("jeruk")
        self.assertEqual(result, 'Barang "jeruk" berhasil dihapus di keranjang belanja.')
        self.assertEqual(len(self.keranjang.keranjang), 0)

    def test_hapus_barang_tidak_ada(self):  #Memeriksa respon saat barang yang dihapus tidak ada di keranjang
        result = self.keranjang.hapus_barang("Apel")
        self.assertEqual(result, 'Barang "Apel" tidak ditemukan di keranjang.')

    def test_total_belanja(self): #Memeriksa apakah total belanja dihitung dengan benar
        self.keranjang.tambah_barang("apel", 3400)
        self.keranjang.tambah_barang("jeruk", 2100)
        result = self.keranjang.total_belanja()
        self.assertEqual(result, 5500)


if __name__ == '__main__':
    unittest.main()

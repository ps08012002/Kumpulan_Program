from prettytable import PrettyTable

class daftar(object) :

    def isi () :

        t = PrettyTable()

        print ("Berikut Beberapa Program Yang Sudah Dibuat".center(70))
        t.padding_width = 7
        t.field_names = ["No", "Nama Program"]
        t.add_row (["1\n", "Penghitung Umur\n"])
        t.add_row (["2\n", "Pembuatan Segitiga\n"])
        t.add_row (["3\n", "Pembuatan Belah Ketupat (Ganjil)\n"])
        t.add_row (["4\n", "Pembuatan Belah Ketupat (Genap)\n"])
        t.add_row (["5\n", "Konveri Suhu\n"])
        t.add_row (["6\n", "Hitung Luas Bangun Datar\n"])
        t.add_row (["7\n", "Melihat Calender Di Tahun Tertentu\n"])
        t.add_row (["8\n", "Main Gunting Batu Kertas\n"])
        t.add_row (["9\n", "Cek Bilangan Prima (Satu Input)\n"])
        t.add_row (["10\n", "Cek Bilangan Prima Dengan Batas Akhir\n"])
        t.add_row (["11\n", "Toko Buah Sederhana\n"])
        t.add_row (["12", "Keluar"])

        print (t)

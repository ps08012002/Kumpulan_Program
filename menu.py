from prettytable import PrettyTable

class daftar(object) :

    def isi () :

        t = PrettyTable()

        print ("Berikut Beberapa Program Yang Sudah Dibuat".center(70))
        t.padding_width = 7
        t.field_names = ["No", "Nama Program"]
        t.add_row (["1", "Penghitung Umur"])
        t.add_row (["2", "Pembuatan Segitiga"])
        t.add_row (["3", "Pembuatan Belah Ketupat (Ganjil)"])
        t.add_row (["4", "Pembuatan Belah Ketupat (Genap)"])
        t.add_row (["5", "Konveri Suhu"])
        t.add_row (["6", "Hitung Luas Bangun Datar"])
        t.add_row (["7", "Melihat Calender Di Tahun Tertentu"])
        t.add_row (["8", "Main Gunting Batu Kertas"])
        t.add_row (["9", "Cek Bilangan Prima (Satu Input)"])
        t.add_row (["10", "Cek Bilangan Prima Dengan Batas Akhir"])
        t.add_row (["11", "Keluar"])

        print (t)

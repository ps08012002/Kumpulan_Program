import os
import time
from prettytable import PrettyTable

salom = "Selamat Datang Di Toko Buah Mr.UwaaW"
salom1 = "Berikut Adalah Rincian Belanja Anda"
dis = "Diskon 10% Untuk Belanjaan Diatas Rp.100,000"
z = 46*"="
a = 45*""

pil_buah = []
berat_buah = []
harga_buah = []

def menu ():
    print (70*"=")
    print (salom.center(70))
    print (z.center(70))
    print (dis.center(70))
    print (70*"=")
    print("Berikut Adalah Buah Yang Tersedia \n")
    print ("1. Mangga" + "Rp.35,000 per 1Kg".rjust(35))
    print ("2. Pisang" + "Rp.15,000 per 1Kg".rjust(35))
    print ("3. Jambu" + "Rp.23,000 per 1Kg".rjust(36))
    print ("4. Apel" + "Rp.33,000 per 1Kg".rjust(37))
    print ("5. Nanas" + "Rp.18,000 per 1Kg".rjust(36))
    print ("6. Melon" + "Rp.27,000 per 1Kg".rjust(36))
    print (70*"=")


os.system ('cls')
menu()

buy = int(input("Masukkan Berapa Banyak Jenis Buah Yang Akan Anda Beli --> "))
print (70*"=")

for i in range(buy) :
    jenis = int(input(f"Masukkan Pilihan Buah Ke-{i+1} (1-7) --> "))

    if jenis == 1 :
        pil_buah.append ("Mangga")
        berat =  int(input("Beli Mangga Berapa Kilo = "))
        berat_buah.append (str(berat) + " Kg" )
        harga = berat * 35000
        harga_buah.append (harga)
        # print ('\033[1A' + '\033[K')
        # os.system('cls')
        # menu()
   
    elif jenis == 2 :
        pil_buah.append ("Pisang")
        berat =  int(input("Beli Pisang Berapa Kilo = "))
        berat_buah.append (str(berat) + " Kg" )
        harga = berat * 15000
        harga_buah.append (harga)
        # print ('\033[1A' + '\033[K')
        # os.system('cls')
        # menu()

    elif jenis == 3 :
        pil_buah.append ("Jambu")
        berat =  int(input("Beli Jambu Berapa Kilo = "))
        berat_buah.append (str(berat) + " Kg" )   
        harga = berat * 23000
        harga_buah.append (harga)
        # print ('\033[1A' + '\033[K')
        # os.system('cls')
        # menu()

    elif jenis == 4 :
        pil_buah.append ("Apel")
        berat =  int(input("Beli Apel Berapa Kilo = "))
        berat_buah.append (str(berat) + " Kg" )  
        harga = berat * 33000
        harga_buah.append (harga)
        # print ('\033[1A' + '\033[K')
        # os.system('cls')
        # menu()

    elif jenis == 5 :
        pil_buah.append ("Nanas")
        berat =  int(input("Beli Nanas Berapa Kilo = "))
        berat_buah.append (str(berat) + " Kg" )  
        harga = berat * 18000
        harga_buah.append (harga)
        # print ('\033[1A' + '\033[K')
        # os.system('cls')
        # menu()

    elif jenis == 6 :
        pil_buah.append ("Melon")
        berat =  int(input("Beli Melon Berapa Kilo = "))
        berat_buah.append (str(berat) + " Kg" )        
        harga = berat * 27000
        harga_buah.append (harga)
        # print ('\033[1A' + '\033[K')
        # os.system('cls')
        # menu()

# x= pil_buah.map()
# y= berat_buah.split()
# z= harga_buah.split()

# print(z)


os.system('cls')
print (70*"=")
print (salom1.center(70))
print (70*"=")

t_harga = sum(harga_buah)
x = f"Rp. {t_harga}"

tabel = PrettyTable()
tabel.padding_width = 6
tabel.add_column ("Nama Buah", pil_buah)
tabel.add_column ("Berat Buah", berat_buah)
tabel.add_column ("Harga Buah", harga_buah)

print(tabel)
print("|",end = "")
print("Total Harga".center(44),end = "|")
print(x.center(22),end = "|\n")
print(69*"-")

z = "\nSelamat Anda Mendapatkan Diskon 10% !!!".center(70)
if t_harga > 100000 :
    print (z)
    time.sleep(5)
    os.system('cls')

    dis = t_harga * 10 / 100
    j_total = t_harga - dis
    a = f"Rp. {int(j_total)}"

    print(tabel)
    print("|",end = "")
    print("Total Harga Sebelum Diskon".center(44),end = "|")
    print(x.center(22),end = "|\n")
    print(69*"-")
    print("|",end = "")
    print("Total Harga Setelah Diskon".center(44),end = "|")
    print(a.center(22),end = "|\n")
    print(69*"-")







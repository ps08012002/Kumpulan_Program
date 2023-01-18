import os

salom = "Selamat Datang Di Toko Buah Mr.UwaaW"
dis = "Diskon 10% Untuk Belanjaan Diatas Rp.100,000"
z = 46*"="

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
    print ("6. Nanas" + "Rp.18,000 per 1Kg".rjust(36))
    print ("7. Melon" + "Rp.27,000 per 1Kg".rjust(36))
    print (70*"=")

os.system ('cls')
menu()

buy = int(input("Masukkan Berapa Banyak Jenis Buah Yang Akan Anda Beli --> "))
print (70*"=")

for i in range(buy) :
    jenis = int(input("Masukkan Pilihan Buah (1-7) --> "))
    print ('\033[1A' + '\033[K')

    if jenis == 1 :
        pil_buah.append ("Mangga")
        berat =  int(input("Beli Mangga Berapa Kilo = "))
        berat_buah.append (berat)
        harga = berat * 35000
        harga_buah.append (harga)
        print ('\033[1A' + '\033[K')
        # os.system('cls')
        # menu()
   
    elif jenis == 2 :
        pil_buah.append ("Pisang")
        berat =  int(input("Beli Pisang Berapa Kilo = "))
        berat_buah.append (berat)
        harga = berat * 15000
        harga_buah.append (harga)
        print ('\033[1A' + '\033[K')
        # os.system('cls')
        # menu()

    elif jenis == 3 :
        pil_buah.append ("Jambu")
        berat =  int(input("Beli Jambu Berapa Kilo = "))
        berat_buah.append (berat)   
        harga = berat * 23000
        harga_buah.append (harga)
        print ('\033[1A' + '\033[K')
        # os.system('cls')
        # menu()

    elif jenis == 4 :
        pil_buah.append ("Apel")
        berat =  int(input("Beli Apel Berapa Kilo = "))
        berat_buah.append (berat)  
        harga = berat * 33000
        harga_buah.append (harga)
        print ('\033[1A' + '\033[K')
        # os.system('cls')
        # menu()

    elif jenis == 5 :
        pil_buah.append ("Nanas")
        berat =  int(input("Beli Nanas Berapa Kilo = "))
        berat_buah.append (berat)  
        harga = berat * 18000
        harga_buah.append (harga)
        print ('\033[1A' + '\033[K')
        # os.system('cls')
        # menu()

    elif jenis == 6 :
        pil_buah.append ("Melon")
        berat =  int(input("Beli Melon Berapa Kilo = "))
        berat_buah.append (berat)        
        harga = berat * 27000
        harga_buah.append (harga)
        print ('\033[1A' + '\033[K')
        # os.system('cls')
        # menu()

print (pil_buah)
print (berat_buah)
print (harga_buah)



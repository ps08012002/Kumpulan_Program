class pilihan (object) :

    def pil1 (self) :
        
        import datetime as dt
        today = dt.datetime.today()
        
        print (70*"=" + "\n")
        input_tgl = int(input("Masukkan Tanggal Lahir = "))
        input_bln = int(input("Masukkan Bulan Lahir = "))
        input_thn = int(input("Masukkan Tahun Lahir = "))

        kumpulan = dt.datetime(input_thn, input_bln, input_tgl)

        umur_hari = today - kumpulan
        umur_tahun = umur_hari.days // 365

        print (f"\nUmur Anda Sekarang Adalah {umur_tahun} Tahun")

    def pil2 (self) :

        print (70*"=" + "\n")
        jmlh_sisi = int(input("Masukkan Jumlah Sisi = "))
    
        count = 1
        spasi = jmlh_sisi
    
        while True :

            if count%2 : 
                print(" "*spasi + "+"*count)
                count += 1
                spasi -= 1

            else :
                count += 1
    
            if count > jmlh_sisi:
                break 

    def pil3 (self) :

        print (70*"=" + "\n")
        jmlh_sisi = int(input("Masukkan Jumlah Sisi (Ganjil) = "))
    
        count = 1
        spasi = int(jmlh_sisi/2)

        while True :

            if count%2 : 
                print(" "*spasi + "+"*count)
                count += 1
                spasi -= 1

            else :
                count += 1

            if count > jmlh_sisi:
                break


        count = jmlh_sisi
        spasi = 0

        while True :

            if count%2 :
                print(" "*spasi + "+"*count)
                count -= 1
                spasi += 1

            else :
                count -= 1

            if count == 0:
                break

    def pil4 (self) :

        print (70*"=" + "\n")
        jmlh_sisi = int(input("Masukkan Jumlah Sisi (Genap) = "))
    
        count = 1
        spasi = int(jmlh_sisi/2)

        while True :

            if count%2 == 0 : 
                print(" "*spasi + "+"*count)
                count += 1
                spasi -= 1

            else :
                count += 1

            if count > jmlh_sisi:
                break


        count = jmlh_sisi
        spasi = 1

        while True :

            if count%2 == 0 :
                print(" "*spasi + "+"*count)
                count -= 1
                spasi += 1

            else :
                count -= 1

            if count == 0:
                break

    def pil5 (self) :

        salam = "Program Konversi Suhu".center(68)

        print(70*"=")
        print (f"={salam}=")
        print(70*"=")
        print("\nPilihan Menu ")
        print("1. Konversi Celcius")
        print("2. Konversi Reamur")
        print("3. Konversi Fahrenheit")
        print("4. Konversi Kelvin")

         #INPUT DARI USER

        User = input("\nMasukkan Pilihan : ")
        print ("\n")

        if User == "1" :

            print (70*"=" + "\n")
            Celcius = float (input("Suhu Dalam Celcius = "))

            print ("\nHASIL  \n")

            #Celcius Ke Reamur
            Reamur = (4/5) * Celcius
            print ("1. Reamur = ",Reamur)
    
            #Celcius Ke Fahrenheit
            Fahrenheit = (9/5) * Celcius + 32
            print ("2. Fahrenheit = ",Fahrenheit)
    
            #Celcius Ke Kelvin
            Kelvin = Celcius + 273
            print ("3. Kelvin = ",Kelvin)


        # Konversi Reamur

        elif User == "2" :

            print (70*"=" + "\n")
            Reamur = float (input("Suhu Dalam Reamur = "))
    
            print ("\nHASIL  \n")
    
            #Reamur Ke Celcius
            Celcius = (5/4) * Reamur
            print ("1. Celcius = ",Celcius)
    
            #Reamur Ke Fahrenheit
            Fahrenheit = (9/4) * Reamur + 32
            print ("2. Fahrenheit = ",Fahrenheit)
    
            #Reamur Ke Kelvin
            Kelvin = (5/4) * Reamur + 273
            print ("3. Kelvin = ",Kelvin)


        # Konversi Fahrenheit

        elif User == "3" :

            print (70*"=" + "\n")
            Fahrenheit = float (input("Suhu Dalam Fahrenheit = "))
    
            print ("\nHASIL  \n")
    
            #Fahrenheit Ke Celcius
            Celcius = 5/9 * (Fahrenheit - 32)
            print ("1. Celcius = ",Celcius)
    
            #Fahrenheit Ke Reamur
            Reamur = 4/9 * (Fahrenheit - 32)
            print ("2. Reamur = ",Reamur)
    
            #Fahrenheit Ke Kelvin
            Kelvin = (Fahrenheit - 32) * 5/9 + 273.15
            print ("3. Kelvin = ",Kelvin)


        # Konversi Kelvin

        elif User == "4" :

            print (70*"=" + "\n")
            Kelvin = float (input("Suhu Dalam Kelvin = "))
    
            print ("\nHASIL  \n")
    
            #Kelvin Ke Celcius
            Celcius = Kelvin - 273
            print ("1. Celcius = ",Celcius)
    
            #Kelvin Ke Reamur
            Reamur = 4/5 * (Kelvin - 273)
            print ("2. Reamur = ",Reamur)
    
            #Kelvin Ke Fahrenheit
            Fahrenheit = (Kelvin - 273.15) * 9/5 + 32
            print ("3. Fahrenheit = ",Fahrenheit)

        else :
            print ("\nPilihan Mu Tidak Ada Dalam Daftar !!!")

    def pil6 (self) :

        salam = "Program Hitung Luas Bangun Datar".center(68)

        print(70*"=")
        print (f"={salam}=")
        print(70*"=")
        print('\nPilihan Menu')
        print('1. Segitiga')
        print('2. Lingkaran')
        print('3. Persegi')
        print('4. Persegi Panjang')

        luas = int (input('Masukan Pilihan = '))
        print ("\n")

        if luas == 1 :
            print (70*"=" + "\n")
            a = int (input('Masukan Alas = '))
            t = int (input('Masukkan Tinggi = '))

            rumus = 1/2 * a * t 
            print ("Hasil = ",rumus)

        elif luas == 2 :
            print (70*"=" + "\n")
            j = int (input('Masukkan Jari-Jari = '))
            
            if j % 7 == 0 :
                rumus1 = int( 22/7 * j * j)
                print ('Hasil = ',rumus1)
            else :
                rumus2 = float( 3.14 * j * j )
                print ('Hasil = ',rumus2)

        elif luas == 3 :
            print (70*"=" + "\n")
            s = int(input('Masukkan Sisi = '))

            rumus = s*s
            print ('Hasil = ',rumus)

        elif luas == 4 :
            print (70*"=" + "\n")
            p = int(input('Masukkan Panjang = '))
            l = int(input('Masukkan Lebar = '))

            rumus = p*l
            print ('Hasil = ',rumus)

        else :
            print ("\nPilihan Mu Tidak Ada Dalam Daftar !!!")

    def pil7 (self) :
        
        import calendar 

        print (70*"=" + "\n")

        thn = int(input("Masukkan Tahun Yang Akan Dicari : "))
        print ("\n" + 70*"=")

        i = 0
        while i < 12 :
            i += 1
            print (calendar.month(thn,i))
            print (20*"=")

    def pil8 (self) :

        import random 

        salam = "AYO MAIN SUIT :)".center(68)

        print(70*"=")
        print (f"={salam}=")
        print(70*"=")
        print("\nPilihan Hero Mu ")
        print("1. Gunting ")
        print("2. Batu")
        print("3. Kertas")

        human = int(input("\nPilih Hero Mu --> "))

        bot = random.choice([1, 2, 3])

        if human == 1 and bot == 1 :
            print(30*"=")
            print ("Gunting (You) VS Gunting (Bot)".center(30))
            print(30*"=")
            print ("Draw".center(30))

        elif human == 1 and bot == 2 :
            print(30*"=")
            print ("Gunting (You) VS Batu (Bot)".center(30))
            print(30*"=")
            print ("Masa Lawan Bot Kalah :(".center(30))

        elif human == 1 and bot == 3 :
            print(30*"=")
            print ("Gunting (You) VS Kertas (Bot)".center(30))
            print(30*"=")
            print ("Yeay Kamu Menang :)".center(30))           
        
        elif human == 2 and bot == 2 :
            print(30*"=")
            print ("Batu (You) VS Batu (Bot)".center(30))
            print(30*"=")
            print ("Draw".center(30))

        elif human == 2 and bot == 3 :
            print(30*"=")
            print ("Batu (You) VS Kertas (Bot)".center(30))
            print(30*"=")
            print ("Masa Lawan Bot Kalah :(".center(30))

        elif human == 2 and bot == 1 :
            print(30*"=")
            print ("Batu (You) VS Gunting (Bot)".center(30))
            print(30*"=")
            print ("Yeay Kamu Menang :)".center(30))     

        elif human == 3 and bot == 3 :
            print(30*"=")
            print ("Kertas (You) VS Kertas (Bot)".center(30))
            print(30*"=")
            print ("Draw".center(30))

        elif human == 3 and bot == 1 :
            print(30*"=")
            print ("Kertas (You) VS Gunting (Bot)".center(30))
            print(30*"=")
            print ("Masa Lawan Bot Kalah :(".center(30))

        elif human == 3 and bot == 2 :
            print(30*"=")
            print ("Kertas (You) VS Batu (Bot)".center(30))
            print(30*"=")
            print ("Yeay Kamu Menang :)".center(30))     

    def pil9 (self) :

        i = 1
        c = 0

        print (70*"=" + "\n")
        a = int(input("Masukkan Bilangan Yang Akan Dicek : "))
        print (70*"=" + "\n")
        
        while i <= a :
            b = a%i
            i += 1

            if b == 0 :

                c += 1
            
        if c == 2 :
            print(f"{a} Adalah Bilangan Prima")

        else :
            print(f"{a} Bukanlah Bilangan Prima")        
 
    def pil10 (self) :

        print (70*"=" + "\n")       
        akhir = int(input("Masukkan Batas Akhir : "))
        print (70*"=" + "\n")

        i = 1
        prima = []

        while i <= akhir :
        
            hitung = 0
            a = 1

            while a <= i :
            
                if i%a == 0 :
                    hitung += 1

                a += 1

            if hitung == 2 :
                prima.append(i)

            i += 1

        print (f"Berikut Adalah Bilangan Prima Dari 1 - {akhir}  --> {prima}")

    def pil11 (self) :
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
            jenis = int(input(f"Masukkan Pilihan Buah Ke-{i+1}   --> "))

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

        input("")





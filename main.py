
import os
import datetime as dt
from menu import * 
from kumpulan_fungsi import *

while True :
    os.system('cls')

    today = dt.datetime.today()
    jam = (f"{today.strftime('%H')}.{today.strftime('%M')}".rjust(46))
    salam = "Selamat Datang Di Kumpulan Program Sederhana".center(68)
    penutup = "Terima Kasih Telah Menggunakan Program Kami :)".center(68)

    print (f"{today.strftime('%A')}, {today.strftime('%d')} {today.strftime('%B')} {today.strftime('%Y')} {jam}") 
    print(70*"=")
    print (f"|{salam}|")
    print(70*"=")
    print ("")

    Menu = daftar
    Menu.isi ()

    input_user = int(input("Masukkan Pilihan Anda = "))

    if input_user == 1 :

        fungsi = pilihan
        fungsi.pil1('self')

    elif input_user == 2 :

        fungsi = pilihan
        fungsi.pil2 ('self')

    elif input_user == 3 :

        fungsi = pilihan
        fungsi.pil3('self')

    elif input_user == 4 :

        fungsi = pilihan
        fungsi.pil4('self')

    elif input_user == 5 :

        fungsi = pilihan
        fungsi.pil5('self')

    elif input_user == 6 :

        fungsi = pilihan
        fungsi.pil6('self')

    elif input_user == 7 :

        fungsi = pilihan
        fungsi.pil7('self')

    elif input_user == 8 :

        fungsi = pilihan
        fungsi.pil8('self')

    elif input_user == 9 :

        fungsi = pilihan
        fungsi.pil9('self')

    elif input_user == 10 :

        fungsi = pilihan
        fungsi.pil10('self')

    elif input_user == 11 :
        print ("")

    else :
        print ("\nPilihan Mu Tidak Ada Dalam Daftar !!!")
    
    print("\n" + 70*"=")
    print (f"={penutup}=")
    print(70*"=")

    jawab =  ["Ya", "Yes", "Y", "y", "yes", "ya", "Iya", "iya"]

    akhir = input(f"Mulai Ulang Program ?      --> ")

    if akhir not in jawab :
        break









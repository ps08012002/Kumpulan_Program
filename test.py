akhir = int(input("Masukkan Batas Akhir : "))

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

print (prima)
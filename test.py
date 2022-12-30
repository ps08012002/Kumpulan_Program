awal = int(input("Masukkan Angka Awal : "))
akhir = int(input("Masukkan Angka Akhir : "))

i = 1
c = 0
prima = []
a = int(range(awal,akhir))

print (type(a))
# print (70*"=" + "\n")
# a = int(input("Masukkan Bilangan Yang Akan Dicek : "))
# print (70*"=" + "\n")

while i in range (awal, akhir) :
    b = a%i
    i += 1
    if b == 0 :
        c += 1
    if i > a :
        break
        
    # if c == 2 :
    #     print(f"{a} Adalah Bilangan Prima")
    # else :
    #     print(f"{a} Bukanlah Bilangan Prima")


for i in range (awal, akhir +1) :
    if c == 2 :
        prima.append(a)

print (prima)
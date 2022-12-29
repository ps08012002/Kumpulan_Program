# # awal = int(input("Masukkan Angka Awal : "))
# # akhir = int(input("Masukkan Angka Akhir : "))

a = int(input("Masukkan Bilangan Yang Akan Dicek : "))

i = 1
c = 0

while i <= a :
    b = a%i
    i += 1

    if b == 0 :
        
        c += 1

    if i > a :
        break

if c == 2 :
    print("Ini Bilangan Prima")

else :
    print("Bukan Bilanagn Prima")

# z = 7 % 4
# print (z)
# # if a%1 == 0 and a%a == 0 :
# #     print ("ini bilangan prima")

# # else :
# #     print ("ini bukan bilangan prima")

# a=1
# b=7

# c= b%a

# print(type(c))
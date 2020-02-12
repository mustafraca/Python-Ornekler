#Problem 2
#Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

def EBOB(x, y):
    i = 1

    while (i <= x and i <= y):
        if (x % i == 0 and y % i == 0):
            ebob = i
        i += 1

    return ebob

x = int(input("1.Sayı: "))
y = int(input("2.Sayı: "))

print("EBOB: ", EBOB(x, y))
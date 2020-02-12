print("Asal Sayı")

def asalsayi(sayi):
    for i in range(2, sayi):
        if sayi <= 0:
            print("Negatif Değer Girildi")
            return False
        elif sayi == 1:
            return False
        elif sayi % i == 0:
            return False
        else: return True

sayi = int(input("Sayı Giriniz: "))

if asalsayi(sayi): print(sayi, "Bir Asal Sayıdır")
else: print(sayi, "Bir Asal Sayı Değildir")
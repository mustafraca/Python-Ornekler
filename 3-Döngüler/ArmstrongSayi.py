#Problem 2
#Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.
#Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.
#Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4

print("Armstrong Sayı")

sayi = int(input("Bir Sayı Giriniz: "))
gsayi = sayi
basamak = []
i = 0

while True:
    ondalik = int(gsayi) % 10
    gsayi = int(gsayi / 10)
    basamak.append(ondalik)
    i += 1

    if gsayi == 0:
        break

armstrong = 0
for j in range(i):
    armstrong += basamak[j] ** i

if armstrong == sayi:
    print("{} Bir Armstrong Sayıdır.".format(sayi))
else:
    print("{} Bir Armstrong Sayısı Değildir.".format(sayi))

"""
print("Armstrong Sayı")

sayi = input("Bir Sayı Giriniz: ")
basamakSayisi = len(sayi)
sayi = int(sayi)
basamak = 0
toplam = 0

geciciSayi = sayi

while geciciSayi > 0:
    
    basamak = geciciSayi % 10
    
    toplam += basamak ** geciciSayi
    
    geciciSayi //= 10
    

if (toplam == sayi):
    print("{} Bir Armstrong Sayıdır.".format(sayi))
else:
    print("{} Bir Armstrong Sayısı Değildir.".format(sayi))
"""
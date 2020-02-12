#Problem 1
#Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
#Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)

print("Mükemmel Sayı Bulma\n")

sayi = int(input("Bir Sayı Giriniz: "))

toplam = 1
liste = [toplam]

for i in range(2, sayi):
    if sayi % i == 0:
        liste.append(i)
        toplam += i
print("Girdiğiniz Sayının Tam Bölenleri: {}".format(liste))
if  toplam == sayi:
    print("{} Mükemmel Bir Sayıdır.".format(sayi))
else:
    print("{} Mükemmel Bir Sayı Değildir.".format(sayi))
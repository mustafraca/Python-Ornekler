import random
import time

print("Sayı Tahmin Oyunu\n1 ile 40 Arasında Bir Sayı Tahmin Edin.")

randomSayi = random.randint(1,40)
tahminHakki = 7

while True:
    tahmin = int(input("Tahmin: "))

    if tahmin < randomSayi:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Daha büyük bir sayı giriniz.")
        tahmin -= 1

    elif tahmin > randomSayi:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Daha küçük bir sayı giriniz.")
        tahmin -= 1
    else:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler! Sayı: ", randomSayi)
        break
    if tahmin == 0:
        print("Tahmin Hakkınız Bitti. Sayı: ", randomSayi)
print("""Hesap Makinesi Programı\n
İşlemler
----------------------
1.Toplama
2.Çıkarma
3.Çarpma
4.Bölme
----------------------
""")

a = int(input("Birinci Sayı: "))
b = int(input("İkinci Sayı: "))

islem = input("İşlem Seçiniz: ")

if islem == "1":
    print("{} ile {} Toplamı: {}".format(a, b, a + b))
elif islem == "2":
    print("{} ile {} Farkı: {}".format(a, b, a - b))
elif islem == "3":
    print("{} ile {} Çarpımı: {}".format(a, b, a * b))
elif islem == "4":
    print("{} ile {} Bölümü: {}".format(a, b, a / b))
else:
    print("Geçersiz İşlem...")
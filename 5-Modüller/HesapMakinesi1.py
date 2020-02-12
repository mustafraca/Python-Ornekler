import math

print("""
Hesap Makinesi
İşlemler;
1- Yukarı Yuvarla
2- Aşağı Yuvarla
3- Faktoriyel
4- Karekök
5- Üs
Çıkmak için Q'ya basın!
""")

while True:
    islem = input("İşlem Numarası: ")
    sayi = float(input("Sayı:"))
    if islem == "Q" or islem == "q":
        break
    elif islem == '1':
        print(math.ceil(sayi))
    elif islem == '2':
        print(math.floor(sayi))
    elif islem == '3':
        print(math.factorial(sayi))
    elif islem == '4':
        print(math.sqrt(sayi))
    elif islem == "5":
        üs = int(input("Üs: "))
        print((math.pow(sayi, üs)))
import mymathmodule

print("Hesap Makinesi")

while True:
    print("""
    1- Toplama
    2- Çıkarma
    3- Bölme
    4- Çarpma
    Çıkmak için Q'ya basın!
    """)

    islem = input("İşlem Numarası: ")
    if islem == "Q" or islem == "q":
        break

    while True:
        if islem == '1':
            liste = list()
            while True:
                sayi = input("Sayı (Geri -> Q): ")
                if sayi == "Q" or sayi == "q":
                    break
                liste.append(float(sayi))
            print(liste, "Toplam: ", mymathmodule.toplama(*liste), "\n")
            break

        elif islem == '2':
            liste = list()
            while True:
                sayi = input("Sayı (Geri -> Q): ")
                if sayi == "Q" or sayi == "q":
                    break
                liste.append(float(sayi))
            print(liste, "Fark: ", mymathmodule.cikarma(*liste), "\n")
            break

        elif islem == '3':
            liste = list()
            while True:
                sayi = input("Sayı (Geri -> Q): ")
                if sayi == "Q" or sayi == "q":
                    break
                liste.append(float(sayi))
            print(liste, "Bölüm: ", mymathmodule.bolme(*liste), "\n")
            break

        elif islem == '4':
            liste = list()
            while True:
                sayi = input("Sayı (Geri -> Q): ")
                if sayi == "Q" or sayi == "q":
                    break
                liste.append(float(sayi))
            print(liste, "Çarpımları: ", mymathmodule.carp(*liste), "\n")
            break

    islem = input("Menüye Git -> M, Çıkış -> Q: ")
    if islem == "Q" or islem == "q":
        break

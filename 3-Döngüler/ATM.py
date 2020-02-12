print("ATM Makinesi")

print("1.Bakiye Sorgulama\n2.Para Yatırma\n3.Para Çekme\n\nProgramdan çıkış yapmak için Q'ya basınız.")

bakiye = 1000

while True:
    islem = input("\nİşlem Seçiniz: ")

    if islem == 'Q'  or islem == "q":
        print("Çıkış Yapılıyor...")
        break

    if islem == '1':
        print("Mevcut Bakiyeniz: ", bakiye)
    elif islem == '2':
        tutar = int(input("Yatırılacak Tutar: "))
        bakiye += tutar
        print("Hesabınıza {} TL Yatırıldı. Mevcut Bakiye: {} TL".format(tutar, bakiye))
    elif islem == '3':
        tutar = int(input("Çekilecek Tutar: "))
        if bakiye - tutar < 0:
            print("Yetersiz Bakiye! Mevcut Bakiye: {} TL".format(bakiye))
            continue
        bakiye -= tutar
        print("Hesabınızdan {} TL Para Çekildi. Mevcut Bakiye: {} TL".format(tutar, bakiye))
    else:
        print("Hatalı İşlem!")

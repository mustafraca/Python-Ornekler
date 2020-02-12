print("Faktoriyel Bulma Programı\nÇıkmak için Q'ya Basınız.")

while True:
    sayi = input("\nFaktoriyeli Bulunacak Sayıyı Giriniz: ")
    if sayi == "Q" or sayi == "q":
        print("Çıkış Yapılıyor...")
        break
    else:
        faktoriyel = 1
        sayi = int(sayi)

        for i in range(2, sayi + 1):
            faktoriyel *=  i
        print("Sayının Faktoriyeli: ", faktoriyel)
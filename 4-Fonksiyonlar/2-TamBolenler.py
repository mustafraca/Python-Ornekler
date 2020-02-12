def tambolen(sayi):
    liste = list()
    for i in range(2, sayi):
        if sayi % i == 0:
            liste.append(i)
    return liste

sayi = int(input("Sayı Giriniz: "))

print("Tam Bölenler: ", tambolen(sayi))
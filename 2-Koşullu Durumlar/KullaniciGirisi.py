print("Kullanıcı Giriş Ekranı\n")

dbKullaniciAdi = "mustafraca"
dbKullaniciParolasi = "123"

kullaniciAdi = input("Kullanıcı Adı: ")
kullaniciParolasi = input("Parola: ")

if dbKullaniciAdi == kullaniciAdi and dbKullaniciParolasi == kullaniciParolasi:
    print("Giriş Yapıldı")
elif dbKullaniciAdi != kullaniciAdi and dbKullaniciParolasi == kullaniciParolasi:
    print("Kullanıcı Adı Yanlış!")
elif dbKullaniciAdi == kullaniciAdi and dbKullaniciParolasi != kullaniciParolasi:
    print("Parola Yanlış!")
else:
    print("Kullanıcı Adı ve Parola Yanlış!")
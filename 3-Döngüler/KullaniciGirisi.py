print("Kullanıcı Giriş Ekranı")

dbKullaniciAdi = "Mustafa"
dbKullaniciSifresi = "123"

girisHakki = 3

while True:
    kullaniciAdi = input("Kullanıcı Adı: ")
    kullaniciSifresi = input("Kullanıcı Şifresi: ")

    if dbKullaniciAdi == kullaniciAdi and dbKullaniciSifresi == kullaniciSifresi:
        print("Hesaba Giriş Yapılıyor.")
        break
    elif dbKullaniciAdi != kullaniciAdi and dbKullaniciSifresi == kullaniciSifresi:
        girisHakki -= 1
        print("Kullanıcı Adı Yanlış!")
    elif dbKullaniciAdi == kullaniciAdi and dbKullaniciSifresi != kullaniciSifresi:
        girisHakki -= 1
        print("Kullanıcı Şifresi Yanlış!")
    else:
        girisHakki -= 1
        print("Bilgiler Yanlış!")
    if girisHakki == 0:
        print("Giriş Hakkınız Bitmiştir.")
        break
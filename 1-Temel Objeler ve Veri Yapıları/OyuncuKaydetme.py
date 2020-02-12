print("Oyuncu Kaydetme Programı")

ad = input("Oyuncunun Adı: ")
soyad = input("Oyuncunun Soyadı: ")
takim = input("Oyuncunun Takımı: ")

OyuncuListesi = [ad, soyad, takim]

print("\nBilgiler Kaydediliyor...")

print("\nOyuncunun Adı: {}\nOyuncunun Soyadı: {}\nOyuncunun Takımı: {}".format(OyuncuListesi[0], OyuncuListesi[1], OyuncuListesi[2]))

print("\nBilgiler Kaydedildi...")
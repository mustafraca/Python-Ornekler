#Proje 2
#Bir tane "Bilgisayar" sınıfı oluşturarak bu sınıfa metodlar ve özellikler ekleyin ve bu class'ı kullanmaya çalışın.
#Bu sınıfı yazarken öğrendiğimiz özel metodların hepsini tanımlamaya çalışın.

class Bilgisayar():

    def __init__(self, marka = "BİLGİ YOK", model = "BİLGİ YOK", ekranboyutu = "BİLGİ YOK", ekrancozunurlugu = "BİLGİ YOK", anakart = "BİLGİ YOK", islemci = "BİLGİ YOK", ekrankarti = "BİLGİ YOK", ram = "BİLGİ YOK", harddisk = "BİLGİ YOK", fiyat = "BİLGİ YOK"):
        self.marka = marka
        self.model = model
        self.ekranboyutu = ekranboyutu
        self.ekrancozunurlugu = ekrancozunurlugu
        self.anakart = anakart
        self.islemci = islemci
        self.ekrankarti = ekrankarti
        self.ram = ram
        self.harddisk = harddisk
        self.fiyat = fiyat

    def BilgileriGoster(self):
        print("""
        Marka:              {}
        Model:              {}
        Ekran Boyutu:       {}
        Ekran Çözünürlüğü:  {}
        Anakart Modeli:     {}
        İşlemci Modeli:     {}
        Ekran Kartı:        {}
        Ram:                {}
        Harddisk:           {}
        Fiyatı:             {}
        """.format(self.marka, self.model, self.ekranboyutu, self.ekrancozunurlugu, self.anakart, self.islemci, self.ekrankarti, self.ram, self.harddisk, self.fiyat))

    def BilgiGir(self):
        self.marka = input("Marka: ")
        self.model = input("Model: ")
        self.ekranboyutu = input("Ekran Boyutu: ")
        self.ekrancozunurlugu = input("Ekran Çözünürlüğü: ")
        self.anakart = input("Anakart: ")
        self.islemci = input("İşlemci: ")
        self.ekrankarti = input("Ekran Kartı: ")
        self.ram = input("Ram: ")
        self.harddisk = input("Harddisk: ")
        self.fiyat = input("Fiyat: ")

    def FiyatGuncelle(self, miktar):
        self.fiyat = miktar

    def RamGuncelle(self, miktar):
        self.ram = miktar

    def HarddiskGuncelle(self, miktar):
        self.harddisk = miktar

Bilgisayar1 = Bilgisayar()

print("""
Bilgisayarlar
1- Bilgi Gir
2- Bilgileri Göster
3- Fiyat Güncelle
4- Ram Güncelle
5- Harddisk Güncelle
6- Çıkış (Q/q)
""")

while True:
    islem = input("İşlem: ")

    if islem == "Q" or islem == "q":
        break
    elif islem == "1":
        Bilgisayar1.BilgiGir()
    elif islem == "2":
        Bilgisayar1.BilgileriGoster()
    elif islem == "3":
        miktar = input("Yeni Fiyat: ")
        Bilgisayar1.FiyatGuncelle(miktar)
    elif islem == "4":
        miktar = input("Ram Miktarı (GB): ")
        Bilgisayar1.RamGuncelle(miktar)
    elif islem == "5":
        miktar = input("Harddisk (GB): ")
        Bilgisayar1.HarddiskGuncelle(miktar)
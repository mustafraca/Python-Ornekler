import random
import time

class Kumanda():

    def __init__(self, tvDurum = "Kapalı", tvSes = 0, kanalListesi = ["TRT"], kanal = "TV Kapalı"):
        self.tvDurum = tvDurum
        self.tvSes = tvSes
        self.kanalListesi = kanalListesi
        self.kanal = kanal

    def tvAc(self):
        if self.tvDurum == "Açık":
            print("TV Açık")
        else:
            print("TV Açılıyor...")
            time.sleep(1)
            self.tvDurum = "Açık"
            self.kanal = "TRT"

    def tvKapat(self):
        if self.tvDurum == "Kapalı":
            print("TV Kapalı")
        else:
            print("TV Kapanıyor...")
            time.sleep(1)
            self.tvDurum = "Kapalı"

    def tvSesAyarları(self):
        while True:
            islem = input("Sesi Arttır (>)\nSesi Azalt (<)\nGeri (Q/q)\nİşlem: ")

            if islem == ">":
                if self.tvSes != 50:
                    self.tvSes += 1
                    print("Ses Düzeyi: ", self.tvSes)
            elif islem == "<":
                if self.tvSes != 0:
                    self.tvSes -= 1
                    print("Ses Düzeyi: ", self.tvSes)
            elif islem == "Q" or islem == "q":
                print("Ses Düzeyi Güncellendi: ", self.tvSes)
                break
            else:
                "Hatalı Seçim!"

    def kanalListele(self):
        print(self.kanalListesi)

    def __len__(self):
        return len(self.kanalListesi)

    def kanalEkle(self, kanal):
        print("Kanal Ekleniyor...")
        self.kanalListesi.append(kanal)
        time.sleep(1)
        print("Kanal Eklendi")

    def kanalSil(self, kanal):
        print("Kanal Siliniyor...")
        self.kanalListesi.remove(kanal)
        time.sleep(1)
        print("Kanal Silindi")

    def rastgeleKanal(self):
        self.kanal = self.kanalListesi[random.randint(0, len(self.kanalListesi) - 1)]
        print("İzlenen Kanal: ", self.kanal)

    def __str__(self):
        print("Bilgiler Getiriliyor...")
        time.sleep(1)
        return "TV Durumu: {}\nSes Düzeyi: {}\nKanal Listesi: {}\nKanal Sayısı: {}\nİzlenen Kanal: {}".format(self.tvDurum, self.tvSes, self.kanalListesi, self.__len__(), self.kanal)

Kumanda = Kumanda()

print("""
TELEVİZYON UYGULAMASI
1- TV AÇ
2- TV KAPAT
3- SES AYARLARI
4- KANAL LİSTESİ
5- KANAL SAYISI
6- KANAL EKLE
7- KANAL SİL
8- RASTGELE KANAL DEĞİŞTİR
9- TV BİLGİLERİ
10- ÇIKIŞ (Q/q)
""")

while True:

    islem = input("İşlem: ")

    if islem == "1":
        Kumanda.tvAc()
    elif islem == "2":
        Kumanda.tvKapat()
    elif islem == "3":
        Kumanda.tvSesAyarları()
    elif islem == "4":
        Kumanda.kanalListele()
    elif islem == "5":
        print("Kanal Sayısı: ", Kumanda.__len__())
    elif islem == "6":
        kanal = input("UYARI: Birden fazla kanal girecekseniz ',' ile ayırınız!\nKanal İsmi/İsimleri: ")
        liste = kanal.split(",")
        for i in liste:
            Kumanda.kanalEkle(i)
    elif islem == "7":
        kanal = input("UYARI: Birden fazla kanal girecekseniz ',' ile ayırınız!\nKanal İsmi/İsimleri: ")
        liste = kanal.split(",")
        for i in liste:
            Kumanda.kanalSil(i)
    elif islem == "8":
        Kumanda.rastgeleKanal()
    elif islem == "9":
        print(Kumanda.__str__())
    elif islem == "Q" or islem == "q":
        print("Çıkış Yapılıyor...")
        time.sleep(1)
        break
    else:
        print("Hatalı Seçim!")
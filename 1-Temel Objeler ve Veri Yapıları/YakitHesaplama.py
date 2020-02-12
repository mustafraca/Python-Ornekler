#Problem 3
#Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.

kmYakit = float(input("Aracınız Kilometrede Ne Kadar Yakıyor?: "))
kmYol = float(input("Aracınız ile Toplam Kaç Kilometre Yol Yaptınız?: "))

ucret = kmYakit * kmYol

print("\n{} TL Ödeme Yapmanız Gerekmektedir.".format(ucret))
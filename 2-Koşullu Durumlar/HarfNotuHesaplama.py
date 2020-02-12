"""
Problem 3
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF
"""
print("Harf Notu Hesaplama\n")

vize1 = float(input("1. Vize Notu: "))
vize2 = float(input("2. Vize Notu: "))
final = float(input("Final Notu: "))

ortalama = (vize1 * 30 / 100) + (vize2 * 30 / 100) + (final * 40 / 100)

print("Ortalamanız: ", ortalama)

if ortalama >= 90 and ortalama <= 100:
    print("Harf Notu: AA")
elif ortalama >= 85:
    print("Harf Notu: BA")
elif ortalama >= 80:
    print("Harf Notu: BB")
elif ortalama >= 75:
    print("Harf Notu: CB")
elif ortalama >= 70:
    print("Harf Notu: CC")
elif ortalama >= 65:
    print("Harf Notu: DC")
elif ortalama >= 60:
    print("Harf Notu: DD")
elif ortalama >= 55:
    print("Harf Notu: FD")
elif ortalama < 55 and ortalama >= 0:
    print("Harf Notu: FF")
else:
    print("Geçersiz Değerler")
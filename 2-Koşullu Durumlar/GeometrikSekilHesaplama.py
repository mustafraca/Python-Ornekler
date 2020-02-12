"""
Problem 4
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.
"""

print("Geometrik Şekil Hesaplama\n")

print("İşlemler;\n1. Üçgen\n2. Dörtgen")

secim = input("İşlem Seçiniz: ")

if secim == "1":
    a = float(input("1. Kenar Uzunluğu: "))
    b = float(input("2. Kenar Uzunluğu: "))
    c = float(input("3. Kenar Uzunluğu: "))

    if a == b and b == c:
        print("Üçgenin Tipi: Eşkenar")
    elif a == b or b == c or a == c:
        print("Üçgenin Tipi: İkizkenar")
    else:
        print("Üçgenin Tipi: Çeşitkenar")
elif secim == "2":
    a = float(input("1. Kenar Uzunluğu: "))
    b = float(input("2. Kenar Uzunluğu: "))
    c = float(input("3. Kenar Uzunluğu: "))
    d = float(input("4. Kenar Uzunluğu: "))

    if a == b and b == c and c == d:
        print("Dörtgenin Tipi: Kare")
    elif a != b and b != c and c != d and a != c and a != d and b != d:
        print("Dörtgenin Tipi: Dörtgen")
    else:
        print("Dörtgenin Tipi: Dikdörtgen")
else:
    print("Hatalı Seçim!")
#Problem 2
#Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

#Beden Kitle İndeksi : Kilo / Boy(m) * Boy(m)

print("Beden Kitle İndeksi Programı\n")

boy = float(input("Boyunuz: "))
kilo = float(input("Kilonuz: "))

indeks = kilo / boy ** 2

print("Beden Kitle İndeksi: ", indeks)
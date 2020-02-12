print("2.Dereceden Bir Bilinmeyenli Denklemin Kökünü Bulma Programı\n")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print("\nDenklem: {}x^2 + {}x + {}".format(a, b, c))

delta = b ** 2 - 4 * a * c

birincikok = (-b - delta ** (1/2)) / (2 * a)
ikincikok = (-b + delta ** (1/2)) / (2 * a)

print("\nDenklemin Birinci Kökü: ", birincikok)
print("Denklemin İkinci Kökü: ", ikincikok)
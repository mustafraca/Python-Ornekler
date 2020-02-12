#Problem 6
#Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
#Hipotenüs Formülü: a^2 + b^2 = c^2

print("Hipotenüs Bulma Programı\n")

a = float(input("A Kenarının Uzunluğu: "))
b = float(input("B Kenarının Uzunluğu: "))

hipotenus = (a ** 2 + b ** 2) ** (1/2) #veya hipotenus ** 2 = a ** 2 + b ** 2

print("\nHipotenüs Uzunluğu: ", hipotenus) #veya format fonksiyonu da kullanılabilir. --> print("\nHipotenüs Uzunluğu: {}".format(hipotenus))
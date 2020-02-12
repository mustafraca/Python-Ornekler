#Problem 5
#Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

a = input("Bir Sayı Giriniz: ")
b = input("Bir Sayı Giriniz: ")

print("\nGirdiğiniz Sayılar -> a:{}, b:{}".format(a, b))

a, b = b, a

print("\nDeğiştirilmiş Hali -> a:{}, b:{}".format(a, b))
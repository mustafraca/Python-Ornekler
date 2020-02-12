#Problem 3
#Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

def EKOK(x, y):
    i = 2
    ekok = 1

    while True:
        if x % i == 0 and y % i == 0:
            ekok *= i
            x //= i
            y //= i
        elif x % i == 0 and y % i != 0:
            ekok *= i
            x //= i
        elif x % i != 0 and y % i == 0:
            ekok *= i
            y //= i
        else:
            i += 1
        if x == 1 and y == 1:
            break
    return ekok

x = int(input("1.Sayı: "))
y = int(input("2.Sayı: "))

print("EKOK: ", EKOK(x, y))
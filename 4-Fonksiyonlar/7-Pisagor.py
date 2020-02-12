#Problem 5
#1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)

def pisagor():
    plist = list()
    for i in range(1,101):
        for j in range(1,101):
            p = (i ** 2 + j ** 2) ** 0.5
            if p == int(p):
                plist.append((i, j, int(p)))
    return plist

for i in pisagor():
    print(i)
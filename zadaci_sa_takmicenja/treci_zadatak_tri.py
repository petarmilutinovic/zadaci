kockice = int(input())

rezultat = 0

while kockice > 1:
    kockice //= 2

    rezultat += kockice - kockice // 2

    kockice //= 2

print(rezultat)
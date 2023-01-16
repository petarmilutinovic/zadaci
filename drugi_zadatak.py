komb_1 = int(input())
komb_2 = int(input())

okretanja = 0

for p in range(4):
    broj_komb_1 = komb_1 % 10
    komb_1 -= broj_komb_1
    komb_1 /= 10

    broj_komb_2 = komb_2 % 10
    komb_2 -= broj_komb_2
    komb_2 /= 10

    if broj_komb_1 >= broj_komb_2:
        strana_1 = broj_komb_1 - broj_komb_2
    else:
        strana_1 = broj_komb_1 + 10 - broj_komb_2

    if broj_komb_1 <= broj_komb_2:
        strana_2 = broj_komb_2 - broj_komb_1
    else:
        strana_2 = broj_komb_2 + 10 - broj_komb_1

    okretanja += min(strana_1, strana_2)

print(int(okretanja))
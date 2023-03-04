# Broj bodova ucenika odeljenja 1 i broj ucenika iz odeljenja 2 koji imaju manji broj poena
bodovi_odelj_1 = [34, 41, 62, 25, 43, 33, 44, 92, 100, 14, 65]
bodovi_odelj_2 = [48, 25, 77, 65, 100, 99, 41, 10, 94, 19]

for bodovi_2 in bodovi_odelj_2:
    manji_o1 = 0

    for bodovi_1 in bodovi_odelj_1:
        if bodovi_2 > bodovi_1:
            manji_o1 += 1

    print(bodovi_2, manji_o1)
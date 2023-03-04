# Za domaci popraviti kod da vraca prosecnu ocenu:
bodovi_odelj_1 = [34, 41, 62, 25, 43, 33, 44, 92, 100, 14, 65]
bodovi_odelj_2 = [48, 25, 77, 65, 100, 99, 41, 10, 94, 19]

broj1 = 0
broj2 = 0

for element1 in bodovi_odelj_1:
    if element1 == broj1:
        broj1 += element1
        for element2 in bodovi_odelj_2:
            if element2 == broj2:
                broj2 += element2

prosek_svih_bodova_odeljenja1 = broj1 / len(bodovi_odelj_1)
prosek_svih_bodova_odeljenja2 = broj2 / len(bodovi_odelj_2)
print(prosek_svih_bodova_odeljenja1 + prosek_svih_bodova_odeljenja2)


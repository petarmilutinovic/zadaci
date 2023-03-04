# Za domaci popraviti kod da vraca prosecnu ocenu:
bodovi_odelj_1 = [34, 41, 62, 25, 43, 33, 44, 92, 100, 14, 65]
bodovi_odelj_2 = [48, 25, 77, 65, 100, 99, 41, 10, 94, 19]

bod1 = 0
bod2 = 0
for element1 in bodovi_odelj_1:
    if element1 > 0:
        bod1 += element1
        for element2 in bodovi_odelj_2:
            if element2 > 0:
                bod2 += element2
prosek = (bod1 + bod2) / (len(bodovi_odelj_1) + len(bodovi_odelj_2))
print(prosek)


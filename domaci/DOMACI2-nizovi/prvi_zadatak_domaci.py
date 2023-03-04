# Pronaci u nizu ocene najmanju ocenu i ispisati je:

ocene_na_kontrolnom = [3, 4, 2, 5, 3, 1, 4, 2, 2, 4]
# print(min(ocene_na_kontrolnom))

min_ocena = 6

for ocena in ocene_na_kontrolnom:
    # 3 4 2 5 1 ...
    if ocena < min_ocena:
        min_ocena = ocena

print(min_ocena)



# Pronaci prosek svih ucenika koji imaju ocenu vecu od 1:

ocene_na_kontrolnom = [3, 4, 2, 5, 1, 3, 4, 2, 2, 4]

zbir_ucenika = 0
for ocena in ocene_na_kontrolnom:
    if ocena > 1:
        zbir_ucenika += ocena
prosek_ucenika_bez_jedinice = zbir_ucenika / len(ocene_na_kontrolnom)
print(prosek_ucenika_bez_jedinice)
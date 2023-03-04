# niz = [1, 9, 3, 4, 5, 6, 7, 8, 9]
#del niz[1]
#del niz[7]
#print




ocene_na_kontrolnom = [3, 4, 2, 5, 1, 3, 4, 2, 2, 4]

zbir_ucenika = 0
for ocena in ocene_na_kontrolnom:
    if ocena > 0:
        zbir_ucenika += ocena
prosek_ucenika_bez_jedinice = zbir_ucenika / len(ocene_na_kontrolnom)
print(prosek_ucenika_bez_jedinice)
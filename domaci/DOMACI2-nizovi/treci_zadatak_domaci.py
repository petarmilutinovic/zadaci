# Pronaci prosek svih ucenika koji imaju ocenu vecu od 1:

ocene_na_kontrolnom = [3, 4, 2, 5, 1, 3, 4, 2, 2, 4]
zbir = 0
for element in ocene_na_kontrolnom:
    if element > 1:
        zbir += element
prosek_bez_jedan = zbir / len(ocene_na_kontrolnom)
print(prosek_bez_jedan)
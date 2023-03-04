# Pronaci u nizu ocene najvecu ocenu i ispisati je:

ocene_na_kontrolnom = [3, 4, 2, 5, 1, 3, 4, 2, 2, 4]
max_ocena = 0
for ocena in ocene_na_kontrolnom:
    if ocena > max_ocena:
        max_ocena = ocena
print(max_ocena)
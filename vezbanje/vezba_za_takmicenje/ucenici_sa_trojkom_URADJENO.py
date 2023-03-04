# Broj ucenika koji imaju trojku:

ocene_na_kontrolnom = [3, 4, 2, 5, 1, 3, 4, 2, 2, 4]

tri = 0
for ocena in ocene_na_kontrolnom:
    if ocena == 3:
        tri += 1
print(tri)
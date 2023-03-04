#Drugi najveci element u nizu (drugu najvecu ocenu)
ocene_na_kontrolnom = [3, 4, 2, 5, 3, 1, 4, 2, 2, 4]

# izracunati indeks najveceg broja

del ocene_na_kontrolnom[3]

for i in range(len(ocene_na_kontrolnom) - 1):
    druga_njveca_ocena = 0
for element in ocene_na_kontrolnom:
    if element > druga_njveca_ocena:
        druga_njveca_ocena = element
print(druga_njveca_ocena)

# najveca_ocena = -1
# druga_najveca_ocena = -1

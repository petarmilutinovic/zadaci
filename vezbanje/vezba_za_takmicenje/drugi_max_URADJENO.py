#Drugi najveci element u nizu (drugu najvecu ocenu)
ocene_na_kontrolnom = [3, 4, 2, 5, 3, 1, 4, 2, 2, 4]
del ocene_na_kontrolnom[3]
for i in range(len(ocene_na_kontrolnom)- 1):
    drugi_max = 0
    for ocena in ocene_na_kontrolnom:
        if ocena > drugi_max:
            drugi_max = ocena
print(drugi_max)

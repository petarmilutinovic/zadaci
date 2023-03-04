 

# max_elem = 1

# niz[index]
# istampaj prvi i poslednji element niza

# istampaj sve elemente niza

# for elem in niz

ocene_na_kontrolnom = [3, 4, 2, 5, 1, 3, 4, 2, 2, 4]
proizvod = 1
for element in ocene_na_kontrolnom:
    if element > 1:
        proizvod *= element
prosek_bez_jedan = proizvod / len(ocene_na_kontrolnom)
print(prosek_bez_jedan)
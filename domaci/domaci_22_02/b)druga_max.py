# b) ispisati prva dva najveca broja
# 9 4

broj_elementa_iz_niza = int(input())

elementi_niza = []

for i in range(broj_elementa_iz_niza):
    elementi_niza.append(int(input()))

prva_max = 0
x = 0
for element in elementi_niza:
    if element > prva_max:
        prva_max = element
        i = x
    x += 1

del elementi_niza[i]

druga_max = 0
for i in elementi_niza:
    if i > druga_max:
        druga_max = i


print(prva_max, druga_max)

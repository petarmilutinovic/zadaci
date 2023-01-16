duzina_niza = int(input())

niz_a = list(map(int, input().split()[:duzina_niza]))
niz_n = list(map(int, input().split()[:duzina_niza]))
niz_m = list(map(int, input().split()[:duzina_niza]))

pozicije = []

for i in range(duzina_niza):
    for j in range(duzina_niza):
        if niz_n[i] == niz_a[j]:
            pozicije.append(j)

rezultat = [-1] * duzina_niza

for i in range(duzina_niza):
    rezultat[i] = niz_m[pozicije[i]]

print(*rezultat)
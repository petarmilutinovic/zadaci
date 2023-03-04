broj_elementa = int(input())

niz = []

for i in range(broj_elementa):
    niz.append(int(input()))

max1 = max(niz)
i = 0 
for i in range(broj_elementa):
    if niz[i] == max1:
        break
del niz[i] 

max2 = max(niz)
print(max1, max2)
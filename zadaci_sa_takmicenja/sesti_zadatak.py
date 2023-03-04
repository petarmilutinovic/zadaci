broj_cifara = int(input())
cifre = list(map(int, input().split()[:broj_cifara]))

resenja = []

for i in range(broj_cifara):
    if cifre[i] == 0:
        continue

    for j in range(broj_cifara):
        if j == i:
            continue

        for k in range(broj_cifara):
            if j == k or k == i or cifre[k] % 2 != 0:
                continue

            kandidat = 100 * cifre[i] + 10 * cifre[j] + cifre[k]

            if kandidat not in resenja:
                resenja.append(kandidat)

print(len(resenja))
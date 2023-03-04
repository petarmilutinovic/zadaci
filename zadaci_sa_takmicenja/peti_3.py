komadi = int(input())
dimenzija = int(input())

zbir_redova = [0] * dimenzija

for komad in range(komadi):
    for red in range(dimenzija):
        elementi = list(map(int,input().split(' ')))

        for elem in elementi:
            zbir_redova[red] += elem

ukupan_zbir = 0

for zbir_reda in zbir_redova:
    ukupan_zbir += zbir_reda

predato = 0

for zbir_reda in zbir_redova:
    ukupan_zbir -= zbir_reda
    predato += zbir_reda

    if predato >= ukupan_zbir:
        print(predato - ukupan_zbir)
        exit(0)

print(predato - ukupan_zbir)
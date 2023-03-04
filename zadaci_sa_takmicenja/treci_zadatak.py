jaja_poeni_k = int(input())
hranilica_doprinos = int(input())
zalihe_hrane = int(input())
ptica_1_hrana, ptica_1_poeni = map(int, input().split())
ptica_2_hrana, ptica_2_poeni = map(int, input().split())

if zalihe_hrane + hranilica_doprinos < ptica_1_hrana:
    ptica_1_poeni = -1

if zalihe_hrane + hranilica_doprinos < ptica_2_hrana:
    ptica_2_poeni = -1

if jaja_poeni_k * 2 > ptica_1_poeni + ptica_2_poeni:
    print(jaja_poeni_k * 2)
    exit(0)

if zalihe_hrane >= ptica_1_hrana + ptica_2_hrana:
    print(max(ptica_1_poeni, jaja_poeni_k) + max(ptica_2_poeni, jaja_poeni_k))
    exit(0)

skor = 0

if zalihe_hrane >= ptica_1_hrana:
    skor = max(skor, ptica_1_poeni + jaja_poeni_k)
elif zalihe_hrane + hranilica_doprinos >= ptica_1_hrana:
    skor = max(skor, ptica_1_poeni)

if zalihe_hrane >= ptica_2_hrana:
    skor = max(skor, ptica_2_poeni + jaja_poeni_k)
elif zalihe_hrane + hranilica_doprinos >= ptica_2_hrana:
    skor = max(skor, ptica_2_poeni)

print(skor)
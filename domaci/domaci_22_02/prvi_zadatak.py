# https://dms.rs/wp-content/uploads/2019/03/Zadaci-1.pdf
# 3. [МЕДАЉЕ] На окружном такмичењу из информатике медаљом се награђују најуспешнији такмичари. Праг
# за бронзану медаљу је 70 освојених поена, за сребрну 80, а за златну 90 освојених поена. Са стандардног улаза
# се уноси број ученика (њих највише 100) и затим поени сваког од њих. Напиши програм који одређује број
# бронзаних, сребрних и златних медаља (сваки број исписати у посебном реду).
# Улаз Излаз
# 5    1
# 83   2
# 95   1
# 55
# 70
# 82


broj_ucenika = int(input())

poeni_ucenika = []

for i in range(broj_ucenika):
    poeni_ucenika.append(int(input()))

zlatne_medalje = 0
for poeni in poeni_ucenika:
    if poeni >= 90:
        zlatne_medalje += 1

srebrne_medalje = 0
for poeni in poeni_ucenika:
    if poeni >= 80 and poeni < 90:
        srebrne_medalje += 1

bronzane_medalje = 0
for poeni in poeni_ucenika:
    if poeni >= 70 and poeni < 80:
        bronzane_medalje += 1

print(zlatne_medalje)
print(srebrne_medalje)
print(bronzane_medalje)


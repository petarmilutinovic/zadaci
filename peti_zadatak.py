rec_1 = str(input())
rec_2 = str(input())
rec_3 = str(input())

rezultat = ''

for pozicija in range(len(rec_1)):
    if rec_1[pozicija] == rec_2[pozicija]:
        rezultat += rec_1[pozicija]
        continue

    if rec_1[pozicija] == rec_3[pozicija]:
        rezultat += rec_1[pozicija]
        continue

    if rec_2[pozicija] == rec_3[pozicija]:
        rezultat += rec_2[pozicija]
        continue

    rezultat += '*'

print(rezultat)
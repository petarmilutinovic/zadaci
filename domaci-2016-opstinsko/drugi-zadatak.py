# duzinu pesme u minutima + sekundama
# prostor u megabajtima
# svaki sekund zauzima 16kB
# izracunati preostali prostor

broj_minuta = int(input())
broj_sekundi = int(input())
prostor = int(input())

duzina_pesme_sek = broj_minuta * 60 + broj_sekundi
velicina_pesme = duzina_pesme_sek * 16

prostor_kb = prostor * 1024

preostali_prostor_kb = prostor_kb - velicina_pesme   # 27 520kB

preostalih_mb = preostali_prostor_kb // 1024
prostalih_kb = preostali_prostor_kb % 1024

print(preostalih_mb, " ", prostalih_kb)
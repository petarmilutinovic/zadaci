# unosi se vreme sati minuti i na to vreme se dodaje neki broj minuta. Ispisati novo vreme u formatu sati i minuti

# npr
# 13:28 + 100m = 15:08


sat = int(input())
minut = int(input())
dodatni_minuti = int(input())

ukupni_minuti = (minut + dodatni_minuti) % 60
ukupni_sati = sat + (minut + dodatni_minuti) // 60

print (ukupni_sati,":", ukupni_minuti)


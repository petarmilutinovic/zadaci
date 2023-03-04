# unosi se vreme sati minuti i na to vreme se dodaje neki broj minuta. Ispisati novo vreme u formatu sati i minuti

# npr
# 13:28 + 100m = 15:08

sati = int(input())
minuti = int(input())
dodavanje_minuta = int(input())
uk_minuti = (minuti + dodavanje_minuta) % 60
uk_sati = sati + (minuti + dodavanje_minuta) // 60
if uk_minuti < 10 and uk_sati < 10:
    print("0"-uk_sati, ":", "0"-uk_minuti)
else:
    print(uk_sati, ":", uk_minuti)

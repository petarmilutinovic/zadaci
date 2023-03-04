# a) ucitati niz broj duzine koja se unosi sa standardnog ulaza

# npr.
# 5  <- broj elemenata niza
# 3  <- elementi niza
# 4 
# 9
# 1
# 2

broj_elementa_iz_niza = int(input())

elementi_niza = []

for i in range(broj_elementa_iz_niza):
    elementi_niza.append(int(input()))

print(elementi_niza)




# c) ispisati sve parne brojeve
# 4 2

# d) ispisati sve brojeve manje od 5
# 3 4 1 2

# e) ispisati prosecnu vrednost niza

# f) ispisati koliko ima neparnih elemenata niza
# 3

# g) ispisati zbir prva tri broja
# 3 4 9

# i) ispisati razliku najveceg i najmanjeg elementa niza
# 8

# h) dodati 3 elementa na kraj niza
# 4
# 7
# 2

# j) ispisati drugi od ta tri uneta elementa
# 7

# k) ispisati svaki drugi element niza (ukljucujuci i dodate elemente)
# 3 9 2 4 2

# l) ispisati najmanji od elementa iz tacke k)
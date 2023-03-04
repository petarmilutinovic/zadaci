maxmin = int(input())
n = int(input())
a = int(input()) 
b = int(input())
c = int(input())

if maxmin == 1:
    # Minimalni broj plavooki_visoki = ?
    # Minimalni broj plavooki_visoki_kovrdzavi = ?

    if (2 * glumci) > (visoki + plavooki + kovrdzavi):
        ming = 0
    else:
        ming = (visoki + plavooki + kovrdzavi) - (2 * glumci)
    print(ming)
else:
    # Maksimalni broj plavooki_visoki = ?
    # Maksimalni broj plavooki_visoki_kovrdzavi = ?

     maxg = (((visoki + plavooki + kovrdzavi) - max(visoki, plavooki, kovrdzavi)) - (glumci - max(visoki, plavooki, kovrdzavi))) // 2
     print(maxg)

def izvrni_broj(br):
    izvrnuti_broj = 0

    while br > 0:
        izvrnuti_broj = izvrnuti_broj * 10 + br % 10
        br //= 10

    return izvrnuti_broj


broj = int(input())
okretanja = int(input())

izvrnuti_broj = izvrni_broj(broj)

if okretanja == 0:
    print("DA")
    exit(0)

if okretanja % 2 == 1:
    if broj == izvrnuti_broj:
        print("DA")
    else: 
        print("NE")
    exit(0)

dvaput_izvrnuti = izvrni_broj(izvrnuti_broj)

if broj == dvaput_izvrnuti:
    print("DA")
else:
    print("NE")
m = int(input())
h = int(input())

sati = h - (m // 60) - 1
minut = 60 - (m % 60)

if sati < 10:
    if minut < 10:
        print("0", sati, ":", "0", minut)
    else:
        print("0", sati, ":", minut)
else:
    print(sati, ":", minut)

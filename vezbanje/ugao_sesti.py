stepen = int(input())
minut = int(input())
sekund = int(input())
ugao = stepen * 3600 + minut * 60 + sekund
print(ugao)
if ugao < 324000:
    print("ostar")
else:
    if ugao == 324000:
        print("prav")
    else:
        print("tup")
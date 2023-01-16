stepen = int(input())
minut = int(input())
minut <= 60
ugao = stepen + minut / 60
print(ugao)
if ugao < 90:
    print("ostar")
else:
    if ugao == 90:
        print("prav")
    else:
        print("tup")

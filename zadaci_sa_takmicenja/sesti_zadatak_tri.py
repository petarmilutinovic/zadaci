MAX_POENA = 10 ** 9 + 1

velicina_tima = int(input())

tim_1 = list(map(int, input().split(' ')))
tim_2 = list(map(int, input().split(' ')))
tim_3 = list(map(int, input().split(' ')))

razlike_12 = [MAX_POENA] * velicina_tima

for i1 in range(velicina_tima):
    min_raz = MAX_POENA
    for i2 in range(velicina_tima):
        razlika = abs(tim_1[i1] - tim_2[i2])
        if razlika < min_raz: 
            min_raz = razlika
            razlike_12[i1] = i2

najblizi = MAX_POENA

for i1 in range(velicina_tima):
    for i3 in range(velicina_tima):
        razlika = max(tim_1[i1], tim_2[razlike_12[i1]], tim_3[i3]) - min(tim_1[i1], tim_2[razlike_12[i1]], tim_3[i3])

        if razlika < najblizi: 
            najblizi = razlika

print(najblizi)
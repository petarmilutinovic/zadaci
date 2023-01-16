import math

rastojanje = int(input())
potrosnja_na_100_porodica_1 = int(input())

#math.ceil(5.634634) = 6
# 850 / 100 = 8.5      8.5 * 7 = 59.5        (850 / 100) * 7
potrosnja_porodica_1 = (rastojanje / 100) * potrosnja_na_100_porodica_1
potrosnja_porodica_1 = math.ceil(potrosnja_porodica_1)

potrosnja_na_100_porodica_2 = int(input())
potrosnja_porodica_2 = math.ceil((rastojanje / 100) * potrosnja_na_100_porodica_2)

potrosnja_na_100_porodica_3 = int(input())
potrosnja_porodica_3 = math.ceil((rastojanje / 100) * potrosnja_na_100_porodica_3)

print(potrosnja_porodica_1 + potrosnja_porodica_2 + potrosnja_porodica_3)
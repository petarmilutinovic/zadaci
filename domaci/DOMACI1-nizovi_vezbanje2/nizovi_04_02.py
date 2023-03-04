
niz_brojeva = [123, 5432, 1, -210, 1000, 400, 300]
broj_za_pretragu = int(input())
# da li se uneti broj nalazi u nizu
z = False # 0 ili 1


# upotrebom continue resiti zadatak
for element in niz_brojeva:
    if broj_za_pretragu == element:
        z = True
        break

if z == False:
    print("NE")
else:
    print("DA")

# break     - izlazl iz petlje
# continue  - nastavlja petlju za sledeci element

# for element in niz_brojeva:
#     if element < 400:
#         continue

#     print(element)


# da li se uneti broj nalazi u nizu
niz_brojeva = [123, 5432, 1, -210, 1000, 400, 300]

broj_za_pretragu = int(input())
pm = False
for element in niz_brojeva:
    if broj_za_pretragu == element:
        pm = True
        break
if pm == False:
    print("NE")
else:
    print("DA")
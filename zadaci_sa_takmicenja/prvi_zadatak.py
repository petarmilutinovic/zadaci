tim_a = int(input())
tim_b = int(input())
tim_c = int(input())
tim_d = int(input())

# Proveravamo da li tim D moze da prodje ako izgubi mec 

tim_d_pozicija = 4

if tim_d >= tim_a:
    tim_d_pozicija -= 1

if tim_d >= tim_b:
    tim_d_pozicija -= 1

if tim_d >= tim_c + 3:
    tim_d_pozicija -= 1

if tim_d_pozicija < 3:
    print(0)
    exit(0)

# Proveravamo da li tim D moze da prodje ako odigra nereseno mec 

tim_d_nereseno_pozicija = 4

if tim_d + 1 >= tim_a:
    tim_d_nereseno_pozicija -= 1

if tim_d + 1 >= tim_b:
    tim_d_nereseno_pozicija -= 1

if tim_d + 1 >= tim_c + 1:
    tim_d_nereseno_pozicija -= 1

if tim_d_nereseno_pozicija < 3:
    print(1)
    exit(0)

# Proveravamo da li tim D moze da prodje ako pobedi mec 

tim_d_pobeda_pozicija = 4

if tim_d + 3 >= tim_a:
    tim_d_pobeda_pozicija -= 1

if tim_d + 3 >= tim_b:
    tim_d_pobeda_pozicija -= 1

if tim_d + 3 >= tim_c:
    tim_d_pobeda_pozicija -= 1

if tim_d_pobeda_pozicija < 3:
    print(3)
    exit(0)
else:
    print('ne')
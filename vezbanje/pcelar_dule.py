a = int(input())
b = int(input())
c = int(input())
n = int(input())   
if n <= a:
    print(n)
    print(0)
    print(0)
else:
    if n <= a + b:
        print(a)
        print(n - a)
        print(0)
    else:
        print(a)
        print(b)
        print(n - a - b)
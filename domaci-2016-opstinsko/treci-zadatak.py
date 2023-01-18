maxmin = int(input())
n = int(input())
a = int(input()) 
b = int(input())
c = int(input())

if maxmin == 1:
    if (2 * n) > (a + b + c):
        ming = 0
    else:
        ming = (a + b + c) - (2 * n)
    print(ming)
else:
    maxg = (((a + b + c) - max(a, b, c)) - (n - max(a, b, c))) // 2
    print(maxg)
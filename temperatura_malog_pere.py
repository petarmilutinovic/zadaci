h = int(input())
m = int(input())
n = int(input())
t_max = 0
i_max = 0

for i in range(n):
    t = int(input())
if t > t_max:
    t_max = t
i_max = i
uk_minuta = h * 60 + m + 30 * i_max

print(t_max)
print(uk_minuta // 60)
print(uk_minuta % 60)

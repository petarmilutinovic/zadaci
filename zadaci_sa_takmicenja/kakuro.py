k1_zbir, k2_zbir = map(int, input().split())
v1_zbir, v2_zbir = map(int, input().split())

p_11, p_12 = map(int, input().split())
p_21, p_22 = map(int, input().split())

# nacin 1
k1_dobar = p_11 + p_21 == k1_zbir
k2_dobar = p_12 + p_22 == k2_zbir
v1_dobar = p_11 + p_12 == v1_zbir
v2_dobar = p_21 + p_22 == v2_zbir

if k1_dobar and k2_dobar and v1_dobar and v2_dobar:
    print("da")
else:
    print("ne")

# nacin 2

# if p_11 + p_21 == k1_zbir:
#     if p_12 + p_22 == k2_zbir:
#         if p_11 + p_12 == v1_zbir:
#             if p_21 + p_22 == v2_zbir:
#                 print("da")
#             else:
#                 print("ne")
#         else:
#             print("ne")
#     else:
#         print("ne")
# else:
#     print("ne")

# nacin 3

# if p_11 + p_21 == k1_zbir and p_12 + p_22 == k2_zbir and p_11 + p_12 == v1_zbir and p_21 + p_22 == v2_zbir:
#     print("da")
# else:
#     print("ne")

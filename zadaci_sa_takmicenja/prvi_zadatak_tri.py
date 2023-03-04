c = int(input())
k = int(input())
x = ( 100 * c ) // ( k -1 )
x1 = ( 100 * c ) % ( k -1 )
if x1 == 0:
    print(x)
else:
    print("ne")
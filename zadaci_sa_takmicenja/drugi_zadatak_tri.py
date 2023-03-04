p1 = int(input())
p2 = int(input())
if p1 < 3 and p2 < 3:
    print(str(p1 * 15)+":"+str(p2 * 15))
else:
    if p1 == 3 and p2 < 3:
        print("40"+":"+str(p2 * 15))
    else:
        if p1 < 3 and p2 == 3:
            print(str(p1 * 15)+":"+"40")
        else:
            if p1 >= 3 and p2 >= 3 and p1 == p2:
                print("40"+":"+"40")
            else:
                if p1 >= 3 and p2 >= 3 and p1 > p2:
                    print("Ad"+":"+"40")
                else:
                    print("40"+":"+"Ad")
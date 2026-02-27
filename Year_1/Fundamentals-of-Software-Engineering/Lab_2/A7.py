x1, y1, x2, y2 = map(int, input("x1 y1 x2 y2 >>> ").split())
if (x1 + y1)%2==(x2 + y2)%2:
    print("YES")
    if (x1 + y1)%2==0 and (x2 + y2)%2==0:
        print("WHITE")
    else:
        print("BLACK")
else:
    print("NO")
x,y,x1,y1 = int(input()),int(input()),int(input()),int(input())
if (x+y)%2==(x1+y1)%2:
    print("YES")
    if (x+y)%2==0 and (x1+y1)%2==0:
        print("WHITE")
    else:
        print("BLACK")
else:
    print("NO")
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

def check_quarter(x, y):
    if x > 0 and y > 0:
        return "I"
    elif x < 0 < y:
        return "II"
    elif x < 0 and y < 0:
        return "III"
    else:
        return "IV"

if check_quarter(x1, y1) == check_quarter(x2, y2):
    print(f"YES, {check_quarter(x1, x2)}")
else:
    print("NO")


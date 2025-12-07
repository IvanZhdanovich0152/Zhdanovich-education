import random
a = []
for _ in range(50):
    a.append(random.randint(1, 100))
a.sort()

print(a)

value = int(input())

low = 0
high = len(a)-1
while low <= high:
    mid = (low+high)//2
    if a[mid] == value:
        print(mid)
        break
    elif a[mid] < value:
        low = mid + 1
        continue
    elif a[mid] > value:
        high = mid - 1
        continue
    else:
        print("None")

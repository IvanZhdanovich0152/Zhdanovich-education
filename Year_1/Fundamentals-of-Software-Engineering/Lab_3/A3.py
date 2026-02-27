previous, current = int(input()), int(input())

if previous >= current:
    usage = 10000 - previous + current
else:
    usage = current - previous

bill = 21
usage -= 300

if 0 < usage <= 300:
    bill += usage * 0.06
elif 300 < usage <= 500:
    bill += usage * 0.04
elif usage > 500:
    bill += usage * 0.025

avg = bill / (usage + 300)

print("Предыдущее    Текущее    Использовано    К оплате      Ср. цена m^3")
print("{:6} {:12} {:13} {:14.2f} {:16.2f}".format(previous, current, usage + 300, bill, avg))
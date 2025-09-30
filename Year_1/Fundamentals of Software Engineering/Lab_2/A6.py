s = int(input())
h = 0
m = 0
s_2 = 86400
if s >= 86400:
    s -= 86400
if 0 <= s < 60:
    print("{}:{:02}:{:02}".format(h, m, s))
elif s > 60:
    m = s // 60
    s = s % 60
    if m < 60 :
        print("{}:{:02}:{:02}".format(h, m, s))
    else:
        h = m // 60
        m = m % 60
        print("{}:{:02}:{:02}".format(h, m, s))
else:
    s_2 += s
    if 0 < s_2 < 60:
        print("{}:{:02}:{:02}".format(h, m, s_2))
    elif s_2 > 60:
        m = s_2 // 60
        s_2 = s_2 % 60
        if m < 60:
            print("{}:{:02}:{:02}".format(h, m, s_2))
        else:
            h = m // 60
            m = m % 60
            print("{}:{:02}:{:02}".format(h, m, s_2))

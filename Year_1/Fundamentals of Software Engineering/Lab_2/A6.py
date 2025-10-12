seconds = int(input("Введите число секунд с начала суток >>> "))
hour = 0
minutes = 0
second_in_day = 86400
if seconds >= 86400:
    seconds -= 86400
if 0 <= seconds < 60:
    print("{}:{:02}:{:02}".format(hour, minutes, seconds))
elif seconds > 60:
    minutes = seconds // 60
    seconds = seconds % 60
    if minutes < 60 :
        print("{}:{:02}:{:02}".format(hour, minutes, seconds))
    else:
        hour = minutes // 60
        minutes = minutes % 60
        print("{}:{:02}:{:02}".format(hour, minutes, seconds))
else:
    second_in_day += seconds
    if 0 < second_in_day < 60:
        print("{}:{:02}:{:02}".format(hour, minutes, second_in_day))
    elif second_in_day > 60:
        minutes = second_in_day // 60
        second_in_day = second_in_day % 60
        if minutes < 60:
            print("{}:{:02}:{:02}".format(hour, minutes, second_in_day))
        else:
            hour = minutes // 60
            minutes = minutes % 60
            print("{}:{:02}:{:02}".format(hour, minutes, second_in_day))

def del_brackets(string):
    while True:
        if ")" in string or "(" in string:
            left = string.find("(")
            right = string.find(")")
            string = string.replace(string[left:right+1], "")

        else:
            string = string.replace("  ", " ")
            break
    return string

# "Падал (куда он там падал) прошлогодний (значит очень старый) снег (а почему не дождь) () (())"
print(del_brackets(input("Enter a string: ")))
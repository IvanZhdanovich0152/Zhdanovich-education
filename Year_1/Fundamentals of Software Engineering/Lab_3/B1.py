with open("file_B/5.ChaseData.txt", "r") as file:
    content = file.read()
    line_data = content.split('\n')
rows_x, columns_y = line_data[0].split()

position_mouse = (0, 0)
count_m = 0
distance_mouse = 0
is_caught = False

position_cat = ("?", "?")
count_c = 0
distance_cat = 0

distance_between = 0



def move_to(position, x, y):
    if position[0] + x > int(rows_x):
        position[0] -= int(rows_x) - x
    elif position[0] + x <= 0:
        position[0] = int(rows_x) + (position[0] + x)
    else:
        position[0] += x
    if position[1] + y > int(columns_y):
        position[1] -= int(columns_y) - y
    elif position[1] + y <= 0:
        position[1] = int(columns_y) + (position[1] + y)
    else:
        position[1] += y
    return position

print("Cat and Mouse\n")
print("  Cat        Mouse    Distance")
print("-" * 31)

for line in line_data[1:-1]:
    data = line.split()
    if data[0] == "M" and count_m < 1:
        count_m += 1
        position_mouse = [int(data[1]), int(data[2])]
    elif data[0] == "M":
        position_mouse = move_to(position_mouse, int(data[1]), int(data[2]))
        distance_mouse += abs(int(data[1])) + abs(int(data[2]))

    if data[0] == "C" and count_c < 1:
        count_c += 1
        position_cat = [int(data[1]), int(data[2])]
    elif data[0] == "C":
        position_cat = move_to(position_cat, int(data[1]), int(data[2]))
        distance_cat += abs(int(data[1])) + abs(int(data[2]))


    if data[0] == "P":
        if position_cat == position_mouse  or position_mouse == position_cat:
            is_caught = True
            break
        if not position_cat[0] == "?":
            distance_between = abs(position_cat[0] - position_mouse[0]) + abs(position_cat[1] - position_mouse[1])
            print("({:2},{:2})     ({:2},{:2}) {:8}".format(position_cat[0],position_cat[1], position_mouse[0], position_mouse[1], distance_between))
        else:
            print("( ?, ?)     ({:2},{:2})".format(position_mouse[0], position_mouse[1]))

print("-" * 31 + "\n\n")
print("Distance   Mouse    Cat")
print("{:16} {:6}".format(distance_mouse, distance_cat))

if is_caught:
    print("\nMouse caught at: ({},{})".format(position_mouse[0], position_mouse[1]))
else:
    print("\nMouse evaded Cat")
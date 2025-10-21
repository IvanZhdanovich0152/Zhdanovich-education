with open("file_B/Precip2.txt", "r") as file:
    content = file.read()
    line_data = content.split('\n')

path_to_file_out = f'file_B/02Report.txt'
file_out = open(path_to_file_out, 'w', encoding='utf-8')

lines = {}
num_lines = 4
days = 1
graph = " "

match line_data[2].split(", ")[0]:
    case 'January'| 'March'| 'May'| 'July'| 'August'| 'October'| 'December':
        days = 31
    case 'April'| 'June'| 'September'| 'November':
        days = 30
    case 'February':
        if line_data[2].split(", ")[1] == '1996':
            days = 29
        else:
            days = 28

file_out.write(f"Programmer: Ivan Zhdanovich"
               f" \n{line_data[0]} \n\n")
file_out.write(f"Precipitation report for {line_data[1]} during {line_data[2]} \n\n")
file_out.write("Error         Day       Line\n")

for line in line_data[3:-1]:
    data = line.split()
    data[0], data[1] = int(data[0]), float(data[1])

    if  data[0] in lines:
        file_out.write("Repeated {: 8} {: 10}\n".format(data[0], num_lines))


    elif data[0] > days:
        file_out.write("Invalid {: 9} {: 10}\n".format(data[0], num_lines))

    else:
        lines[data[0]] = data[1]
    num_lines += 1

file_out.write("\nDay Amount Graph\n")

for i in range(1, days + 1):
    values = lines.get(i, "NA")
    if values != "NA" and values != 0:
        values = float(values)
        a = int(values // 0.25)
        graph = "*" * (a+1)
        file_out.write("{: 3} {: 6} {}".format(i, values, graph) + "\n")
    else:
        file_out.write(f"{i: 3} {values: >6} {graph}" + "\n")
    graph = " "

maximum = float(max(lines.values()))
minimum = float(min(lines.values()))
avg = float(sum(lines.values()) / days)

file_out.write("\n" + "Minimum     Maximum     Average" + "\n")
file_out.write(f"{minimum: 7.2f} {maximum: 11.2f} {avg: 11.2f}\n")


file_out.close()

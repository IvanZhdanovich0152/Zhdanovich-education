Path_to_File_with_data = 'file_B/3.WCData.txt'
x = Path_to_File_with_data[7]
Path_to_new_file_result = f'file_B/{x}.WindChillReport.txt'

with open(Path_to_File_with_data, 'r', encoding='utf-8') as file:
    content = file.read()
    line_data = content.split('\n')

total_temp = 0
count_obs = 0

file_with_result = open(Path_to_new_file_result, 'w', encoding='utf-8')

file_with_result.write("Time     WC temp     WC Effect" + "\n")
file_with_result.write("-" * 31 + "\n")

for line in line_data[2:]:
    data = line.split()
    time = data[0]
    air_temp = int(data[1])
    wind_speed = int(data[2])

    wc_temp = 35.74 + 0.6125 * air_temp + (0.4275 * air_temp - 35.74) * wind_speed**0.16
    wc_effect = wc_temp - air_temp

    total_temp += wc_temp
    count_obs += 1
    file_with_result.write("{} {: 7.1f} {: 13.1f}".format(time, wc_temp, wc_effect) + "\n")

avg_temp = total_temp / count_obs

file_with_result.write("-" * 31 + "\n")
file_with_result.write("The average adjusted temperature, based on {} observations, was {:.1f}".format(count_obs,avg_temp))

file_with_result.close()
with open('file_B/inmap1.dat', 'r', encoding='utf-8') as file:
    content = file.read()
    line_numbers = content.split()

scale = float(line_numbers[1])
total_mile = 0
number_point = 0

print("Ivan Zhdanovich \nSimple Map Distance Computations\n")
print(f'Map Scale Factor:    {scale} miles per inch\n')
print("      Map       Mileage\n      Measure   Distance")
print("="*61)

for num in line_numbers[2:]:
    inch = float(num)
    mile = inch * scale
    mile = round(mile, 1)
    total_mile += mile
    number_point += 1
    print("#{}:{: 8}:{: 10}".format(number_point, inch, mile))


print("="*61)
print(f'Map Total Distance:   {total_mile} miles')







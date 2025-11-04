"""
2 in_file
1 out_file

defunction:
seach(list, str) -> turle or str
diff(list, str, str) -> int
mode(list, str) -> str
encode(str) -> str
decode(str) -> str
read_data(file) -> list(list(str))

сжатие максимум 9 минимум 3
"""
from collections import Counter

def read_data(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read().splitlines()
        lines_data = []
        for line in data:
            lines_data.append(line.split('\t'))
    return lines_data

def decode(string):
    for char in string:
        if char.isdigit() and (char != '1' or char != '2'):
            position = string.find(char)
            string = string[:position] + string[position+1] * (int(char)-1) + string[position + 1:]
        else:
            continue
    return string

def seach_fragment(data:list, *protein_part:str):
    protein_part = decode(protein_part)
    for item in data:
        name, organism, protein = item
        for protein in item:
            if protein.find(protein_part) != -1:
                return True, (organism, name)
    return False, "NOT FOUND"

def seach(data:list, protein_name:str):
    for items in data:
        name, organism, protein = items
        for name in items:
            if name == protein_name:
                return True, protein
    return False, protein_name

def diff(data:list, protein_1:str, protein_2:str):
    flag1, protein_1 = seach(sequences, protein_1)
    flag2, protein_2 = seach(sequences, protein_2)
    count = 0
    odds = 0

    if flag1 or flag2:
        if len(protein_1) > len(protein_2):
            odds = len(protein_1) - len(protein_2)
            protein_2 = protein_2+ "#"*odds
        elif len(protein_2) > len(protein_1):
            odds = len(protein_2) - len(protein_1)
            protein_1 = protein_1 + "#"*odds
        for i in range(len(protein_1)):
            if protein_1[i] != protein_2[i]:
                count += 1
            else:
                continue
        return count
    elif not flag1:
        return protein_1
    elif not flag2:
        return protein_2
    return None

def mode(data:list, protein:str):
    flag, protein = seach(sequences, protein)
    if flag:
        most_common_char = sorted(Counter(protein).most_common(4), key=lambda x: x[0])
        return most_common_char[0]
    else:
        return protein


sequences = read_data("other_file/sequences.0.txt")
print(sequences)
commands = read_data("other_file/commands.0.txt")
print(commands)

print(diff(sequences, "Cecropin", "Pre-T/NK cell associated protein 6H9A"))


print(mode(sequences, "Cecropin"))


#flag, a = seach_fragment(data=sequences, protein_part="II")
# if flag:
#     organism, name = a
#     print(organism, name)
# else:
#     print(a)
#
#
# flag, protein = seach(sequences, "6.8 kDa mitochond proteolipid")
#
# if flag:
#     print(protein)
# else:
#     print(f"Missing: {protein}")
#

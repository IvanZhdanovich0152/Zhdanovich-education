"""
2 in_file
1 out_file

defunction:
search_fragment(list, str) -> list[bool, tuple]
seach(list, str) -> list[bool, str]
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

def search_fragment(data:list, protein_part:str) -> list[bool, tuple]:
    protein_part = decode(protein_part)
    for item in data:
        name, organism, protein = item
        for protein in item:
            if protein.find(protein_part) != -1:
                return True, (organism, name)
    return False, "NOT FOUND"

def search(data:list, protein_name:str):
    for items in data:
        name, organism, protein = items
        for name in items:
            if name == protein_name:
                return True, protein
    return False, protein_name

def diff(data:list, protein_1:str, protein_2:str):
    flag1, protein_1 = search(sequences, protein_1)
    flag2, protein_2 = search(sequences, protein_2)
    protein_1 = decode(protein_1)
    protein_2 = decode(protein_2)
    count = 0
    odds = 0

    if flag1 or flag2:
        if len(protein_1) > len(protein_2):
            odds = len(protein_1) - len(protein_2)
            protein_2 = protein_2 + "#" * odds
        elif len(protein_2) > len(protein_1):
            odds = len(protein_2) - len(protein_1)
            protein_1 = protein_1 + "#" * odds
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

def mode(data:list, protein:str) :
    flag, protein = search(sequences, protein)
    if flag:
        counter = Counter(protein)
        max_freq = max(counter.values())
        return min(aa for aa, freq in counter.items() if freq == max_freq), max_freq
    else:
        return [protein, -1]


sequences = read_data("other_file/sequences.1.txt")
commands = read_data("other_file/commands.1.txt")

path_to_file_out = "other_file/output.txt"
with open(path_to_file_out, 'w', encoding='utf-8') as file_out:
    file_out.write("Ivan Zhdanovich\n")
    file_out.write("Genetic Searching\n")

    for i, command in enumerate(commands):
        file_out.write("-" * 75 +"\n")
        i+=1
        match command[0]:
            case "search":
                flag_search, tuple_protein = search_fragment(sequences, command[1])
                if flag_search:
                    organism, protein = tuple_protein
                    file_out.write("{:03}   {:<9}{}\n".format(i,command[0], command[1]))
                    file_out.write("{}\t\t\t\t{}\n".format("organism", "protein"))
                    file_out.write("{}\t\t{}\n".format(organism, protein))
                else:
                    file_out.write("{:03}   {:<9}{}\n".format(i, command[0], command[1]))
                    file_out.write("{}\t\t\t\t{}\n".format("organism", "protein"))
                    file_out.write("{}\n".format(tuple_protein))
            case "diff":
                file_out.write("{:03}   {}   {}\t{}\n".format(i, command[0], command[1], command[2]))
                count_diff = diff(sequences, command[1], command[2])
                if type(count_diff) == int:
                    file_out.write("{}\n".format("amino-acids difference: "))
                    file_out.write("{}\n".format(count_diff))
                else:
                    file_out.write(f"MISSING: {count_diff}\n")
            case "mode":
                file_out.write("{:03}   {:<9}{}\n".format(i, command[0], command[1]))
                aa, count = mode(sequences, command[1])
                if count == -1:
                    file_out.write(f"MISSING: {aa}\n")
                else:
                    file_out.write("{}\n".format("amino-acid occurs:"))
                    file_out.write("{} \t\t {}\n".format(aa, count))
            case _:
                continue
    file_out.write("-" * 75 +"\n")



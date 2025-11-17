from collections import Counter
from loguru import logger

def read_data(file) -> list:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = f.read().splitlines()
            lines_data = []
            for line in data:
                lines_data.append(line.split('\t'))
        logger.info("Successfully read data from {}!".format(file))
        return lines_data
    except FileNotFoundError:
        logger.error(f'File {file} not found.')
        exit(-1)


def decode(protein_line: str) -> str:
    for char in protein_line:
        if char.isdigit() and (char != '1' or char != '2'):
            position = protein_line.find(char)
            protein_line = protein_line[:position] + protein_line[position + 1] * (int(char) - 1) + protein_line[position + 1:]
        else:
            continue
    logger.info("Successfully decode protein line: {}".format(protein_line))
    return protein_line


def search_fragment(data: list, fragment: str) -> list[bool, tuple]:
    fragment = decode(fragment)
    logger.info(f'Searching fragment {fragment}...')

    for item in data:
        name, organism, *proteins = item
        for protein in proteins:
            if fragment in protein:
                logger.info(f'Found fragment for {organism} and {name}')
                return [True, (organism, name)]

    logger.warning(f'No fragment for {fragment}')
    return [False, "NOT FOUND"]


# def search_fragment(data:list, fragment:str) -> list[bool, tuple]:
#     fragment = decode(fragment)
#     logger.info(f'Searching fragment for {fragment}...')
#     for item in data:
#         for protein in item:
#             if protein.find(fragment) != -1:
#                 organism, name = item[1], item[0]
#                 logger.info(f'Found fragment for {organism} and {name}')
#                 return True, (organism, name)
#     logger.info(f'No fragment for {fragment}')
#     return False, "NOT FOUND"

def search(data:list, protein_name:str) -> list[bool, str]:
    logger.info(f'Searching for {protein_name}...')
    for items in data:
        for name in items:
            if name == protein_name:
                protein = items[2]
                logger.info(f'Found protein {protein}...')
                return [True, protein]
    logger.warning(f'No protein with name: {protein_name}')
    return [False, protein_name]


def diff(data:list, protein_1:str, protein_2:str) -> int:
    found_1, protein_1 = search(sequences, protein_1)
    found_2, protein_2 = search(sequences, protein_2)

    if not found_1:
        return protein_1
    elif not found_2:
        return protein_2
    elif found_1 and found_2:
        logger.info(f'Difference between {protein_1} and {protein_2}')
        protein_1 = decode(protein_1)
        protein_2 = decode(protein_2)
        max_len = max(len(protein_1), len(protein_2))
        protein_1 = protein_1.ljust(max_len, "#")
        protein_2 = protein_2.ljust(max_len, "#")

        return sum(c1 != c2 for c1, c2 in zip(protein_1, protein_2))
    return None


def mode(data: list, protein: str) -> list[str, int]:
    found, protein = search(sequences, protein)
    if found:
        counter = Counter(protein)
        max_freq = max(counter.values())
        return [min(aa for aa, freq in counter.items() if freq == max_freq), max_freq]
    else:
        logger.warning(f'No protein with name: {protein}')
        return [protein, -1]


path_file_with_commands = "other_file/commands.1.txt"
path_file_with_data = "other_file/sequences.1.txt"
path_to_file_out = "other_file/output.txt"


sequences = read_data("other_file/sequences.1.txt")
commands = read_data("other_file/commands.2.txt")



with open(path_to_file_out, 'w', encoding='utf-8') as file_out:
    file_out.write("Ivan Zhdanovich\n")
    file_out.write("Genetic Searching\n")

    for i, command in enumerate(commands, 1):
        file_out.write("-" * 75 +"\n")
        cmd, *args = command
        match cmd:
            case "search":
                fragment = args[0]
                file_out.write(f"{i:03}   {cmd:<9}{fragment}\n")
                file_out.write("organism\t\t\t\tprotein\n")
                found, result = search_fragment(sequences, fragment)
                if found:
                    organism, protein = result
                    file_out.write(f"{organism}\t\t{protein}\n")
                else:
                    file_out.write("NOT FOUND\n")
            case "diff":
                protein1, protein2 = args
                file_out.write(f"{i:03}   {cmd}   {protein1}\t{protein2}\n")
                count_diff = diff(sequences, protein1, protein2)
                if isinstance(count_diff, int):
                    file_out.write("amino-acids difference: \n")
                    file_out.write(f"{count_diff}\n")
                else:
                    file_out.write(f"MISSING: {count_diff}\n")
            case "mode":
                protein_name = args[0]
                file_out.write(f"{i:03}   {cmd:<9}{protein_name}\n")
                aa, count = mode(sequences, protein_name)
                if count == -1:
                    file_out.write(f"MISSING: {aa}\n")
                else:
                    file_out.write("amino-acid occurs:\n")
                    file_out.write(f"{aa} \t\t {count}\n")
            case _:
                continue
    file_out.write("-" * 75 +"\n")

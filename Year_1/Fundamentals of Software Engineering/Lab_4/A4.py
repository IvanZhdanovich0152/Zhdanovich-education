def is_valid_number(string):
    return string.isdigit() and len(string) in [13,14, 15, 16]

def check_luhn(string):
    checksum = 0
    for i in range(len(string) - 2, -1, -2):
        if int(string[i]) * 2 > 9:
            checksum += int(string[i]) * 2 - 9
        else:
            checksum += int(string[i]) * 2
    for j in range(len(string) - 1, -1, -2):
        checksum += int(string[j])
    return checksum % 10 == 0

def get_card_type(string):
    if len(string) == 13 or len(string) == 16 and string.startswith('4'):
        return "Visa"
    elif len(string) == 16 and string.startswith('5') or string.startswith('2'):
        return "Mastercard"
    elif len(string) == 15 and string.startswith('34') or string.startswith('37'):
        return "American Express"
    elif string.startswith('6'):
        return "Discover"
    elif string.startswith('30') or string.startswith('36') or string.startswith('38') or string.startswith('39'):
        return "Diner's Club International"
    else:
        return "Invalid"



file_in = "card.data"
with open(file_in) as f:
    content = f.read()
    card_numbers = content.split("\n")

for card_number in card_numbers[:-1]:
    if is_valid_number(card_number):
        if check_luhn(card_number):
            print(f"{card_number} - {get_card_type(card_number)}")
        else:
            print('Invalid card number')
    else:
        print('Invalid card number')
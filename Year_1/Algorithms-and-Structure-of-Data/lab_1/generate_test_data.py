import random


def generate_officials_data(n, max_bribe=100, max_set_size=None):

    subordinates = [[] for _ in range(n)]
    visa_sets = []
    bribes = []

    sets_for_officer = []
    bribes_for_officer = []

    for i in range(2, n + 1):
        boss = random.randint(1, i - 1)
        subordinates[boss - 1].append(i)

    for i in range(n):
        sub_list = subordinates[i]
        num_subs = len(sub_list)

        if num_subs == 0:
            num_sets = 1
        else:
            num_sets = random.randint(1, min(15, 2 ** num_subs))

        if num_subs > 0 and random.choice([True, False]):
            sets_for_officer.append([])
            bribes_for_officer.append(random.randint(0, max_bribe))
            num_sets -= 1


        possible_subs = sub_list.copy()

        for _ in range(max(0, num_sets)):
            if max_set_size:
                set_size = random.randint(1, min(max_set_size, num_subs))
            else:
                set_size = random.randint(1, num_subs) if num_subs > 0 else 0


            if num_subs > 0 and set_size > 0:
                selected = sorted(random.sample(possible_subs, min(set_size, num_subs)))
            else:
                selected = []

            if selected not in sets_for_officer:
                sets_for_officer.append(selected)
                bribes_for_officer.append(random.randint(0, max_bribe))

        if not sets_for_officer:
            sets_for_officer.append([])
            bribes_for_officer.append(random.randint(0, max_bribe))

        visa_sets.append(sets_for_officer)
        bribes.append(bribes_for_officer)

    return subordinates, visa_sets, bribes


def print_generated_data(subordinates, visa_sets, bribes):
    n = len(subordinates)

    print(f"Сгенерировано {n} чиновников:")
    print("-" * 50)

    for i in range(n):
        print(f"\nЧиновник {i + 1}:")
        print(f"  Подчиненные: {subordinates[i] if subordinates[i] else 'нет'}")
        print(f"  Наборы виз и взятки:")
        for j, (visa_set, bribe) in enumerate(zip(visa_sets[i], bribes[i])):
            print(f"    {j + 1}. {visa_set if visa_set else 'пустой'} -> взятка {bribe}")


if __name__ == "__main__":
    amount_officer = 10
    list_subordinates, list_visa_sets, list_bribes = generate_officials_data(amount_officer, max_bribe=100)
    print_generated_data(list_subordinates, list_visa_sets, list_bribes)


def solution(subs, bribes, visa_sets):
    cost = {}
    chosen_set = {}

    def calculate_cost(chinovnik):
        if chinovnik in cost:
            return cost[chinovnik]

        idx = chinovnik - 1

        if not subs[idx]:
            cost[chinovnik] = bribes[idx][0]
            chosen_set[chinovnik] = 0
            return cost[chinovnik]

        subs_cost = {}

        for sub in subs[idx]:
            subs_cost[sub] = calculate_cost(sub)

        min_total = float('inf')
        best_set = -1

        for j, visa_set in enumerate(visa_sets[idx]):
            total = bribes[idx][j]
            for req_sub in visa_set:
                if req_sub in subs_cost:
                    total += subs_cost[req_sub]
                else:
                    total = float('inf')
                    break

            if total < min_total:
                min_total = total
                best_set = j

        cost[chinovnik] = min_total
        chosen_set[chinovnik] = best_set
        return min_total

    def get_order(chinovnik, result):
        idx = chinovnik - 1
        if chosen_set[chinovnik] == -1:
            return

        visa_set = visa_sets[idx][chosen_set[chinovnik]]
        for sub in visa_set:
            get_order(sub, result)


        result.append(chinovnik)




    min_cost = calculate_cost(1)
    order = []
    get_order(1, order)


    return min_cost, order


subordinates = [
    [2,3],
    [4],
    [5],
    [],
    [6, 7, 8, 9],
    [10],
    [],
    [],
    [],
    [],
]
visa_sets = [
    [[2],[3],[2,3]],
    [[4]],
    [[5]],
    [[]],
    [[6], [7], [8], [6, 7]],
    [[10], [8], [1]],
    [[]], [[]], [[]], [[]],
]
bribes = [
    [10, 15, 25],
    [16],
    [9],
    [33],
    [4, 10, 15, 25],
    [10, 15, 25],
    [8],
    [9],
    [6],
    [4]
]



min_cost, order = solution(subordinates, bribes, visa_sets)

print(f"\nРезультат: cost={min_cost}, order={order}")








import generate_test_data as gtd

def solution(subs, bribes, visa_sets):
    cost = {}
    chosen_set = {}

    def calculate_cost(officer):
        if officer in cost:
            return cost[officer]


        idx = officer - 1

        if not subs[idx]:
            cost[officer] = bribes[idx][0]
            chosen_set[officer] = 0
            return cost[officer]

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

        cost[officer] = min_total
        chosen_set[officer] = best_set
        return min_total

    def get_order(officer, result):
        idx = officer - 1
        if chosen_set[officer] == -1:
            return

        visa_set = visa_sets[idx][chosen_set[officer]]
        for sub in visa_set:
            get_order(sub, result)


        result.append(officer)


    min_cost = calculate_cost(1)
    order = []
    get_order(1, order)


    return min_cost, order




subordinates, visa_sets, bribes = gtd.generate_officials_data(99)
gtd.print_generated_data(subordinates, visa_sets, bribes)

min_cost, order = solution(subordinates, bribes, visa_sets)

print(f"\nРезультат: cost={min_cost}, order={order}")








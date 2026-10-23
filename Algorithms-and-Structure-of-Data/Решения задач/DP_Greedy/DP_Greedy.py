items = [
    {"name": "A", "weight": 7, "value": 5},
    {"name": "B", "weight": 2, "value": 4},
    {"name": "C", "weight": 1, "value": 7},
    {"name": "D", "weight": 9, "value": 2}
]
MAX_WEIGHT = 15


def solve_dp(items, max_weight):
    n = len(items)
    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        current_item = items[i - 1]
        w = current_item["weight"]
        v = current_item["value"]

        for cap in range(max_weight + 1):
            if w <= cap:
                dp[i][cap] = max(dp[i - 1][cap], dp[i - 1][cap - w] + v)
            else:
                dp[i][cap] = dp[i - 1][cap]

    selected_items = []
    current_cap = max_weight

    for i in range(n, 0, -1):
        if dp[i][current_cap] != dp[i - 1][current_cap]:
            item = items[i - 1]
            selected_items.append(item["name"])
            current_cap -= item["weight"]

    return dp[n][max_weight], selected_items


def solve_greedy(items, max_weight):
    sorted_items = sorted(items, key=lambda x: x["value"] / x["weight"], reverse=True)

    total_value = 0
    total_weight = 0
    selected_items = []

    print("\n--- Жадный алгоритм ---")
    print(f"{'Предмет':<8} | {'Вес':<4} | {'Цена':<4} | {'Уд. цена':<10}")
    print("-" * 35)

    for item in sorted_items:
        ratio = item['value'] / item['weight']
        print(f"{item['name']:<8} | {item['weight']:<4} | {item['value']:<4} | {ratio:.2f}")

    print("-" * 35)

    for item in sorted_items:
        if total_weight + item["weight"] <= max_weight:
            selected_items.append(item["name"])
            total_weight += item["weight"]
            total_value += item["value"]

    return total_value, selected_items, total_weight


print("=" * 40)
print("РЕШЕНИЕ 1: Динамическое программирование")
print("=" * 40)
dp_value, dp_items = solve_dp(items, MAX_WEIGHT)
print(f"Максимальная стоимость: {dp_value}")
print(f"Выбранные предметы: {dp_items}")

print("\n" + "=" * 40)
print("РЕШЕНИЕ 2: Жадный алгоритм")
print("=" * 40)
greedy_value, greedy_items, greedy_weight = solve_greedy(items, MAX_WEIGHT)
print(f"Итоговый вес: {greedy_weight} (из {MAX_WEIGHT})")
print(f"Максимальная стоимость (жадно): {greedy_value}")
print(f"Выбранные предметы: {greedy_items}")
# Данные из задачи
# Масштабируем суммы (делим на 50 000), чтобы уменьшить размер таблицы DP
SCALE = 50000

projects = [
    {"name": "A", "cost": 600000, "profit": 170000},
    {"name": "B", "cost": 250000, "profit": 125000},
    {"name": "C", "cost": 750000, "profit": 200000},
    {"name": "D", "cost": 200000, "profit": 150000},
    {"name": "E", "cost": 250000, "profit": 90000},
    {"name": "F", "cost": 100000, "profit": 70000}
]

MAX_BUDGET = 1250000
max_capacity = MAX_BUDGET // SCALE
n = len(projects)

# Создаем таблицу DP (n+1 строк, max_capacity+1 столбцов), заполненную нулями
dp = [[0 for _ in range(max_capacity + 1)] for _ in range(n + 1)]

# Заполняем таблицу динамического программирования
for i in range(1, n + 1):
    p = projects[i - 1]
    cost_scaled = p["cost"] // SCALE
    profit = p["profit"]

    for w in range(max_capacity + 1):
        if cost_scaled <= w:
            # Максимум из: не берем проект ИЛИ берем проект + лучший результат с оставшимся бюджетом
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost_scaled] + profit)
        else:
            # Если стоимость проекта больше текущего доступного бюджета, мы не можем его взять
            dp[i][w] = dp[i - 1][w]

# Восстановление ответа (какие именно проекты выбраны)
selected_projects = []
current_capacity = max_capacity

# Идем по таблице снизу вверх
for i in range(n, 0, -1):
    # Если прибыль изменилась по сравнению с предыдущей строкой, значит проект был выбран
    if dp[i][current_capacity] != dp[i - 1][current_capacity]:
        p = projects[i - 1]
        selected_projects.append(p["name"])
        current_capacity -= (p["cost"] // SCALE)

# Разворачиваем список, так как шли с конца
selected_projects.reverse()

# Вывод результатов
print("=" * 40)
print("ОПТИМАЛЬНОЕ РЕШЕНИЕ")
print("=" * 40)
print(f"Максимально возможная прибыль: ${dp[n][max_capacity]:,}")
print(f"Выбранные проекты: {', '.join(selected_projects)}")

# Считаем итоговые затраты для проверки
total_cost = sum(p["cost"] for p in projects if p["name"] in selected_projects)
print(f"Общий объем инвестиций: ${total_cost:,} (из доступных ${MAX_BUDGET:,})")
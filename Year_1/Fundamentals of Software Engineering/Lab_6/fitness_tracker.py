import matplotlib.pyplot as plt
import numpy as np
import xml.etree.ElementTree as ET

def load_users_data() -> list[dict]:
    try:
        users_tree = ET.parse('users.xml')
        users = []
        for user_elem in users_tree.getroot().findall('user'):
            user = {
                'user_id': int(user_elem.find('user_id').text),
                'name': user_elem.find('name').text,
                'age': int(user_elem.find('age').text),
                'weight': int(user_elem.find('weight').text),
                'fitness_level': user_elem.find('fitness_level').text,
                'workouts': []
            }
            users.append(user)
        return users
    except FileNotFoundError:
        print("Файл не найден")
        return []

def load_workouts_data() -> list[dict]:
    try:
        workouts_tree = ET.parse('workouts.xml')
        workouts = []
        for workouts_elem in workouts_tree.getroot().findall('workout'):
            workout = {
                'workout_id': int(workouts_elem.find('workout_id').text),
                'user_id': int(workouts_elem.find('user_id').text),
                'date': workouts_elem.find('date').text,
                'type': workouts_elem.find('type').text,
                'duration': int(workouts_elem.find('duration').text),
                'distance': float(workouts_elem.find('distance').text),
                'calories': int(workouts_elem.find('calories').text),
                'avg_heart_rate': workouts_elem.find('avg_heart_rate').text,
                'intensity': workouts_elem.find('intensity').text,
            }
            workouts.append(workout)
        return workouts
    except FileNotFoundError:
        print("Файл не найден")
        return []


def get_stats(users_list: list[dict], workouts_stats: list[dict]):
    calories_burned, total_time, distance_covered = (0,0,0)
    for stats in workouts_stats:
        calories_burned += stats['calories']
        total_time += stats['duration']
        distance_covered += stats['distance']

    print(f'''
ОБЩАЯ СТАТИСТИКА
===========================
Всего тренировок: {workouts_stats[-1]['workout_id']}
Всего пользователей: {users_list[-1]['user_id']}
Сожжено калорий: {calories_burned}
Общее время: {total_time/60:.1f} часов
Пройдено дистанции: {distance_covered:.1f} км
    ''')

def update_workouts(users_list: list[dict], workouts_stats: list[dict]):
    for user in users_list:
        for workout in workouts_stats:
            if workout['user_id'] == user['user_id']:
                user['workouts'].append(workout)


def analyze_user_activity(users_list: list[dict], workouts_stats: list[dict]):
    update_workouts(users_list, workouts_stats)
    people_data = []

    for user in users_list:
        count_workouts = len(user['workouts'])
        calories_burned = 0
        total_time = 0
        for workout in user['workouts']:
            calories_burned += workout['calories']
            total_time += workout['duration']
        people_data.append({
            'name': user['name'],
            'total_time': total_time,
            'workouts': count_workouts,
            'calories': calories_burned,
            'level': user['fitness_level']
        })

    times = [p['total_time'] for p in people_data]
    counts = [p['workouts'] for p in people_data]
    calories = [p['calories'] for p in people_data]

    max_time, min_time = max(times), min(times)
    max_count, min_count = max(counts), min(counts)
    max_cal, min_cal = max(calories), min(calories)

    for p in people_data:
        norm_time = (p['total_time'] - min_time) / (max_time - min_time) * 100 if max_time != min_time else 50
        norm_count = (p['workouts'] - min_count) / (max_count - min_count) * 100 if max_count != min_count else 50
        norm_cal = (p['calories'] - min_cal) / (max_cal - min_cal) * 100 if max_cal != min_cal else 50

        p['score'] = norm_time * 0.4 + norm_cal * 0.4 + norm_count * 0.2

    ranked_people = sorted(people_data, key=lambda x: x['score'], reverse=True)

    print("ТОП-3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ:")
    for person in ranked_people[:3]:
        print(
f'''{person["name"]} ({person['level']}) 
 Рейтинг: {person['score']:.1f}
 Тренировок: {person['workouts']}
 Калорий: {person['calories']}
 Время: {(person['total_time']/60):.1f} часов
''')

    x = np.array([p['name'] for p in ranked_people])
    y = np.array([p['score'] for p in ranked_people])
    plt.figure(figsize=(9, 6))
    bars = plt.bar(x, y)
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2,
                 height + 0.5,
                 str(int(height)),
                 ha='center',
                 va='bottom',
                 fontsize=12)

    plt.xlabel('Пользователи')
    plt.ylabel('Счёт')
    plt.title('Активность пользователей (рейтинг)')
    plt.show()


def plot_calories_comparison_simple(users_list, workouts_stats):
    user_calories = {}

    for user in users_list:
        user_calories[user['name']] = {
            'calories': 0,
            'level': user['fitness_level']
        }


    for workout in workouts_stats:

        user = next((u for u in users_list if u['user_id'] == workout['user_id']), None)
        if user:
            user_calories[user['name']]['calories'] += workout['calories']


    data_for_chart = []
    for name, info in user_calories.items():
        data_for_chart.append({
            'name': name,
            'calories': info['calories'],
            'fitness_level': info['level']
        })


    data_for_chart.sort(key=lambda x: x['calories'], reverse=True)

    plt.figure(figsize=(12, 6))

    names = [item['name'] for item in data_for_chart]
    calories = [item['calories'] for item in data_for_chart]

    colors = []
    for item in data_for_chart:
        level = item['fitness_level'].lower()
        if 'нач' in level:
            colors.append('green')
        elif 'сред' in level:
            colors.append('orange')
        elif 'прод' in level:
            colors.append('red')
        else:
            colors.append('gray')

    bars = plt.bar(names, calories, color=colors, edgecolor='black')
    for bar, cal in zip(bars, calories):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 50,
                 f'{cal}', ha='center', va='bottom')

    plt.title('Сравнение пользователей по затраченным калориям')
    plt.xlabel('Пользователи')
    plt.ylabel('Калории')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



def analyze_workout_types(workouts_stats: list[dict]):
    type_stats = {}
    for workout in workouts_stats:
        workout_type = workout['type']
        if workout_type not in type_stats:
            type_stats[workout_type] = {
                'count': 1,
                'total_duration': workout['duration'],
                'total_calories': workout['calories'],
            }
        else:
            type_stats[workout_type]['count'] += 1
            type_stats[workout_type]['total_duration'] += workout['duration']
            type_stats[workout_type]['total_calories'] += workout['calories']

    total_workouts = len(workouts_stats)
    final_stats = {}

    for workout_type, stats in type_stats.items():
        count = stats['count']
        avg_calories = stats['total_calories'] / count
        avg_duration = stats['total_duration'] / count
        calories_per_minute = avg_calories / avg_duration if avg_duration != 0 else 0
        percentage = count / total_workouts * 100 if total_workouts != 0 else 0

        final_stats[workout_type] = {
            'count': count,
            'total_duration': stats['total_duration'],
            'total_calories': stats['total_calories'],
            'avg_duration': avg_duration,
            'avg_calories': avg_calories,
            'calories_per_minute': calories_per_minute,
            'percentage': percentage
        }

    print_statistics(final_stats)
    visualize_statistics(final_stats)

    return final_stats

def print_statistics(type_stats: dict[str, dict]) -> None:
    print("РАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК:")

    for workout_type, stats in type_stats.items():
        print(
f'''{workout_type.capitalize()}: {stats['count']} тренировок ({stats['percentage']:.1f}%)
Средняя длительность: {stats['avg_duration']:.1f} мин
Средние калории: {stats['avg_calories']:.1f} ккал
''')


def visualize_statistics(type_stats: dict[str, dict]) -> None:
    if not type_stats:
        print("NO DATA")
        return
    types = list(type_stats.keys())

    percentages = [stats['percentage'] for stats in type_stats.values()]
    calories_per_minute = [stats['calories_per_minute'] for stats in type_stats.values()]
    counts = [stats['count'] for stats in type_stats.values()]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    ax1.pie(percentages, labels=types, autopct='%1.1f%%', startangle=90)
    ax1.set_title('Распределение тренировок по типам', fontsize=14)
    ax1.axis('equal')

    bars = ax2.bar(types, calories_per_minute, color='skyblue')
    ax2.set_xlabel('Тип тренировки', fontsize=12)
    ax2.set_ylabel('Ккал в минуту', fontsize=12)
    ax2.set_title('Эффективность тренировок (ккал/минуту)', fontsize=14)
    for bar, value in zip(bars, calories_per_minute):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2,
                 height + 0.1,
                 f'{value:.2f}',
                 ha='center',
                 va='bottom',
                 fontsize=11)

    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    bars = plt.bar(types, counts, color='lightcoral')
    plt.xlabel('Тип тренировки', fontsize=12)
    plt.ylabel('Количество тренировок', fontsize=12)
    plt.title('Количество тренировок по типам', fontsize=14)

    for bar, count in zip(bars, counts):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2,
                 height + 0.5,
                 str(count),
                 ha='center',
                 va='bottom',
                 fontsize=11)

    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.show()

def find_user_by_name(users_list: list[dict], name: str):
    user = next((u for u in users_list if u['name'].lower() == name.lower()), None)
    return user

def find_user_workouts(users_list: list[dict], user_name: str) -> list[dict]:
    user = find_user_by_name(users_list, user_name)
    user_workouts = user['workouts']
    for w in user_workouts:
        print(f"id {w['workout_id']} >> Тип {w['type']} >> Продолжительность {w['duration']} мин >> Калории {w['calories']} калорий")
    return user_workouts

def analyze_user(users_list: list[dict], user_name: str):
    user = find_user_by_name(users_list, user_name)
    workouts = find_user_workouts(users_list, user_name)
    calories_burned = 0
    total_time = 0
    count_workouts = len(workouts)
    distance = 0
    type = {}
    for w in workouts:
        calories_burned += w['calories']
        total_time += w['duration']
        distance += w['distance']
        if w['type'] not in type:
            type[w['type']] = 1
        else:
            type[w['type']] += 1

    avg_calories = calories_burned / count_workouts
    type = max(type, key=lambda x: x[1])
    print(
f'''
ДЕТАЛЬНЫЙ АНАЛИЗ ДЛЯ ПОЛЬЗОВАТЕЛЯ: {user['name']}
===========================================
Возраст: {user['age']} лет, Вес: {user['weight']} кг
Уровень: {user['fitness_level']}
Тренировок: {count_workouts}
Сожжено калорий: {calories_burned}
Общее время: {total_time/60:.1f} часов
Пройдено дистанции: {distance:.1f} км
Средние калории за тренировку: {avg_calories:.0f}
Любимый тип тренировки: {type}
''')

users = load_users_data()
workouts = load_workouts_data()
get_stats(users, workouts)
analyze_workout_types(workouts)
analyze_user_activity(users, workouts)
find_user_workouts(users, "аННа")
analyze_user(users, "Борис")
plot_calories_comparison_simple(users, workouts)

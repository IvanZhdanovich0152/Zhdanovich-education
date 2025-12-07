import matplotlib.pyplot as plt
import numpy as np
import xml.etree.ElementTree as ET

from numpy.ma.core import append


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



def analyze_workout_types(workouts_stats: list[dict]):
    types = {}
    for workout in workouts_stats:
        if workout['type'] not in types:
            types[workout['type']] = [1, workout['duration'], workout['calories']]
        else:
            types[workout['type']][0] += 1
            types[workout['type']][1] += workout['duration']
            types[workout['type']][2] += workout['calories']
    print("РАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК:")
    y = []
    for type in types:
        types[type][1] /= types[type][0]
        types[type][2] /= types[type][0]
        y += (types[type][0]/workouts_stats[-1]['workout_id'])*100
        print(
f'''{type.capitalize()}: {types[type][0]} тренировок ({(types[type][0]/workouts_stats[-1]['workout_id'])*100:.1f}%)
 Средняя длительность: {int(types[type][1])} мин
 Средние калории: {int(types[type][2])} ккал
''')
    plt.pie(y, labels=types, autopct='%1.1f%%')
    plt.show()




def find_user_by_name(users_list: list[dict], name: str):
    user = next((u for u in users_list if u['name'].lower() == name.lower()), None)
    return user

def find_user_workouts(users_list: list[dict], user_name: str) -> list[dict]:
    user = find_user_by_name(users_list, user_name)
    user_workouts = user['workouts']
    return user_workouts



def analyze_user(users_list: list[dict], user_name: str):
    user = find_user_by_name(users_list, user_name)
    workouts = find_user_workouts(users_list, user_name)
    calories_burned = 0
    total_time = 0
    count_workouts = len(workouts)
    distance = 0
    avg_calories = 0
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


for w in find_user_workouts(users, "аННа"):
    print(f"{w['workout_id']} {w['type']} {w['duration']} {w['calories']}")


analyze_user(users, "Борис")




# user = next((u for u in users if u['name'].lower() == user_name.lower()), None)



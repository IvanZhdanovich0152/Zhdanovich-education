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
            user = {
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
            workouts.append(user)
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

users = load_users_data()
workouts = load_workouts_data()

get_stats(users, workouts)
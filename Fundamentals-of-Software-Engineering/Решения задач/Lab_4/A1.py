import random
import time

n = int(input("Введите кол-во примеров >>> "))

right_answer = 0
total_time = 0

for i in range(1,n+1):
    print(f"Вопрос {i}/{n}")
    a, b = random.randint(2, 9), random.randint(2, 9)

    while True:
        try:
            start_time = time.time()
            answer = int(input(f"{a} * {b} = "))
            time_elapsed = time.time() - start_time
            break
        except ValueError:
            print("Пожалуйста введите целое число!")


    total_time += time_elapsed


    if answer == a*b:
        print(f"Верно! (Время: {time_elapsed :.2f} сек) ")
        right_answer += 1
    else:
        print(f"Неверно! Правильно {a*b} (Время: {time_elapsed:.2f} сек) ")


print(f"\n{"=" * 50}\n"
      f"СТАТИСТИКА:\n"
      f"{"=" * 50}")


print(f"\nОбщее время: {total_time :.2f} сек\n"
      f"Среднее время на вопрос: {total_time / n :.2f} сек\n"
      f"Правильных ответов: {right_answer}/{n}\n"
      f"Процент правильных: {(right_answer*100)/n}%\n")



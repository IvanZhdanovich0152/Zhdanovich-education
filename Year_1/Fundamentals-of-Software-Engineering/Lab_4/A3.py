packets = input("Введите строку пакетов >>> ")

if not all(char in '01' for char in packets) or len(packets) < 5:
    print("Неверный ввод. Используйте только символы '0' и '1'! и длину более 5 символов")
else:
    list_packets = list(packets)
    all_pakets = len(list_packets)
    lost_packets = packets.count('0')
    len_loss = 1
    max_loss = 0
    msg = " "
    for i in range(all_pakets):
        if list_packets[i] == '0':
            if list_packets[i - 1] == '0':
                len_loss += 1
                if max_loss < len_loss:
                    max_loss = len_loss
            elif list_packets[i - 1] == '1':
                len_loss = 1


    percent_lost = (lost_packets/all_pakets)*100

    if 0 <= percent_lost <= 1:
        msg = "Отличное качество"
    elif 1 < percent_lost <= 5:
        msg = "Хорошее качество"
    elif 5 < percent_lost <= 10:
        msg = "Удовлетворительное качество"
    elif 10 < percent_lost <= 20:
        msg = "Хорошее качество"
    elif 20 < percent_lost:
        msg = "Критическое состояние сети"




    print(f"Общее кол-во пакетов: {all_pakets}")
    print(f"Кол-во потерянных пакетов: {lost_packets}")
    print(f"Длина самой длинной последовательности потерянных пакетов: {max_loss}")
    print(f"Процент потерь: {percent_lost:.2f}%")
    print(f"Качество связи: {msg}")





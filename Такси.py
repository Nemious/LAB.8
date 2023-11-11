tariffs = []  # список тарифов за 1 километр для каждого водителя
distances = []  # список километража от работы до дома для каждого сотрудника

# Ввод данных
N = int(input("Введите количество сотрудников: "))
for i in range(N):
    tariff = float(input(f"Введите тариф за 1 км для водителя {i+1}: "))
    tariffs.append(tariff)

for i in range(N):
    distance = float(input(f"Введите километраж от работы до дома для сотрудника {i+1}: "))
    distances.append(distance)

# Определение минимальных затрат на такси
total_cost = 0
assignments = []  # список назначений сотрудников на такси
for i in range(N):
    min_cost = float('inf')  # начальное значение минимальной стоимости поездки
    assigned_taxi = -1  # начальное значение номера такси
    for j in range(N):
        cost = tariffs[j] * distances[i]  # стоимость поездки для сотрудника i на такси j
        if cost < min_cost:  # если стоимость меньше минимальной
            min_cost = cost  # обновляем минимальную стоимость
            assigned_taxi = j  # обновляем номер такси
    total_cost += min_cost  # увеличиваем суммарные затраты
    assignments.append((i+1, assigned_taxi+1))  # добавляем назначение в список


# Вывод результатов
rubles = int(total_cost)  # округляем суммарные затраты до рублей
kopecks = int((total_cost - rubles) * 100)  # вычисляем копейки
print(f"{rubles} рублей {kopecks} копеек")  # выводим сумму в рублях и копейках

for assignment in assignments:
    print(assignment[1], end=' ')  # выводим номер такси, в которое должен сесть сотрудник
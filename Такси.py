def rubles_ending(number):
    last_digit = number % 10
    if (
        (number >= 11 and number <= 19)
        or last_digit == 0
        or (last_digit >= 5 and last_digit <= 9)
    ):
        return "рублей"
    elif last_digit == 1:
        return "рубль"
    else:
        return "рубля"


class Employee:
    def __init__(self):
        self.distance_to_home = 0
        self.taxi_tariff = 0
        self.taxi_number = 0


def main():
    # Ввод данных
    N = 0
    while N <= 1 or N >= 1000:
        N = int(input("Введите количество сотрудников (от 1 до 1000): "))
    employees = [Employee() for _ in range(N)]

    print("Введите расстояния в километрах для каждого сотрудника:")
    for i in range(N):
        employees[i].distance_to_home = int(input(f"Сотрудник {i + 1}: "))

    print("Введите тарифы в рублях за проезд одного километра для каждой машины такси:")
    for i in range(N):
        employees[i].taxi_tariff = int(input(f"Такси {i + 1}: "))
        employees[i].taxi_number = i + 1

    if employees:
        employees.sort(
            key=lambda emp: emp.taxi_tariff / emp.distance_to_home
        )

        print("\nРаспределение сотрудников по такси для минимальных затрат:")
        for i, emp in enumerate(employees):
            print(f"Сотрудник {i + 1} едет на такси {emp.taxi_number}")

        total_cost = sum(emp.distance_to_home * emp.taxi_tariff for emp in employees)

        print(f"\nОбщая стоимость: {int(total_cost)} {rubles_ending(int(total_cost))}")
        from num2words import num2words
        if total_cost % 10 == 1 and total_cost % 100 != 11:
            print(f"{int(total_cost)} рубль")
            word = num2words(int(total_cost), lang='ru')
            print(word, "рубль")
        elif total_cost % 10 in [2, 3, 4] and total_cost % 100 not in [12, 13, 14]:
            print(f"{int(total_cost)} рубля")
            word = num2words(int(total_cost), lang='ru')
            print(word, "рубля")
        else:
            print(f"{int(total_cost)} рублей")
            word = num2words(int(total_cost), lang='ru')
            print(word, "рублей")


if __name__ == "__main__":
    main()

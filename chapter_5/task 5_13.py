# Вправа по програмуванню 5-13
# Висота падіння


# Головна функція.
def main():
    # Розраховуємо і виводимо результати на екран.
    print("\nЧас\t\tВідстань падіння")
    print("--------------------------------")

    for time in range(1, 11):
        distance = falling_distance(time)
        print(time, "\t\t", format(distance, ".2f"))


# Функція розраховує і повертає відстань, яку пролетить тіло за проміжок часу.
def falling_distance(time):
    distance = 0.5 * 9.8 * time ** 2
    return distance


# Виклик головної функції.
main()

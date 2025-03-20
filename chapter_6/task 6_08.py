# Вправа по програмуванню 6-8
# Читання файлу з випадковими числами


# Головна функція.
def main():
    # Ініціалізація змінних.
    total = 0
    counter = 0

    # Відкриття файлу для читання.
    infile = open(r"chapter_6\data\random_numbers.txt")

    # Читання файлу. Підрахунок суми чисел та їх кількості.
    for line in infile:
        number = int(line)
        total += number
        counter += 1

    # Виводимо результати на екран.
    print(f"Сума чисел: {total}")
    print(f"Кількість значень: {counter}")

    # Закриття файлу.
    infile.close()


# Виклик головної функції.
main()

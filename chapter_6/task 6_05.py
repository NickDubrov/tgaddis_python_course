# Вправа по програмуванню 6-5
# Сума чисел


# Головна функція.
def main():
    # Ініціалізація накопичувальної змінної.
    total = 0

    # Відкриття файлу для читання.
    infile = open(r"chapter_6\data\numbers.txt")

    # Читання файлу та підрахунок суми чисел.
    for line in infile:
        number = float(line)
        total += number

    # Закриття файлу.
    infile.close()

    # Виводимо результати на екран.
    print(f"Сума чисел: {total}")


# Виклик головної функції.
main()

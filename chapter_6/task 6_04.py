# Вправа по програмуванню 6-4
# Лічильник значень


# Головна функція.
def main():
    # Ініціалізація змінних.
    counter = 0

    # Відкриття файлу для читання.
    infile = open(r"chapter_6\data\names.txt")

    # Первинне читання файлу.
    line = infile.readline()

    # Читання файлу та підрахунок кількості рядків.
    while line != '':
        counter += 1

        line = infile.readline()

    # Закриття файлу.
    infile.close()

    # Виводимо результати на екран.
    print(f"Кількість значень: {counter}")


# Виклик головної функції.
main()

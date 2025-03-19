# Вправа по програмуванню 6-2
# Виведення на екран верхньої частини файлу


# Головна функція.
def main():
    # Отримання назви файлу.
    filename = input("Назва файлу: ")

    # Відкриття файлу для читання.
    infile = open("chapter_6\\data\\" + filename)

    # Первинне читання файлу.
    line = infile.readline()
    i = 1

    # Читаємо файл та виводимо результати на екран.
    while line != '' and i <= 5:
        line = line.rstrip('\n')
        print(line)

        line = infile.readline()
        i += 1

    # Закриття файлу.
    infile.close()


# Виклик головної функції.
main()

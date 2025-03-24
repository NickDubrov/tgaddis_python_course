# Вправа по програмуванню 6-10b
# Рахунок у грі в гольф


# Головна функція.
def main():
    # Відкриття файлу для читання.
    infile = open(r"chapter_6\data\golf.txt")

    # Читання імені першого гравця.
    player = infile.readline()

    # Читання файлу.
    while player != '':
        # Читання кількості очків гравця.
        score = infile.readline()

        # Відсікання символу нової строки.
        player = player.rstrip('\n')

        # Виводимо результати на екран.
        print("Ім'я гравця:", player)
        print("Рахунок гравця:", score)

        # Читання наступного імені.
        player = infile.readline()

    # Закриття файлу.
    infile.close()


# Виклик головної функції.
main()

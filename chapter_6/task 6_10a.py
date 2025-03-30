# Вправа по програмуванню 6-10а
# Рахунок у грі в гольф


# Головна функція.
def main():
    # Отримання кількості гравців в турнірі.
    num_players = int(input("Кількість гравців: "))

    # Відкриття файлу для запису.
    outfile = open(r"chapter_6\data\golf.txt", 'w')

    # Отримання даних про гравця та запис їх до файлу.
    for i in range(num_players):
        player = input("\nІм'я гравця: ")
        score = input("Рахунок гравця: ")

        outfile.write(player + '\n')
        outfile.write(score + '\n')

    # Закриття файлу.
    outfile.close()


# Виклик головної функції.
main()

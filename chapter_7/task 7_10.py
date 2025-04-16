# Вправа по програмуванню 7-10
# Чемпіони Світової серії


# Головна функція.
def main():
    try:
        # Відкриття файлу для читання.
        infile = open(r"chapter_7\data\WorldSeriesWinners.txt")

        # Читання файлу та збереження його вмісту в список.
        winners = infile.readlines()

        # Закриття файлу.
        infile.close()

        # Відсікання символу нової строки.
        for i in range(len(winners)):
            winners[i] = winners[i].rstrip('\n')

        # Отримання назви команди.
        team = input("Введіть назву команди: ")

        # Виводимо результати на екран.
        show_result(team, winners)

    except IOError:
        print("Виникла помилка під час спроби прочитати файл")
    except IndexError:
        print("Помилка індексації")
    except Exception as error:
        print("Виникла помилка!")
        print(error)


# Функція перевіряє, чи вигравала команда Світову серію,
# та підраховує кількість її перемог.
def show_result(value, team_list):
    # Ініціалізація змінних.
    win_count = 0

    if value not in team_list:
        print(f"Команда {value} ніколи не вигравала Світову серію.")
    else:
        for item in team_list:
            if item == value:
                win_count += 1
        print(f"Команда {value} вигравала Світову серію {win_count} " +
              f"разів протягом періоду з 1903 по 2009 роки.")


# Виклик головної функції.
main()

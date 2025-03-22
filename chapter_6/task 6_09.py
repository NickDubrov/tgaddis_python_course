# Вправа по програмуванню 6-9
# Обробка винятків


# Головна функція.
def main():
    # Ініціалізація змінних.
    total = 0
    counter = 0

    try:
        # Відкриття файлу для читання.
        infile = open(r"chapter_6\data\numbers.txt")

        # Читання файлу. Підрахунок суми чисел та їх кількості.
        for line in infile:
            number = float(line)
            total += number
            counter += 1

        # Закриття файлу.
        infile.close()

        # Розрахунок середнього арифметичного прочитаних із файлу чисел.
        average = total / counter

        # Виводимо результати на екран.
        print(f"Середнє арифметичне чисел: {average:.2f}")

    except IOError:
        print("Виникла помилка під час спроби прочитати файл.")
    except ValueError:
        print("У файлі виявлено нечислові дані.")
    except:
        print("Виникла помилка.")


# Виклик головної функції.
main()

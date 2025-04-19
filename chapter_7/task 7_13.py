# Вправа по програмуванню 7-13
# Чарівна куля

import random


# Головна функція.
def main():
    try:
        # Відкриття файлу для читання.
        infile = open(r"chapter_7\data\8_ball_responses.txt")

        # Читання файлу та збереження його вмісту в список.
        answers = infile.readlines()

        # Закриття файлу.
        infile.close()

        # Відсікання символу нової строки.
        for i in range(len(answers)):
            answers[i] = answers[i].rstrip('\n')

        # Отримання питання від користувача.
        question = input(f"Введіть своє питання " +
                         f"або введіть '0', щоб вийти: ")

        while question != '0':
            # Виводимо результати на екран.
            print(random.choice(answers))

            # Отримання питання від користувача.
            question = input(f"\nВведіть своє питання " +
                             f"або введіть '0', щоб вийти: ")

    except IOError:
        print("Виникла помилка під час спроби прочитати файл")
    except IndexError:
        print("Помилка індексації")
    except Exception as error:
        print("Виникла помилка!")
        print(error)


# Виклик головної функції.
main()

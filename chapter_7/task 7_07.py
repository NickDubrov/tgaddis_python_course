# Вправа по програмуванню 7-7
# Іспит з отримання водійських прав


# Головна функція.
def main():
    # Ініціалізація змінних.
    correct_answers = 0
    incorrect_answers = 0

    # Ініціалізація порожнього списку.
    incorrect_questions = []

    # Ініціалізація списку з правильними відповідями.
    solution = ['A', 'C', 'A', 'A', 'D',
                'B', 'C', 'A', 'C', 'B',
                'A', 'D', 'C', 'A', 'D',
                'C', 'B', 'B', 'D', 'A']

    try:
        # Відкриття файлу для читання.
        infile = open(r"chapter_7\data\student_solution.txt")

        # Читання файлу та збереження його вмісту в список.
        student_solutions = infile.readlines()

        # Закриття файлу.
        infile.close()

        for i in range(len(student_solutions)):
            # Відсікання символу нової строки.
            student_solutions[i] = student_solutions[i].rstrip('\n')

            # Порівняння відповідей студента з правильними відповідями
            # та оновлення змінних.
            if student_solutions[i] == solution[i]:
                correct_answers += 1
            else:
                incorrect_answers += 1
                incorrect_questions.append(str(i + 1))

        # Виводимо результати на екран.
        show_result(correct_answers)
        print(f"Кількість правильних відповідей: {correct_answers}")
        print(f"Кількість неправильних відповідей: {incorrect_answers}")
        show_incorrect_answers(incorrect_answers, incorrect_questions)

    except IOError:
        print("Виникла помилка під час спроби прочитати файл")
    except IndexError:
        print("Помилка індексації")
    except Exception as error:
        print(f"Виникла помилка!")
        print(error)


# Функція показує результат іспиту.
def show_result(correct_answers):
    if correct_answers >= 15:
        print("Вітаємо, ви склали іспит!")
    else:
        print("На жаль, ви не склали іспит. Спробуйте ще раз!")


# Функція показує номери питань, на які було дано неправильні відповіді.
def show_incorrect_answers(incorrect_answers, incorrect_questions):
    # Перевірка, чи було дано студентом неправильні відповіді.
    if incorrect_answers > 0:
        # Показати номери питань, на які було дано неправильні відповіді.
        print("Номери питань, на які було дано неправильні відповіді: ", end='')
        for i in range(len(incorrect_questions)):
            print(incorrect_questions[i], end='')
            if (i + 1) < incorrect_answers:
                print(', ', end='')


# Виклик головної функції.
main()

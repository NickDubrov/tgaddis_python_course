# Вправа по програмуванню 7-8
# Пошук імені


# Головна функція.
def main():
    try:
        # Відкриття файлів для читання.
        boys_infile = open(r"chapter_7\data\BoyNames.txt")
        girls_infile = open(r"chapter_7\data\GirlNames.txt")

        # Читання файлів та збереження їх вмісту в списки.
        popular_boys_names = boys_infile.readlines()
        popular_girls_names = girls_infile.readlines()

        # Закриття файлів.
        boys_infile.close()
        girls_infile.close()

        # Відсікання символу нової строки.
        for i in range(len(popular_boys_names)):
            popular_boys_names[i] = popular_boys_names[i].rstrip('\n')

        for i in range(len(popular_girls_names)):
            popular_girls_names[i] = popular_girls_names[i].rstrip('\n')

        # Отримання чоловічого імені від користувача.
        boy = input(f"Введіть чоловіче ім'я або введіть '0', щоб пропустити: ")

        # Отримання жіночого імені від користувача.
        girl = input(f"Введіть жіноче ім'я або введіть '0', щоб пропустити: ")

        # Виводимо результати на екран.
        show_result(boy, "чоловіче", popular_boys_names)
        show_result(girl, "жіноче", popular_girls_names)

    except IOError:
        print("Виникла помилка під час спроби прочитати файл")
    except IndexError:
        print("Помилка індексації")
    except Exception as error:
        print(f"Виникла помилка!")
        print(error)


# Функція перевіряє наявність введеного імені в списку популярних імен
# та виводить результати на екран.
def show_result(value, gender, name_list):
    value = value.capitalize()
    if value == '0':
        print(f"Ви вирішили не вводити {gender} ім'я.")
    elif value in name_list:
        print(f"{gender.capitalize()} ім'я {value} входить " +
              f"до списку популярних імен.")
    else:
        print(f"{gender.capitalize()} ім'я {value} не входить " +
              f"до списку популярних імен.")


# Виклик головної функції.
main()

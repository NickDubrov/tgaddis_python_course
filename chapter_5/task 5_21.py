# Вправа по програмуванню 5-21
# Гра "Камінь, ножиці, папір"

import random


# Головна функція.
def main():
    # Ініціалізація змінних.
    score1 = 0
    score2 = 0
    is_running = True

    # Головний цикл гри.
    while is_running:
        # Виведення на екран меню-підказки.
        show_menu()

        # Отримання відповіді від користувача і перевірка коректності значення.
        user_choice = get_user_choice()

        # Робочий цикл гри.
        while user_choice != 4:
            # Отримання випадкового числа для імітації вибору комп'ютера.
            pc_choice = random.randint(1, 3)

            # Виведення на екран відповідних значень.
            print(f"Гравець: {determine_value(user_choice)}")
            print(f"Комп'ютер: {determine_value(pc_choice)}")

            # Виведення на екран результату раунду.
            score1, score2 = show_result(
                user_choice, pc_choice, score1, score2)
            print(f"Рахунок: {score1}-{score2}")

            # Виведення на екран результату гри.
            if score1 == 5:
                print("\nВітаю! Ви перемогли в цій грі.")
                break
            elif score2 == 5:
                print("\nНажаль, Ви програли! Спробуйте ще раз!")
                break

            user_choice = get_user_choice()

        # Переведення прапора стану гри.
        is_running = False

        # Пропозиція зіграти знову.
        score1, score2, is_running = get_answer()


# Функція отримує відповідь від користувача і перевіряє коректність значення.
def get_user_choice():
    user_choice = int(input("\nВибір користувача: "))
    while user_choice < 1 or user_choice > 4:
        print("Некоректне значення! Введіть число від 1 до 4")
        user_choice = int(input("\nВибір користувача: "))
    return user_choice


# Функція пропонує користувачу зіграти знову і перевіряє його відповідь.
def get_answer(score1=0, score2=0):
    answer = input("Бажаєте зіграти знову (y/n)?: ")
    if answer == "n" or answer == "N":
        is_running = False
    else:
        is_running = True
    return score1, score2, is_running


# Функція повертає відповідне значення у рядковому форматі.
def determine_value(value):
    if value == 1:
        return "Камінь"
    elif value == 2:
        return "Ножиці"
    elif value == 3:
        return "Папір"


# Функція виводить на екран меню-підказку.
def show_menu():
    print("\n- - - - - - - - - - - - - - - - - -")
    print("Меню:")
    print("Натисніть '1', щоб вибрати 'Камінь'")
    print("Натисніть '2', щоб вибрати 'Ножиці'")
    print("Натисніть '3', щоб вибрати 'Папір'")
    print("Натисніть '4', щоб вибрати 'Вихід'")
    print("- - - - - - - - - - - - - - - - - -")


# Функція виводить на екран результат раунду.
def show_result(user, pc, user_score, pc_score):
    if (user == 1 and pc == 2) or (user == 2 and pc == 3) or (user == 3 and pc == 1):
        print("В раунді переміг гравець.")
        user_score += 1
    elif (user == 1 and pc == 3) or (user == 2 and pc == 1) or (user == 3 and pc == 2):
        print("В раунді переміг комп'ютер.")
        pc_score += 1
    else:
        print("Нічия! Треба переграти!")
    return user_score, pc_score


# Виклик головної функції.
main()

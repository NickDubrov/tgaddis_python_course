# Вправа по програмуванню 5-20
# Вгадування випадкового числа

import random


# Головна функція.
def main():
    # Ініціалізація змінних.
    attempt = 1
    is_running = True

    # Головний цикл гри.
    while is_running:
        # Отримання випадкового числа.
        number = get_random_number()

        # # Отримання числа від користувача і перевірка коректності значення.
        user_number = get_user_number()

        # Робочий цикл гри.
        while user_number != number:
            determine_number(number, user_number)
            attempt += 1
            user_number = get_user_number()

        # Переведення прапора стану гри.
        is_running = False

        # Виводимо на екран результати розрахунків.
        print(f"Вітаю! Ви вгадали правильне число. Ним було число {number}.")
        print(f"Ви відгадали його з {attempt}-ої спроби.")

        # Пропозиція зіграти знову.
        attempt, is_running = get_answer()


# Функція повертає випадкове число.
def get_random_number():
    number = random.randint(1, 100)
    return number


# Функція отримує число від користувача і перевіряє коректність значення.
def get_user_number():
    user_number = int(input("\nВідповідь користувача: "))
    while user_number < 1 or user_number > 100:
        print("Некоректне значення! Введіть число від 1 до 100")
        user_number = int(input("\nВідповідь користувача: "))
    return user_number


# Функція пропонує користувачу зіграти знову і перевіряє його відповідь.
def get_answer(attempt=1):
    user_answer = input("\nБажаєте зіграти знову (y/n)?: ")
    if user_answer == "y" or user_answer == "Y":
        is_running = True
    else:
        is_running = False
    return attempt, is_running


# Функція перевіряє чи вгадано число і виводить підказку на екран.
def determine_number(number, user_number):
    if user_number > number:
        print("Занадто багато. Спробуйте ще раз!")
    elif user_number < number:
        print("Занадто мало. Спробуйте ще раз!")


# Виклик головної функції.
main()

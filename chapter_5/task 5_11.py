# Вправа по програмуванню 5-11
# Математичний тест

import random


# Головна функція.
def main():
    # Отримання випадкових чисел.
    number1 = get_number()
    number2 = get_number()

    # Розрахунок суми чисел.
    correct_answer = calculate_sum(number1, number2)

    # Отримання відповіді користувача.
    user_answer = get_answer()

    # Порівняння відповідей і виведення результату на екран.
    compare_answers(correct_answer, user_answer)


# Функція повертає випадкове число.
def get_number():
    number = random.randint(1, 1000)
    return number


# Функція повертає відповідь користувача.
def get_answer():
    answer = int(input("\nВідповідь користувача: "))
    return answer


# Функція розраховує і повертає суму чисел.
def calculate_sum(number1, number2):
    print(format(number1, "5"))
    print("+", format(number2, "3"))
    return number1 + number2


# Функція повідомляє чи є відповідь користувача вірною.
def compare_answers(correct_answer, user_answer):
    if correct_answer == user_answer:
        print("Вітаю! Відповідь вірна.")
    else:
        print(f"На жаль, відповідь невірна. " +
              f"Правильна відповідь: {correct_answer}")


# Виклик головної функції.
main()

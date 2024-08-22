# Вправа по програмуванню 5-16
# Лічильник парних/непарних чисел

import random


# Головна функція.
def main():
    # Ініціалізація змінних.
    even = 0
    odd = 0

    # Отримання випадкових чисел.
    for i in range(100):
        number = get_random_number()

        # Перевірка числа на парність.
        if is_even(number):
            even += 1
        else:
            odd += 1

    # Виводимо на екран результати розрахунків.
    print(f"Серед отриманих випадкових чисел {even} були парними, " +
          f"а решта {odd} були непарними.")


# Функція повертає випадкове число.
def get_random_number():
    number = random.randint(1, 1000)
    return number


# Функція перевіряє чи є число парним.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


# Виклик головної функції.
main()

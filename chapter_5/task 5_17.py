# Вправа по програмуванню 5-17
# Прості числа

import math


# Головна функція.
def main():
    # Отримання числа від користувача.
    number = int(input("Введіть число: "))

    # Перевірка чи є число простим і виведення результату на екран.
    if is_prime(number):
        print(f"Число {number} є простим.")
    else:
        print(f"Число {number} не є простим.")


# Функція перевіряє чи є число простим.
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(number) + 1), 2):
            if number % i == 0:
                return False
        return True
    return False


# Виклик головної функції.
main()

# Вправа по програмуванню 7-12
# Генерація простого числа

import math


# Головна функція.
def main():
    # Ініціалізація порожнього списку.
    numbers = []

    # Отримання числа від користувача.
    number = int(input("Введіть ціле число більше 1: "))

    # Заповнення списку цілими числами.
    for i in range(2, number + 1):
        numbers.append(i)

    # Перевірка чи є число простим і виведення результату на екран.
    print("\nПрості числа, які менші або рівні введеному числу:")
    for number in numbers:
        if is_prime(number):
            print(number, end=' ')
    print()


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

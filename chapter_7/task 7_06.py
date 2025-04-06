# Вправа по програмуванню 7-6
# Більше числа n

import random


# Головна функція.
def main():
    # Ініціалізація списку.
    numbers = [0] * 10

    # Отримання випадкового числа n.
    number = random.randint(25, 75)

    # Отримання випадкових чисел і присвоєння їх елементам списку.
    for i in range(10):
        numbers[i] = random.randint(1, 100)

    # Виводимо результати на екран.
    print(f"Число n: {number}")
    print(f"Список чисел: \n{numbers}")
    print(f"Список чисел, більших за число {number}:")
    show_numbers_larger_than_n(number, numbers)


# Функція показує всі числа у списку, які більше за число n.
def show_numbers_larger_than_n(n, number_list):
    # Ініціалізація порожнього списку.
    larger_than_n = []

    # Порівняння значень у списку з числом n.
    # Якщо значення більше числа n, то добавити його до списку.
    for i in number_list:
        if i > n:
            larger_than_n.append(i)

    # Виводимо результати на екран.
    print(larger_than_n)


# Виклик головної функції.
main()

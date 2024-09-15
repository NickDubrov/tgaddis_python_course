# Вправа по програмуванню 5-18
# Список простих чисел

import math


# Головна функція.
def main():
    # Перевірка чи є число простим і виведення результату на екран.
    print("Усі прості числа в інтервалі від 1 до 100:")
    for number in range(1, 100):
        if is_prime(number):
            if number < 97:
                print(number, end=', ')
            else:
                print(number)


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

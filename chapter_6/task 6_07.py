# Вправа по програмуванню 6-7
# Запис файлу з випадковими числами

import random


# Головна функція.
def main():
    # Отримання кількості випадкових чисел, що будуть записані до файлу.
    nums_amount = int(input("Кількість випадкових чисел: "))

    # Отримання назви файлу.
    filename = input("Назва файлу: ")

    # Відкриття файлу для запису.
    outfile = open("chapter_6\\data\\" + filename, 'w')

    # Запис випадкових чисел до файлу.
    for i in range(nums_amount):
        num = random.randint(1, 500)
        outfile.write(str(num) + '\n')

    # Закриття файлу.
    outfile.close()


# Виклик головної функції.
main()

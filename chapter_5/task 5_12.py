# Вправа по програмуванню 5-12
# Максимальне значення


# Головна функція.
def main():
    # Отримання чисел від користувача.
    number1 = int(input("Введіть перше число: "))
    number2 = int(input("Введіть друге число: "))

    # Визначення більшого з чисел.
    max_number = show_max_number(number1, number2)

    # Виводимо на екран результати розрахунків.
    print(f"\nМаксимальне число з введених: {max_number}")


# Функція порівнює числа і повертає більше з них.
def show_max_number(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2


# Виклик головної функції.
main()

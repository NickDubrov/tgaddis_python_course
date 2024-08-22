# Вправа по програмуванню 5-6
# Калорії від жирів та вуглеводів

# Іменовані константи.
CALORIES_FROM_FAT = 9
CALORIES_FROM_CARBS = 4


# Головна функція.
def main():
    # Отримання кількості спожитих жирів.
    grams_fat = float(input("Кількість спожитих жирів в грамах: "))

    # Отримання кількості спожитих вуглеводів.
    grams_carbs = float(input("Кількість спожитих вуглеводів в грамах: "))

    # Розрахунок кількості калорій від споживання жирів та вуглеводів.
    calories_fat, calories_carbs = calculate_calories(grams_fat, grams_carbs)

    # Виводимо на екран результати розрахунків.
    print(f"\nКалорій від споживання жирів: {calories_fat:.2f}")
    print(f"Калорій від споживання вуглеводів: {calories_carbs:.2f}")


# Функція розраховує і повертає кількість калорій
# від споживання жирів та вуглеводів.
def calculate_calories(grams_fat, grams_carbs):
    calories_fat = grams_fat * CALORIES_FROM_FAT
    calories_carbs = grams_carbs * CALORIES_FROM_CARBS
    return calories_fat, calories_carbs


# Виклик головної функції.
main()

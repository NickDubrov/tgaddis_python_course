# Вправа по програмуванню 5-3
# Вартість страховки

# Іменовані константи.
INSURANCE_PERCENT = 0.8


# Головна функція.
def main():
    # Отримання загальної вартості будівлі.
    building_cost = float(input("Вартість будівлі в $: "))

    # Розрахунок мінімальної суми страхування нерухомості.
    min_insurance = calculate_insurance(building_cost)

    # Виводимо на екран результати розрахунків.
    print(f"Рекомендована сума страхування нерухомості "
          f"не повинна бути менша, ніж ${min_insurance:,.2f}")


# Функція розраховує і повертає мінімальну суму страхування нерухомості.
def calculate_insurance(building_cost):
    return building_cost * INSURANCE_PERCENT


# Виклик головної функції.
main()

# Вправа по програмуванню 5-5
# Податок на нерухоме майно

# Іменовані константи.
ASSESS_PERCENT = 0.6
PROPERTY_TAX_PERCENT = 0.0072


# Головна функція.
def main():
    # Отримання фактичної вартості нерухомого майна.
    actual_value = float(input("Фактична вартість нерухомого майна: "))

    # Розрахунок оціночної вартості.
    assessed_value = calculate_assessed_value(actual_value)

    # Розрахунок податку на нерухоме майно.
    property_tax = calculate_property_tax(assessed_value)

    # Виводимо на екран результати розрахунків.
    print(f"Оціночна вартість: {assessed_value:,.2f}")
    print(f"Податок на нерухоме майно: {property_tax:,.2f}")


# Функція розраховує і повертає оціночну вартість.
def calculate_assessed_value(actual_value):
    return actual_value * ASSESS_PERCENT


# Функція розраховує і повертає податок на нерухоме майно.
def calculate_property_tax(assessed_value):
    return assessed_value * PROPERTY_TAX_PERCENT


# Виклик головної функції.
main()

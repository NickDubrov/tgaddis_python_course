# Вправа по програмуванню 5-9
# Місячний податок з продажу

# Іменовані константи.
FED_TAX_RATE = 0.05
MUN_TAX_RATE = 0.025


# Головна функція.
def main():
    # Отримання обсягу продажів.
    sales = float(input("Загальний обсяг продажів за місяць: "))

    # Розрахунок федерального податку.
    fed_tax = calculate_fed_tax(sales)

    # Розрахунок муніципального податку.
    mun_tax = calculate_mun_tax(sales)

    # Розрахунок загального податку.
    total_tax = calculate_total_tax(fed_tax, mun_tax)

    # Виводимо на екран результати розрахунків.
    print(f"\nФедеральний податок: {fed_tax:,.2f}")
    print(f"Муніципальний податок: {mun_tax:,.2f}")
    print(f"Загальний податок: {total_tax:,.2f}")


# Функція розраховує і повертає федеральний податок.
def calculate_fed_tax(sales):
    return sales * FED_TAX_RATE


# Функція розраховує і повертає муніципальний податок.
def calculate_mun_tax(sales):
    return sales * MUN_TAX_RATE


# Функція розраховує і повертає загальний податок.
def calculate_total_tax(fed_tax, mun_tax):
    return fed_tax + mun_tax


# Виклик головної функції.
main()

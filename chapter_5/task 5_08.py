# Вправа по програмуванню 5-8
# Оцінювач малярських робіт

# Іменовані константи.
METERS_PER_CAN = 10
METERS_PER_HOUR = 1.25
HOURLY_RATE = 80


# Головна функція.
def main():
    # Отримання площі поверхні.
    surface_area = float(input("Площа поверхні під фарбування: "))

    # Отримання ціни ємності фарби.
    price_paint = float(input("Ціна 5-літрової ємності фарби: "))

    # Розрахунок необхідної кількості банок з фарбою.
    paint_cans = calculate_paint_cans(surface_area)

    # Розрахунок необхідної кількості робочих годин.
    working_hours = calculate_working_hours(surface_area)

    # Розрахунок витрат на фарбу.
    paint_cost = calculate_paint_cost(price_paint, paint_cans)

    # Розрахунок суми, сплаченої за роботу.
    working_cost = calculate_working_cost(working_hours)

    # Розрахунок загальної вартості малярських робіт.
    total_cost = calculate_total_cost(paint_cost, working_cost)

    # Виводимо на екран результати розрахунків.
    print(f"\nКількість ємностей із фарбою: {paint_cans}")
    print(f"Кількість робочих годин: {working_hours}")
    print(f"Витрати на фарбу: {paint_cost:,.2f}")
    print(f"Вартість роботи: {working_cost:,.2f}")
    print(f"Загальна вартість: {total_cost:,.2f}")


# Функція розраховує і повертає необхідну кількість банок з фарбою.
def calculate_paint_cans(surface_area):
    paint_cans = surface_area // METERS_PER_CAN
    if (surface_area % METERS_PER_CAN) != 0:
        paint_cans += 1
    return paint_cans


# Функція розраховує і повертає необхідну кількість робочих годин.
def calculate_working_hours(surface_area):
    working_hours = surface_area // METERS_PER_HOUR
    if (surface_area % METERS_PER_HOUR) != 0:
        working_hours += 1
    return working_hours


# Функція розраховує і повертає суму, сплачену за фарбу.
def calculate_paint_cost(price_paint, paint_cans):
    return price_paint * paint_cans


# Функція розраховує і повертає суму, сплачену за роботу.
def calculate_working_cost(working_hours):
    return working_hours * HOURLY_RATE


# Функція розраховує і повертає загальну вартість малярських робіт.
def calculate_total_cost(paint_cost, working_cost):
    return paint_cost + working_cost


# Виклик головної функції.
main()

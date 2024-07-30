# Вправа по програмуванню 5-4
# Витрати на автомобіль


# Головна функція.
def main():
    # Отримання витрат на обслуговування автомобіля.
    loan = float(input("Платіж по кредиту: "))
    insurance = float(input("Платіж по страховці: "))
    fuel = float(input("Витрати на пальне: "))
    oil = float(input("Витрати на машинне мастило: "))
    tires = float(input("Витрати на колеса: "))
    maintenance = float(input("Витрати на техобслуговування: "))

    # Розрахунок загальної суми витрат за місяць.
    total_month = calculate_monthly_expenses(
        loan, insurance, fuel, oil, tires, maintenance)

    # Розрахунок загальної суми витрат за рік.
    total_year = calculate_annual_expenses(total_month)

    # Виводимо на екран результати розрахунків.
    print(f"\nЗагальні місячні витрати: {total_month:,.2f}")
    print(f"Загальні річні витрати: {total_year:,.2f}")


# Функція розраховує і повертає загальну суму витрат за місяць.
def calculate_monthly_expenses(loan, insurance, fuel, oil, tires, maintenance):
    return loan + insurance + fuel + oil + tires + maintenance


# Функція розраховує і повертає загальну суму витрат за рік.
def calculate_annual_expenses(total_month):
    return total_month * 12


# Виклик головної функції.
main()

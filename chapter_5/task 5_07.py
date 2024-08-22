# Вправа по програмуванню 5-7
# Місця на стадіоні

# Іменовані константи.
TICKET_PRICE_CLASS_A = 20
TICKET_PRICE_CLASS_B = 15
TICKET_PRICE_CLASS_C = 10


# Головна функція.
def main():
    # Отримання кількості проданих місць класу А.
    tickets_a = int(input("Кількість проданих місць класу А: "))

    # Отримання кількості проданих місць класу B.
    tickets_b = int(input("Кількість проданих місць класу B: "))

    # Отримання кількості проданих місць класу C.
    tickets_c = int(input("Кількість проданих місць класу C: "))

    # Розрахунок загальної суми прибутку з продажу квитків.
    total_income = calculate_total_income(tickets_a, tickets_b, tickets_c)

    # Виводимо на екран результати розрахунків.
    print(f"Загальний дохід з продажу квитків: {total_income:,.2f}")


# Функція розраховує і повертає загальну суму прибутку з продажу квитків.
def calculate_total_income(tickets_a, tickets_b, tickets_c):
    tickets_a_income = tickets_a * TICKET_PRICE_CLASS_A
    tickets_b_income = tickets_b * TICKET_PRICE_CLASS_B
    tickets_c_income = tickets_c * TICKET_PRICE_CLASS_C
    return tickets_a_income + tickets_b_income + tickets_c_income


# Виклик головної функції.
main()

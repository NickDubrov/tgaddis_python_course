# Вправа по програмуванню 3-12
# Продаж програмного забезпечення

# Іменовані константи.
RETAIL_PRICE = 99

# Отримання кількості придбаних пакетів програмного забезпечення.
quantity = int(input("Кількість придбаних пакетів: "))

# Визначення знижки
if quantity < 10:
    discount_rate = 0
elif quantity < 20:
    discount_rate = 0.10
elif quantity < 50:
    discount_rate = 0.20
elif quantity < 100:
    discount_rate = 0.30
elif quantity >= 100:
    discount_rate = 0.40

# Розрахунок загальної суми без урахування знижки.
full_price = quantity * RETAIL_PRICE

# Розрахунок суми знижки.
discount = full_price * discount_rate

# Розрахунок загальної суми з урахуванням знижки.
total_price = full_price - discount

# Виводимо результати на екран.
print(f"Сума знижки: {discount:.2f}")
print(f"Сума з урахуванням знижки: {total_price:.2f}")

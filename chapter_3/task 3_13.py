# Вправа по програмуванню 3-13
# Вартість доставки

# Отримання ваги посилки.
weight = float(input("Вага посилки в грамах: "))

# Визначення тарифу доставки.
if weight <= 200:
    delivery_rate = 90
elif weight <= 600:
    delivery_rate = 120
elif weight <= 1000:
    delivery_rate = 150
elif weight > 1000:
    delivery_rate = 180

# Розрахунок загальної вартості доставки.
delivery_fee = delivery_rate * weight / 1000

# Виводимо результати на екран.
print(f"Доставка посилки вагою {weight/1000:.2f} кг " +
      f"становить {delivery_fee:,.2f} грн.")

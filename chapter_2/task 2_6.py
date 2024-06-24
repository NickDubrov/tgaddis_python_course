# Вправа по програмуванню 2-6
# Податок з продажу

# Величини федерального та регіонального податків з продажу.
FED_TAX_RATE = 0.05
REG_TAX_RATE = 0.025

# Отримання величини суми покупки.
purchase_amount = float(input("Введіть величину суми покупки: "))

# Розрахунок федерального податку з продажу.
fed_tax = purchase_amount * FED_TAX_RATE

# Розрахунок регіонального податку з продажу.
reg_tax = purchase_amount * REG_TAX_RATE

# Розрахунок загального податку з продажу
total_tax = fed_tax + reg_tax

# Розрахунок загальної суми продажу
total_amount = purchase_amount + total_tax

print(f"\nСума покупки: {purchase_amount:,.2f}")
print(f"Федеральний податок з продажу: {fed_tax:,.2f}")
print(f"Регіональний податок з продажу: {reg_tax:,.2f}")
print(f"Загальний податок з продажу: {total_tax:,.2f}")
print(f"Загальна сума продажу: {total_amount:,.2f}")

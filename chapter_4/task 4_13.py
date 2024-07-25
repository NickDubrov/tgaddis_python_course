# Вправа по програмуванню 4-13
# Зростання популяції

# Ініціалізація змінних.
start_population = 0
daily_increase = 0
days = 0

# Отримання початкової кількості організмів.
while start_population <= 0:
    start_population = int(input("Початкова кількість організмів: "))

# Отримання відсотка середньодобового збільшення популяції.
while daily_increase <= 0:
    daily_increase = float(input("Середньодобовий приріст організмів у %: "))

# Отримання кількості днів.
while days <= 0:
    days = int(input("Кількість днів: "))

# Визначаємо, чи було введено значення середньодобового
# збільшення популяції як ціле число.
if daily_increase >= 1:
    daily_increase /= 100

# Розраховуємо і виводимо результати на екран.
print("День\t\tПопуляція")
print("-------------------------")

for day in range(days):
    if day > 0:
        start_population += (start_population * daily_increase)
    print((day + 1), '\t\t', format(start_population, ",.0f"))

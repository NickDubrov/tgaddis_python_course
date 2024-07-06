# Вправа по програмуванню 3-5
# Маса та вага

# Іменовані константи.
MASS_MULTIPLIER = 9.8
TOO_HEAVY = 500
TOO_LIGHT = 100

# Отримання маси об'єкта.
mass = float(input("Маса об'єкта в кілограмах: "))

# Розрахунок ваги об'єкта.
weight = mass * MASS_MULTIPLIER

# Виводимо результати розрахунків на екран.
print(f"Вага об'єкта становить {weight:.2f} ньютонів.")

if weight > TOO_HEAVY:
    print(f"Об'єкт занадто важкий. Він важить більше {TOO_HEAVY} ньютонів.")
elif weight < TOO_LIGHT:
    print(f"Об'єкт занадто легкий. Він важить менше {TOO_LIGHT} ньютонів.")

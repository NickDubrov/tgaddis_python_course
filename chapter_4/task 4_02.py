# Вправа по програмуванню 4-2
# Спалені калорії

# Іменовані константи.
CALORIES_PER_MINUTE = 4.2

# Розраховуємо і виводимо результати на екран.
print("Хвилини\t\tСпалені калоріЇ")
print("-------------------------------")

for minutes in range(5, 31, 5):
    calories = minutes * CALORIES_PER_MINUTE
    print(minutes, "\t\t", calories)

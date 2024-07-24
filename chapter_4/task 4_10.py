# Вправа по програмуванню 4-10
# Зростання плати за навчання

# Іменовані константи.
INCREASE_PER_YEAR = 0.03
STARTING_AMOUNT = 22000

# Розрахунок річної суми оплати за навчання.
tuition_per_year = 2 * STARTING_AMOUNT

# Розраховуємо і виводимо результати на екран.
print("Рік\t\tПланова вартість навчання")
print("-----------------------------------------")

for year in range(5):
    tuition_per_year += (tuition_per_year * INCREASE_PER_YEAR)
    print((year + 1), "\t\t", format(tuition_per_year, ".2f"))

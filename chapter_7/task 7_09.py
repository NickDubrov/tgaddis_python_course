# Вправа по програмуванню 7-9
# Дані про населення

# Іменовані константи.
STARTING_YEAR = 1950


# Головна функція.
def main():
    # Ініціалізація порожнього списку.
    annual_change = []

    try:
        # Відкриття файлу для читання.
        infile = open(r"chapter_7\data\USPopulation.txt")

        # Читання файлу та збереження його вмісту в список.
        annual_population = infile.readlines()

        # Закриття файлу.
        infile.close()

        # Перетворення всіх строкових значень в числа.
        for i in range(len(annual_population)):
            annual_population[i] = float(annual_population[i])

        # Розрахунок щорічних змін чисельності населення.
        for i in range(1, len(annual_population)):
            change = annual_population[i] - annual_population[i - 1]
            annual_change.append(change)

        # Розрахунок середньорічної зміни чисельності населення.
        total_change = sum(annual_change)
        average_change = total_change / len(annual_change)

        # Визначення року з найбільшим зростанням чисельності населення.
        max_change = max(annual_change)
        year_max_change = annual_change.index(max_change) + 1

        # Визначення року з найменшим зростанням чисельності населення.
        min_change = min(annual_change)
        year_min_change = annual_change.index(min_change) + 1

        # Виводимо результати на екран.
        print(f"Середньорічна зміна чисельності населення протягом " +
              f"зазначеного періоду часу: {average_change:,.2f}")
        print(f"Рік з найбільшим зростанням чисельності населення: " +
              f"{STARTING_YEAR + year_max_change}")
        print(f"Рік з найменшим зростанням чисельності населення: " +
              f"{STARTING_YEAR + year_min_change}")

    except IOError:
        print("Виникла помилка під час спроби прочитати файл")
    except IndexError:
        print("Помилка індексації")
    except Exception as error:
        print("Виникла помилка!")
        print(error)


# Виклик головної функції.
main()

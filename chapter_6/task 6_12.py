# Вправа по програмуванню 6-12
# Середня кількість кроків

# Іменовані константи.
JAN_DAYS = 31
FEB_DAYS = 28
MARCH_DAYS = 31
APRIL_DAYS = 30
MAY_DAYS = 31
JUNE_DAYS = 30
JULY_DAYS = 31
AUG_DAYS = 31
SEPT_DAYS = 30
OCT_DAYS = 31
NOV_DAYS = 30
DEC_DAYS = 31


# Головна функція.
def main():
    # Відкриття файлу для читання.
    infile = open(r"chapter_6\data\steps.txt")

    # Розраховуємо і виводимо результати на екран.
    print("Січень:")
    calculate_average(infile, JAN_DAYS)
    print("Лютий:")
    calculate_average(infile, FEB_DAYS)
    print("Березень:")
    calculate_average(infile, MARCH_DAYS)
    print("Квітень:")
    calculate_average(infile, APRIL_DAYS)
    print("Травень:")
    calculate_average(infile, MAY_DAYS)
    print("Червень:")
    calculate_average(infile, JUNE_DAYS)
    print("Липень:")
    calculate_average(infile, JULY_DAYS)
    print("Серпень:")
    calculate_average(infile, AUG_DAYS)
    print("Вересень:")
    calculate_average(infile, SEPT_DAYS)
    print("Жовтень:")
    calculate_average(infile, OCT_DAYS)
    print("Листопад:")
    calculate_average(infile, NOV_DAYS)
    print("Грудень:")
    calculate_average(infile, DEC_DAYS)

    # Закриття файлу.
    infile.close()


# Функція розраховує середню кількість кроків в день,
# зроблених протягом місяця і виводить результати на екран.
def calculate_average(infile, days):
    total = 0
    for day in range(days):
        total += int(infile.readline())
    average = total / days

    print(f"Кількість днів: {days}")
    print(f"Загальна кількість кроків: {total:,}")
    print(f"Середня кількість кроків в день: {round(average)}\n")


# Виклик головної функції.
main()

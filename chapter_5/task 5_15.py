# Вправа по програмуванню 5-15
# Середній бал та його рівень


# Головна функція.
def main():
    # Отримання оцінок від користувача.
    score1 = float(input("Введіть оцінку №1: "))
    score2 = float(input("Введіть оцінку №2: "))
    score3 = float(input("Введіть оцінку №3: "))
    score4 = float(input("Введіть оцінку №4: "))
    score5 = float(input("Введіть оцінку №5: "))

    # Розрахунок середнього балу.
    average = calculate_average(score1, score2, score3, score4, score5)

    # Виводимо на екран результати розрахунків.
    print("\nОцінка\t\tЧисло\tБуква")
    print("-----------------------------")
    print("Оцінка №1\t", score1, "\t", determine_grade(score1))
    print("Оцінка №2\t", score2, "\t", determine_grade(score2))
    print("Оцінка №3\t", score3, "\t", determine_grade(score3))
    print("Оцінка №4\t", score4, "\t", determine_grade(score4))
    print("Оцінка №5\t", score5, "\t", determine_grade(score5))
    print("-----------------------------")
    print("Середній бал\t", average, "\t", determine_grade(average))


# Функція розраховує і повертає середній бал.
def calculate_average(score1, score2, score3, score4, score5):
    return (score1 + score2 + score3 + score4 + score5) / 5


# Функція визначає і повертає буквений рівень оцінки.
def determine_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# Виклик головної функції.
main()

# Вправа по програмуванню 2-10
# Регулятор інгредієнтів

# Константи для кількості печива, цукру, масла та муки згідно рецепту.
COOKIES_RECIPE = 48.0
SUGAR_RECIPE = 1.5
BUTTER_RECIPE = 1.0
FLOUR_RECIPE = 2.75

# Отримання кількості печива.
cookies = float(input("Кількість печива: "))

# Розрахунок кількості цукру.
sugar = (cookies * SUGAR_RECIPE) / COOKIES_RECIPE

# Розрахунок кількості масла.
butter = (cookies * BUTTER_RECIPE) / COOKIES_RECIPE

# Розрахунок кількості муки.
flour = (cookies * FLOUR_RECIPE) / COOKIES_RECIPE

# Виводимо на екран результати розрахунків.
print(f"\nДля приготування {cookies:.0f} штук печива необхідно:")
print(f"Стаканів цукру - {sugar:.1f}")
print(f"Стаканів масла - {butter:.1f}")
print(f"Стаканів муки - {flour:.1f}")

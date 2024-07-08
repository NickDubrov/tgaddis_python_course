# Вправа по програмуванню 3-8
# Калькулятор інгредієнтів для пікніку

# Іменовані константи.
SAUSAGES_IN_PACK = 10
BUNS_IN_PACK = 8

# Отримання кількості присутніх на пікніку.
persons = int(input("Кількість людей на пікніку: "))

# Отримання кількості хот-догів на одну людину.
hotdog_per_person = int(input("Кількість хот-догів на одну людину: "))

# Розрахунок загальної кількості хот-догів.
total = persons * hotdog_per_person

# Розрахунок необхідної кількості упаковок з сосисками
# і кількості сосисок, що залишилися після пікніку.
sausage_pack = total // SAUSAGES_IN_PACK
if sausage_pack > 0:
    sausages_left = total % SAUSAGES_IN_PACK
    if sausages_left != 0:
        sausage_pack += 1
else:
    sausage_pack = 1
sausages_left = sausage_pack * SAUSAGES_IN_PACK - total

# Розрахунок необхідної кількості упаковок з булочками
# та кількості булочок, що залишилися після пікніку.
buns_pack = total // BUNS_IN_PACK
if buns_pack > 0:
    buns_left = total % BUNS_IN_PACK
    if buns_left != 0:
        buns_pack += 1
else:
    buns_pack = 1
buns_left = buns_pack * BUNS_IN_PACK - total

# Виводимо результати розрахунків на екран.
print(f"\nВсього хот-догів приготовлено: {total}")
print(f"Необхідно упаковок з сосисками: {sausage_pack}")
print(f"Необхідно упаковок з булочками: {buns_pack}")
print(f"Кількість сосисок, що залишилося: {sausages_left}")
print(f"Кількість булочок, що залишилося: {buns_left}")

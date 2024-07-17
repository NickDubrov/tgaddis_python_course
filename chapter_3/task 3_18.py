# Вправа по програмуванню 3-18
# Селектор ресторанів

# Визначення друзів, які будуть на зустрічі.
print("Чи буде вегетаріанець на зустрічі (так чи ні)? ", end="")
answer = input()
if answer == "так":
    vegetarian = True
else:
    vegetarian = False

print("Чи буде веган на зустрічі (так чи ні)? ", end="")
answer = input()
if answer == "так":
    vegan = True
else:
    vegan = False

print("Чи буде прихильник безглютенової дієти на зустрічі (так чи ні)? ", end="")
answer = input()
if answer == "так":
    gluten_out = True
else:
    gluten_out = False

# Виводимо результати на екран.
print("\nВаріанти ресторанів:")
if not vegetarian and not vegan and not gluten_out:
    print("Вишукані гамбургери від Джо")
if not vegan and not gluten_out:
    print("Страви від італійської мами")
if not vegan:
    print("Центральна піцерія")
print("Кафе за рогом")
print("Кухня шеф-кухаря")

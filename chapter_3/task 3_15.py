# Вправа по програмуванню 3-15
# Калькулятор часу

# Отримання кількості секунд від користувача.
total_seconds = int(input("Кількість секунд, введених користувачем: "))

# Розрахунок кількості тижнів, днів, годин, хвилин та секунд.
# Виводимо результати на екран.
if total_seconds < 60:
    seconds = total_seconds % 60
    print(f"\nВ {total_seconds} секундах...")
    print(f"cекунд: {seconds}")
elif total_seconds < 3600:
    minutes = (total_seconds // 60)
    seconds = total_seconds % 60
    print(f"\nВ {total_seconds} секундах...")
    print(f"хвилин: {minutes}")
    print(f"секунд: {seconds}")
elif total_seconds < 86400:
    hours = (total_seconds // 3600)
    minutes = (total_seconds // 60) % 60
    seconds = total_seconds % 60
    print(f"\nВ {total_seconds} секундах...")
    print(f"годин: {hours}")
    print(f"хвилин: {minutes}")
    print(f"секунд: {seconds}")
elif total_seconds < 604800:
    days = (total_seconds // (3600 * 24))
    hours = (total_seconds // 3600) % 24
    minutes = (total_seconds // 60) % 60
    seconds = total_seconds % 60
    print(f"\nВ {total_seconds} секундах...")
    print(f"днів: {days}")
    print(f"годин: {hours}")
    print(f"хвилин: {minutes}")
    print(f"секунд: {seconds}")
elif total_seconds >= 604800:
    weeks = (total_seconds // (3600 * 24 * 7))
    days = (total_seconds // (3600 * 24)) % 7
    hours = (total_seconds // 3600) % 24
    minutes = (total_seconds // 60) % 60
    seconds = total_seconds % 60
    print(f"\nВ {total_seconds} секундах...")
    print(f"тижнів: {weeks}")
    print(f"днів: {days}")
    print(f"годин: {hours}")
    print(f"хвилин: {minutes}")
    print(f"секунд: {seconds}")

# Вправа по програмуванню 7-5
# Перевірка допустимості номера видаткового рахунку


# Головна функція.
def main():
    try:
        # Відкриття файлу для читання.
        infile = open(r"chapter_7\data\charge_accounts.txt")

        # Читання файлу та збереження його вмісту в список.
        accounts = infile.readlines()

        # Закриття файлу.
        infile.close()

        # Відсікання символу нової строки.
        for i in range(len(accounts)):
            accounts[i] = accounts[i].rstrip('\n')

        # Отримання номеру видаткового рахунку від користувача.
        entered_account = input("Номер видаткового рахунку: ")

        # Перевірка допустимості номера видаткового рахунку.
        if entered_account in accounts:
            print(f"Номер рахунку {entered_account} є допустимим.")
        else:
            print(f"Номер рахунку {entered_account} не є допустимим.")

    except IOError:
        print("Виникла помилка під час спроби прочитати файл")
    except Exception as error:
        print("Виникла помилка!")
        print(error)


# Виклик головної функції.
main()

# Вправа по програмуванню 6-1
# Виведення файлу на екран


# Головна функція.
def main():
    # Відкриття файлу для читання.
    infile = open(r"chapter_6\data\numbers.txt")

    # Читання файлу та збереження його вмісту в змінній.
    contents = infile.read()

    # Закриття файлу.
    infile.close()

    # Виводимо вміст файлу на екран.
    print(contents)


# Виклик головної функції.
main()

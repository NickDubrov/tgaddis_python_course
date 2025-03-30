# Вправа по програмуванню 6-11
# Генератор персональної веб-сторінки


# Головна функція.
def main():
    # Отримання імені користувача.
    name = input("Введіть своє ім'я: ")

    # Отримання інформації про користувача.
    description = input("Опишіть себе: ")

    # Відкриття файлу для запису.
    outfile = open(r"chapter_6\data\my_page.html", 'w')

    # Написання HTML-розмітки сторінки.
    write_html(outfile, name, description)

    # Закриття файлу.
    outfile.close()


# Функція записує HTML-розмітку сторінки.
def write_html(outfile, name, description):
    # Написання тегу <html>.
    outfile.write("<html>\n")

    # Написання заголовку сторінки.
    write_head(outfile)

    # Написання тіла сторінки.
    write_body(outfile, name, description)

    # Написання тегу </html>.
    outfile.write("</html>\n")


# Функція записує заголовок сторінки.
def write_head(outfile):
    outfile.write("<head>\n")
    outfile.write("\t<title>My personal web page</title>\n")
    outfile.write("</head>\n")


# Функція записує тіло сторінки.
def write_body(outfile, name, description):
    outfile.write("<body>\n")
    outfile.write("\t<center>\n")
    outfile.write(f"\t<h1>{name}</h1>\n")
    outfile.write("\t</center>\n")
    outfile.write("\t<hr />\n")
    outfile.write(f"\t{description}\n")
    outfile.write("\t<hr />\n")
    outfile.write("</body>\n")


# Виклик головної функції.
main()

def get_pliny_letters(filename):
    file = open(filename)
    book = file.read()
    book = book.replace("C. Plinius", "&&C. Plinius")
    return book.split("&&")
    file.close()
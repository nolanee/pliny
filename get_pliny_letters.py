def get_pliny_letters(pliny_book):
    filename = pliny_book.value
    file = open(filename)
    book = file.read()
    book = book.replace("C. Plinius", "&&C. Plinius")
    return book.split("&&")
    file.close()
from book_files import Pliny_book, Cicero_book

def letters(book):
    if isinstance(book, Pliny_book):
        return pliny_letters(book)
    if isinstance(book, Cicero_book):
        return cicero_letters(book)

def pliny_letters(pliny_book):
    book = open_book(pliny_book)
    book = book.replace("C. Plinius", "&&C. Plinius")
    if pliny_book.name == 'X' :
        book = book.replace("Traianus Plinio", "&&Traianus Plinio")   
    return book.split("&&")

def cicero_letters(cicero_book):
    book = open_book(cicero_book)
    book = book.replace("Scr.", "&&Scr.")  
    return book.split("&&")

def open_book(book):
    filename = book.value
    file = open(filename)
    rb = file.read()
    file.close()
    return rb
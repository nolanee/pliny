import re

def pliny_letters(pliny_book):
    filename = pliny_book.value
    file = open(filename)
    book = file.read()
    file.close()

    book = book.replace("C. Plinius", "&&C. Plinius")
    if pliny_book.name == 'X' :
        book = book.replace("Traianus Plinio", "&&Traianus Plinio")   
    return book.split("&&")
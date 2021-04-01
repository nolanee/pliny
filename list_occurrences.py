from pliny_letters import pliny_letters
from contains_greek import contains_greek

def offset(num):
    if num < 4:
        return 0
    if num < 19:
        return 1
    if num < 89:
        return 2
    return 3

def provide_citation(pliny_book, num):
    if pliny_book.name == 'X':
        num = num - offset(num)
    return pliny_book.name + '.' + str(num)

def list_greek(pliny_book):
    found_letters = []
    letters = pliny_letters(pliny_book)
    num = 0
    for letter in letters:
        if contains_greek(letter):
            found_letters.append(provide_citation(pliny_book, num))
        num = num + 1
    return found_letters
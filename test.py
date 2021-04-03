from is_alphabet import is_latin, is_greek
from pliny_letters import letters
from book_files import Pliny_book, Cicero_book
from list_occurrences import list_greek

assert(is_latin('a') == True)
assert(is_latin('ᾶ') == False)
assert(is_greek('ᾶ') == True)

assert("C. Plinius Baebio Hispano suo s." in letters(Pliny_book.I)[24])

assert(list_greek(Pliny_book.I) == ['I.2', 'I.5', 'I.7', 'I.9', 'I.12', 'I.18', 'I.20'])
assert(list_greek(Pliny_book.X) == ['X.10', 'X.15', 'X.116', 'X.117', 'X.118', 'X.119'])

print(letters(Cicero_book.I)[5])

from is_alphabet import is_latin, is_greek
from pliny_letters import pliny_letters
from book_files import Pliny_books
from list_occurrences import list_greek

assert(is_latin('a') == True)
assert(is_latin('ᾶ') == False)
assert(is_greek('ᾶ') == True)

assert("C. Plinius Baebio Hispano suo s." in pliny_letters(Pliny_books.I)[24])

assert(list_greek(Pliny_books.I) == ['I.2', 'I.5', 'I.7', 'I.9', 'I.12', 'I.18', 'I.20'])
assert(list_greek(Pliny_books.X) == ['X.10', 'X.15', 'X.116', 'X.117', 'X.118', 'X.119'])



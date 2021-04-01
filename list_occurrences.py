from get_pliny_letters import get_pliny_letters
from contains_greek import contains_greek

def list_greek(pliny_book):
    found_letters = []
    letters = get_pliny_letters(pliny_book)
    num = 0
    for letter in letters:
        if contains_greek(letter):
            found_letters.append(pliny_book.name + '.' + str(num))
        num = num + 1
    return found_letters
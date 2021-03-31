from is_alphabet import is_latin, is_greek
from get_pliny_letters import get_pliny_letters
from contains_greek import contains_greek

assert(is_latin('a') == True)
assert(is_latin('ᾶ') == False)
assert(is_greek('ᾶ') == True)

assert("C. Plinius Baebio Hispano suo s." in get_pliny_letters("Plinius/Epistulae1.txt")[24])

book_one = get_pliny_letters("Plinius/Epistulae1.txt")

for letter in book_one:
    if contains_greek(letter):
        print(letter)
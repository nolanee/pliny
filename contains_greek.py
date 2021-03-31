from is_alphabet import is_greek

def contains_greek(letter):
    for word in letter:
        for letter in word:
            if is_greek(letter):
                return True
    return False
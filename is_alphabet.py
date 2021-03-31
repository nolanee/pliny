import unicodedata as ud

def is_alphabet(alphabet, uchar):
    if uchar == '\n':
        return False
    return alphabet in ud.name(uchar)

def is_latin(uchar):
    return is_alphabet("LATIN", uchar)

def is_greek(uchar):
    return is_alphabet("GREEK", uchar)
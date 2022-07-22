from difflib import get_close_matches
from .uzwords import words


def check_word(word):
    if word.isalpha():
        word = word.lower()
        matches = set(get_close_matches(word, words))
        available = 0
        if word in words:
            available = 1
            matches = word
        return {'available':available, 'matches':matches}
    else:
        available = 2
        return {'available': available}

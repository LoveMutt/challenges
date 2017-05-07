#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html
import random
import itertools

from challenge02.data import DICTIONARY, LETTER_SCORES, POUCH, _load_words

NUM_LETTERS = 7


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    val = 0
    for c in word.upper():
        if not c in LETTER_SCORES:
            continue
        val += LETTER_SCORES[c]
    return val


def max_word_value(word_list=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if word_list == None:
        word_list = _load_words()
    max_val = -1
    max_word = ''
    for word in word_list:
        word_val = calc_word_value(word)
        if word_val > max_val:
            max_val = word_val
            max_word = word
    return max_word


def draw_letters():
    """Select NUM_LETTERS letters from the pouch based on distribution"""
    p = POUCH.copy()
    random.shuffle(p)
    return p[0:NUM_LETTERS]


def get_possible_dict_words(letters):
    """Find the valid words from letters that are found in DICTIONARY"""
    p = _get_permutations_draw(letters)  # type: str
    dict_words = [word for word in p if word.lower() in DICTIONARY]
    return dict_words


def _get_permutations_draw(letters):
    """Permute the drawn letters into all possible combinations"""
    return [''.join(p) for x in range(1, len(letters)+1) for p in itertools.permutations(letters, x) if len(p) > 0]


def _validation(word, letters):
    """Validate that the word is possible with the given letters"""
    tmp = letters.copy()
    for c in word.upper():
        tmp.pop(tmp.index(c))
    if word.lower() not in DICTIONARY:
        raise ValueError('{} is not a valid dicationary word'.format(word))
    return True


def main():
    draw = draw_letters()
    chosen = input('Form the word with the max value from {} >'.format(draw))
    chosen_val = calc_word_value(chosen)
    print('You chose "{}" that has a value of {}'.format(chosen, chosen_val))
    _validation(chosen, draw)
    best_word = max_word_value(get_possible_dict_words(draw))
    best_val = calc_word_value(best_word)
    print('The optimal word is {} with value {}'.format(best_word, best_val))
    print('You receive a score of {.2}'.format(100*chosen_val/best_val))


if __name__ == "__main__":
    main()

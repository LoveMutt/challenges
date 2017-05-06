#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html
import random

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
    rands = []
    p = POUCH.copy()
    random.shuffle(p)
    return p[0:NUM_LETTERS]


def main():
    pass


if __name__ == "__main__":
    main()

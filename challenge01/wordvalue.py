from challenge01.data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        words = [word.strip() for word in f.readlines() if word]
    return words


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
    pass

if __name__ == "__main__":
    pass # run unittests to validate

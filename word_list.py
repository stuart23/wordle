# from nltk import download
from nltk.corpus import words


def wordList():
    '''
    Returns a list of all 5 letter words that are valid guesses/answers.

    Currently uses NLTK but can be substituted for something else.
    '''
    all_words = list(filter(lambda x: len(x) == 5, words.words()))
    return [x.lower() for x in all_words]

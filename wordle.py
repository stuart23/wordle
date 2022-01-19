from random import randint
from word_list import wordList


class Wordle(object):
    '''
    Game for guessing a 5 letter word. Maximum number of turns allowed is set
    by MAX_TURNS.
    '''
    MAX_TURNS = 5

    def __init__(self):
        '''
        Initializes the all_words list with all the 5 letter words in the
        dictionary. Sets a word as the solution to be guessed.

        State vector represents the remaining possible letters for each space.
        Will return a 5 element list, with each element being an alphabetical
        list of all the possible letters.
        '''
        self.all_words = wordList()
        self.solution = self.all_words[randint(0, len(self.all_words))]
        self.guessed_words = []
        self.state_vector = 5 * [list('abcdefghijklmnopqrstuvwxyz')]

    def guess(self, guessed_word):
        '''
        Assert that the input is a 5 letter word that exists in the word list.
        The word is added to the list of already guessed words.
        '''
        assert isinstance(guessed_word, str), 'Only strings are accepted'
        assert len(guessed_word) == 5, 'Input must be 5 letters'
        assert guessed_word in self.all_words, 'Input is not a recognized word'
        self.guessed_words.append(guessed_word)
        assert self.guess_number <= self.MAX_TURNS, 'Out of turns'

        guess_result = self._evaluate(guessed_word)

        return guess_result

    def visualGuess(self, guessed_word):
        '''
        Wrapper around the guess method to print the answer with the colours.
        '''
        guess_result = self.guess(guessed_word)
        display_string = ''
        for letter, letter_state in zip(guessed_word, guess_result):
            if letter_state == 'correct':
                display_string += '\033[92m{}\033[0m'.format(letter)
            elif letter_state == 'present':
                display_string += '\033[93m{}\033[0m'.format(letter)
            else:
                display_string += letter
        print(display_string)

    def _evaluate(self, guessed_word):
        '''
        Broken out for testing. This is the algorithm for returning the match
        state of the input word. This returns a 5 element list with each
        element being one of:
        - absent = the letter in this position does not exist in the solution.
        - present = the letter in this position exists in the solution in
            another location.
        - correct = the letter in this position is in the correct location.
        '''
        guess_result = []
        for index in range(5):
            if guessed_word[index] == self.solution[index]:
                guess_result.append('correct')
            elif guessed_word[index] in self.solution:
                guess_result.append('present')
            else:
                guess_result.append('absent')
        assert len(guess_result) == 5
        return guess_result

    def _updateStateVector(self, guessed_word):
        '''
        Given a guessed word and the guessed result (correct/present/absent for
        each space), mutate the state_vector property so it represents all the
        plausible letter choices.

        ## THIS MAY NOT BE A GOOD REPRESENTATION BECAUSE IT DOES NOT INCLUDE THE
        LETTERS THAT ARE IN THE WRONG LOCATION.
        '''
        for letter, letter_state in zip(guessed_word, state):
            if letter_state == 'correct':

    @property
    def guess_number(self):
        '''
        Returns the guess number
        '''
        return len(self.guessed_words)

    @property
    def guessed_letters(self):
        '''
        Returns a list of the letters already guessed
        '''
        return sorted(set(''.join(self.guessed_words)))

from wordslist import letters, keyletter, words

class SpellingBee:
    def __init__(self):
        self.wordlist = words
        self.letters = letters
        self.keyletter = keyletter
        self.guessedwords = []
        self.score = 0

    def correct_guess(self, user_guess):
            self.guessedwords.append(user_guess)
            self.score += 1

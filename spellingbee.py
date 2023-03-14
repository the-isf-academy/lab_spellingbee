class SpellingBee:
    def __init__(self, word_list, letter_list, keyletter):
        self.word_list = word_list
        self.letter_list = letter_list
        self.keyletter = keyletter
        self.guessed_words_list = []
        self.score = 0

    def correct_guess(self, user_guess):
        self.guessed_words_list.append(user_guess)
        self.score += 1

    

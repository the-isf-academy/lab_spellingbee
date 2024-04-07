class SpellingBee:
    def __init__(self, word_list, letter_list, keyletter):
        # initializes a spelling bee object with it's properties

        self.word_list = word_list
        self.letter_list = letter_list
        self.keyletter = keyletter
        self.guessed_words = []

    def check_letters(self, user_guess):
        all_letters_valid = True

        for letter in user_guess:
            if letter not in self.letter_list:
                all_letters_valid = False
        
        return all_letters_valid

    def check_wordlist(self, user_guess):
        # checks whether the user's guess is a real word or not
        # returns true or false

        if user_guess in self.word_list:
            return True
        else:
            return False
        
    def correct_word(self, word):
        # adds the correct word to the list of guessed words
        self.guessed_words.append(word)

    

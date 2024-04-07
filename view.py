class TerminalView:

    def welcome(self):
        print("\n---Welcome to Spelling Bee---")

    def rules(self, letters, keyletter):
        print("\n[RULES]")
        print("You can use any of these letters: {}".format(letters))
        print("You must you use the letter {}".format(keyletter))
        print("Guesses must be more than 3 letters long")

    def get_guess(self):
        print("\n---mystery message 0---")
        guess = input(" > ")
        return guess.upper()

    def too_short(self):
        print("\n  -mystery message 1-  ")
    
    def bad_letters(self):
        print("\n  -mystery message 2-  ")
            
    def missing_center_letter(self):
        print("\n  -mystery message 3-  ")

    def not_in_word_list(self):
        print("\n  -mystery message 4-  ")

    def correct(self):
        print("\n  -mystery message 5-  ")

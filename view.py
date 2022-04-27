class TerminalView:
    def mystery_method_1(self, letters, keyletter):
        print("""\nRULES: You can use any of these letters: {}
        You must you use the letter {} \n""".format(letters, keyletter))

    def mystery_method_2(self):
        print("\n---Mystery Method 2---")
        guess = input("> ")
        return guess.upper()

    def mystery_method_3(self):
        print("\n---Mystery Method 3---")

    def mystery_method_4(self):
        print('\n---Mystery Method 4---')

    def mystery_method_5(self):
        print("\n---Mystery Method 5---")

    def mystery_method_6(self, mystery_parameter):
        print('\n---Mystery Method 6---')

    def mystery_method_7(self):
        print("\n---Mystery Method 7---")

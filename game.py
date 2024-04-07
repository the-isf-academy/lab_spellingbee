from wordslist import letter_list, keyletter, word_list
from model import SpellingBee
from view import TerminalView
from helpers import menu

# create a SpellingBee object
spelling_bee = SpellingBee(word_list, letter_list, keyletter)
# create a TerminalView object
terminal_view = TerminalView()                                       

terminal_view.welcome()

terminal_view.rules(spelling_bee.letter_list, spelling_bee.keyletter)

game_play = True

while game_play:

    # user guesses a word
    user_guess = terminal_view.get_guess()

    #check length of word
    if len(user_guess) <= 3:
        terminal_view.too_short()

    #check for bad letters
    elif spelling_bee.check_letters(user_guess) == False:
        terminal_view.bad_letters()

    #check for center letter
    elif spelling_bee.keyletter not in user_guess:
        terminal_view.missing_center_letter()
    
    #check word list
    elif spelling_bee.check_wordlist(user_guess) == False:
        terminal_view.not_in_word_list()

    #word is valid
    else:
        #save the correct word
        spelling_bee.correct_word(user_guess)
        #give the user a success message
        terminal_view.correct()

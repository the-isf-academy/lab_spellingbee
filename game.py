from wordslist import letter_list, keyletter, word_list
from spellingbee import SpellingBee
from view import TerminalView


spelling_bee = SpellingBee(word_list, letter_list, keyletter)        # creates a SpellingBee()
view = TerminalView()                                                # creates a TerminalView()

view.mystery_method_0()

view.mystery_method_1(spelling_bee.letter_list, spelling_bee.keyletter)

game_play = True

while game_play:

    user_guess = view.mystery_method_2()

    is_letter_valid = True

    for letter in user_guess:
        if letter not in spelling_bee.letter_list:
            is_letter_valid = False
            
    if  is_letter_valid == False:
        view.mystery_method_3()

    elif spelling_bee.keyletter not in user_guess:
        view.mystery_method_4()

    elif user_guess in spelling_bee.guessed_words_list:
        view.mystery_method_5()
        
    elif user_guess in spelling_bee.word_list:
        spelling_bee.correct_guess(user_guess)
        view.mystery_method_6("mystery_value")

    else:
        view.mystery_method_7()

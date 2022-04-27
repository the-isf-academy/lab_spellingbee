from spellingbee import SpellingBee
from view import TerminalView

spelling_bee = SpellingBee()
view = TerminalView()


def game():
    view.mystery_method_1(spelling_bee.letters, spelling_bee.keyletter)
    while True:
        user_guess = view.mystery_method_2()
        for letter in user_guess:
            if letter not in spelling_bee.letters:
                break

        if letter not in spelling_bee.letters:
            view.mystery_method_3()
        elif spelling_bee.keyletter not in user_guess:
            view.mystery_method_4()
        elif user_guess in spelling_bee.guessedwords:
            view.mystery_method_5()
        elif user_guess in spelling_bee.wordlist:
            spelling_bee.correct_guess(user_guess)
            view.mystery_method_6("mystery_value")
        else:
            view.mystery_method_7()
game()

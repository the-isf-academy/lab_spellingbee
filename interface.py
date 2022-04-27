################################
# interface for the Pet object
# ----------
# it's up to you to finish it! 
# feel free to customize it as you please.
################################

# Creates a fancy menu system in the Terminal
from simple_term_menu import TerminalMenu

# Imports the Pet from pet.py
from pet import Pet  

def menu(options):
    '''This function creates an interactive Terminal menu.'''

    terminal_menu = TerminalMenu(options) #Creates the Terminal Menu 
    option_num = terminal_menu.show() #Get user selected Option 

    return options[option_num]
    

def pet_simulator():
    '''This function runs the game.'''
    
    print("-"*35)
    print("---- Welcome to Pet Simulator ----")
    print("-"*35,"\n")

    print("What would you like to name your pet?")
    name = input(" > ")

    my_pet = Pet() #create the pet
    my_pet.set_name(name)

    print("-"*25)
    print("Your pet is ready!")
    print("-"*25)

    play = True

    while play == True:
        options = ["Introduce", "Quit"] #set the menu choices

        option = menu(options)

        if option == 'Introduce':
            my_pet.introduce()

        elif option == 'Quit':
            play = False

    print("-"*29)
    print("--- Leaving Pet Simulator ---")
    print("-"*29)

pet_simulator()
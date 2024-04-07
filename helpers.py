# helper function

from InquirerPy import inquirer, get_style       # creates a menu system in the Terminal


def menu(prompt, options):
    # This function creates an interactive Terminal menu.
    # it returns the selected Node 

    choice = inquirer.select(
        message= f"\n{prompt}",
        choices= options,
        qmark="",
        amark="",
        style= get_style({ 
            "answer": "#438fa8",
            "pointer": "#438fa8",
            "questionmark": "hidden"
            },
            ),
        ).execute()

    return choice
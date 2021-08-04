# Importing all of the needed functions
from modules.design import menu
from modules.functions import call, open_file

# List of all possible choices given to the user
lst = ('Jogar', 'Palavras', 'Adicionar', 'Deletar', 'Fechar')
open_file()  # Creates a file if necessary

while True:  # Runs the main program
    call(menu(lst))  # Shows the menu and calls the function
    print()

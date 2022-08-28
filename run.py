"""
Import section (to put in)
"""



cash = 0



def introduction():

    """
    Function to get the users name and to explain the rules
    """
    
    name = input('What is your name: ')
    print('\n')
    print (f'Hello {name} and welcome to the Cash Building Quiz! \n')
    print('The rules are simply... you have 10 questions ')
    print('The questions get harder for each one you answer correctly ')
    print('You gain a massive 100 euro to your pot for each question you answer right')
    print('You have the option to leave the game with your cash that you earned ')
    print('Or do you dare to answer the next question answer wrong and you lose all your cash. \n')
    play = input('Do you wish to play the Cash Building Game? type Y or N :')
    if play.capitalize() == 'Y':
        print('starting game')
    elif play.capitalize() == 'N':
        print(f'You have choose not to play. Come back when your ready {name}')
    else:
        print(f'Invalid choice {name} The game will now restart')
    
    
def main():
    introduction()


main()


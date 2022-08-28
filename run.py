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
    print(f'Hello {name} and welcome to the Cash Building Quiz! \n')
    print('The rules are simply... you have 10 questions ')
    print('The questions get harder for each one you answer correctly ')
    print('You gain a massive 100 euro to your pot for each question you answer right')
    print('You have the option to leave the game with your cash that you earned ')
    print('Or do you dare to answer the next question answer wrong and you lose all your cash. \n')
    play = input('Do you wish to play the Cash Building Game? type Y or N :')
    if play.capitalize() == 'Y':
        start_game()
    elif play.capitalize() == 'N':
        print(f'You have choose not to play. Come back when your ready {name}')
    else:
        print(f'Invalid choice {name} The game will now restart')

def start_game():

    """
    question one
    """

    cash = 0
    print('Question Number One for 100euro....\n')
    print('Q1. What is the Capital of Ireland: \nA. Galway \nB. Dublin \nC. Kilkenny \nD. Cork')
    answer = input ('What do you think the answer is :')
    if answer.capitalize() == 'B' or answer.capitalize() == 'Dublin':
        cash =+ 100
        print(f'Well Done You have won {cash} euro!!')
        decision = input(f'Would you like to answer another question or take the {cash} euro. \nA. Another Question \nB. Keep The Cash :')
        if decision.capitalize() == 'A' or answer.capitalize() == 'Another question':
                question_two() 
        else:
             print ('Thank you for playing the game!')
    else:
        print('Your wrong! The Answer was B. Dublin. Thanks for playing!')

def question_two():
    print('question 2')

def main():
    """
    Main function to run the game
    """
    introduction()
    
main()
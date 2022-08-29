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

    
    print('Question Number One for 100euro....\n')
    print('Q1. What is the Capital of Ireland: \nA. Galway \nB. Dublin \nC. Kilkenny \nD. Cork')
    answer = input ('What do you think the answer is :')
    if answer.capitalize() == 'B' or answer.capitalize() == 'Dublin':
        cash =+ 100
        print(f'Well Done You have won {cash} euro!!')
        decision = input(f'Would you like to answer another question or take the {cash} euro. \nA. Another Question \nB. Keep The Cash :')
        if decision.capitalize() == 'A' or answer.capitalize() == 'Another question':
                return cash
        else:
             print (f'You have decided to keep the {cash} euro. \nThank you for playing the game!')
             introduction()
    else:
        print('Your wrong! The Answer was B. Dublin. Thanks for playing!')
        introduction()


def question_two():
    """
    Question two function
    """

    print('Question Number two for 200euro....\n')
    print('Q2. Who Created the Xbox: \nA. Apple \nB. Sony \nC. Nintendo \nD. Microsoft')
    answer = input ('What do you think the answer is :')
    if answer.capitalize() == 'D' or answer.capitalize() == 'Microsoft':
        cash =+ 100
        print(f'Well Done You have won {cash} euro!!')
        decision = input(f'Would you like to answer another question or take the {cash} euro. \nA. Another Question \nB. Keep The Cash :')
        if decision.capitalize() == 'A' or answer.capitalize() == 'Another question':
                return cash
        else:
            print (f'You have decided to keep the {cash} euro. \nThank you for playing the game!')
            introduction()
    else:
        print('Your wrong! The Answer was D. Microsoft. Thanks for playing!')
        introduction()
        


def question_three():
    """
    question three function
    """
    

    print('Question Number three for 300euro....\n')
    print('Q3. Where is the Car manufacturers Audi From:\nA. Germany \nB. China\nC. U.S.A \nD. England')
    answer = input ('What do you think the answer is :')
    if answer.capitalize() == 'A' or answer.capitalize() == 'Germany':
        cash =+ 100
        print(f'Well Done You have won {cash} euro!!')
        decision = input(f'Would you like to answer another question or take the {cash} euro. \nA. Another Question \nB. Keep The Cash :')
        if decision.capitalize() == 'A' or answer.capitalize() == 'Another question':
                return cash
        else:
            print (f'You have decided to keep the {cash} euro. \nThank you for playing the game!')
            introduction()
    else:
        print('Your wrong! The Answer was A. Germany. Thanks for playing!')
        introduction()

def question_four():
    """
    question four function
    """
    print('Question Number four for 400euro....\n')
    print('Q4.Which of these is a Song from Harry Style:\nA. UpTown Girl\nB. Californation\nC. Adore You \nD. Londons Burning')
    answer = input ('What do you think the answer is :')
    if answer.capitalize() == 'C' or answer.capitalize() == 'Adore You':
        cash =+ 100
        print(f'Well Done You have won {cash} euro!!')
        decision = input(f'Would you like to answer another question or take the {cash} euro. \nA. Another Question \nB. Keep The Cash :')
        if decision.capitalize() == 'A' or answer.capitalize() == 'Another question':
                return cash
        else:
            print(f'You have decided to keep the {cash} euro. \nThank you for playing the game!')
            introduction()
    else:
        print('Your wrong! The Answer was C. Adore You. Thanks for playing!')
        introduction()

def question_five():
    print('Half way there with 500euro....\n')
    print('Q5. Which of these EU countries does not use the euro as its currency?\nA. Poland\nB. Denmark \nC. Sweden\nD. All of the above  ')
    answer = input ('What do you think the answer is :')
    if answer.capitalize() == 'D' or answer.capitalize() == 'All of the above':
        cash =+ 100
        print(f'Well Done You have won {cash} euro!!')
        decision = input(f'Would you like to answer another question or take the {cash} euro. \nA. Another Question \nB. Keep The Cash :')
        if decision.capitalize() == 'A' or answer.capitalize() == 'Another question':
                return cash
        else:
            print(f'You have decided to keep the {cash} euro. \nThank you for playing the game!')
            introduction()
    else:
        print('Your wrong! The Answer was D. All of the above. Thanks for playing!')
        introduction()

def question_six():
    print ('six')
    



def main():
    """
    Main function to run the game
    """
    introduction()
    question_two()
    question_three()
    question_four()
    question_five()
    question_six()
    
    
main()
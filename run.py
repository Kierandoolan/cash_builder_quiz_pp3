"""
Import section (to put in)
"""

cash = []


def restartgame():
    """
    Function to start from the beginning
    """
    restart = input('Would you like to play again? Y/N')
    if restart.capitalize() == 'Y':
        print('Great!')
        main()
    else:
        print('You have choosen no. see you soon...')
        restartgame()

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
        return
    elif play.capitalize() == 'N':
        print(f'You have choose not to play. Come back when your ready {name}')
        main()
    else:
        print(f'Invalid choice {name} The game will now restart')
        main()


def start_game():

    """
    question one
    """
    print('Question Number One for 100euro....\n')
    print('Q1. What is the Capital of Ireland: \nA. Galway \nB. Dublin \nC. Kilkenny \nD. Cork')
    answer = input('What do you think the answer is :')
    if answer.capitalize() == 'B' or answer.capitalize() == 'Dublin':
        cash =+ 100
        print(f'Well Done You have won {cash} euro!!')
        decision = input(f'Would you like to answer another question or take the {cash} euro. \nA. Another Question \nB. Keep The Cash :')
        if decision.capitalize() == 'A' or answer.capitalize() == 'Another question':
                return cash
        else:
             print (f'You have decided to keep the {cash} euro. \nThank you for playing the game!')
             restartgame()
    else:
        print('Your wrong! The Answer was B. Dublin. Thanks for playing!')
        restartgame()


def question_two():
    """
    Question two function
    """

    print('Question Number two for 200euro....\n')
    print('Q2. Who Created the Xbox: \nA. Apple \nB. Sony \nC. Nintendo \nD. Microsoft')
    answer = input ('What do you think the answer is :')
    if answer.capitalize() == 'D' or answer.lower() == str.lower('microsoft'):
        cash =+ 100
        print(f'Well Done You have won {cash} euro!!')
        decision = input(f'Would you like to answer another question or take the {cash} euro. \nA. Another Question \nB. Keep The Cash :')
        if decision.capitalize() == 'A' or answer.lower() == str.lower('another question'):
                return cash
        else:
            print (f'You have decided to keep the {cash} euro. \nThank you for playing the game!')
            restartgame()
    else:
        print('Your wrong! The Answer was D. Microsoft. Thanks for playing!')
        restartgame()
        


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
            restartgame()
    else:
        print('Your wrong! The Answer was A. Germany. Thanks for playing!')
        restartgame()

def question_four():
    """
    question four function
    """
    print('Question Number four for 400euro....\n')
    print('Q4.Which of these is a Song from Harry Style:\nA. UpTown Girl\nB. Californication\nC. Adore You \nD. Londons Burning')
    answer = input('What do you think the answer is :')
    if answer.capitalize() == 'B' or answer.capitalize() == 'Californication':
        cash =+ 100
        print(f'Well Done You have won {cash} euro!!')
        decision = input(f'Would you like to answer another question or take the {cash} euro. \nA. Another Question \nB. Keep The Cash :')
        if decision.capitalize() == 'A' or answer.capitalize() == 'Another question':
                return cash
        else:
            print(f'You have decided to keep the {cash} euro. \nThank you for playing the game!')
            restartgame()
    else:
        print('Your wrong! The Answer was B Californication . \nThanks for playing!')
        restartgame()

def question_five():
    """
    question five function
    """
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
            restartgame()
    else:
        print('Your wrong! The Answer was D. All of the above. Thanks for playing!')
        restartgame()

def question_six():
    """
    question six function
    """
    print('Question number six for 600euro....\n')
    print('Q6.What color dresses do Chinese women traditionally wear on their wedding day?\nA. Blue \nB. Gold\nC. White \nD. Red ')
    answer = input ('What do you think the answer is :')
    if answer.capitalize() == 'D' or answer.capitalize() == 'Red':
        cash =+ 100
        print(f'Well Done You have won {cash} euro!!')
        decision = input(f'Would you like to answer another question or take the {cash} euro. \nA. Another Question \nB. Keep The Cash :')
        if decision.capitalize() == 'A' or answer.capitalize() == 'Another question':
                return cash
        else:
            print(f'You have decided to keep the {cash} euro. \nThank you for playing the game!')
            restartgame()
    else:
        print('Your wrong! The Answer was D. Red. Thanks for playing!')
        restartgame()
    
def question_seven():
    """
    question seven function
    """
    print('Question number seven for 700euro....\n')
    print('Q7.How many molecules of oxygen does ozone have?\nA. 1\nB. 2\nC. 3 \nD. 4 ')
    answer = input ('What do you think the answer is :')
    if answer.capitalize() == 'C' or answer.capitalize() == 'Three' or answer == '3':
        cash =+ 100
        print(f'Well Done You have won {cash} euro!!')
        decision = input(f'Would you like to answer another question or take the {cash} euro. \nA. Another Question \nB. Keep The Cash :')
        if decision.capitalize() == 'A' or answer.capitalize() == 'Another question':
                return cash
        else:
            print(f'You have decided to keep the {cash} euro. \nThank you for playing the game!')
            restartgame()
    else:
        print('Your wrong! The Answer was C. Three. Thanks for playing!')
        restartgame()
    
def question_eight():
    """
    Question eight function
    """
    print('Question number eight for 800euro....\n')
    print('Q8. Where did the croissant originate?\nA. France\nB. Austria \nC. Turkey \nD. Tokyo')
    answer = input ('What do you think the answer is :')
    if answer.capitalize() == 'B' or answer.capitalize() == 'Austria':
        cash =+ 100
        print(f'Well Done You have won {cash} euro!!')
        decision = input(f'Would you like to answer another question or take the {cash} euro. \nA. Another Question \nB. Keep The Cash :')
        if decision.capitalize() == 'A' or answer.capitalize() == 'Another question':
                return cash
        else:
            print(f'You have decided to keep the {cash} euro. \nThank you for playing the game!')
            restartgame()
    else:
        print('Your wrong! The Answer was B. Austria Thanks for playing!')
        restartgame()
    
def question_nine():
    """
    Question nine function
    """
    print('Question number nine for 900euro....\n')
    print('Q9. Q9. Pupusas are from what country?\nA. Mexico\nB. El Salvador \nC. Brazil \nD. Poland ')
    answer = input ('What do you think the answer is :')
    if answer.capitalize() == 'B' or answer.capitalize() == 'El Salador':
        cash =+ 100
        print(f'Well Done You have won {cash} euro!!')
        decision = input(f'Would you like to answer the FINAL question or take the {cash} euro. \nA. Another Question \nB. Keep The Cash :')
        if decision.capitalize() == 'A' or answer.capitalize() == 'Another question':
                return cash
        else:
            print(f'You have decided to keep the {cash} euro. \nThank you for playing the game!')
            restartgame()
    else:
        print('Your wrong! The Answer was B. El Salvador Thanks for playing!')
        restartgame()

def question_ten():
    """
    Question ten function
    """
    print('Last question for a massive 1000euro....\n')
    print('Q10. Which of these US presidents appeared on the television series "Laugh-In?"\nA: Lyndon Johnson \nB: Richard Nixon \nC: Jimmy Carter \nD: Gerald Ford')
    answer = input ('What do you think the answer is :')
    if answer.capitalize() == 'B' or answer.capitalize() == 'Richard Nixon':
        cash =+ 100
        print(f'Congratulations you have won {cash} euro and have completed the game. I hope you had fun!!')
    else:
        print('Oh no you lost all the cash! The Answer was B. Richard Nixon. Thanks for playing!')
        restartgame()

def main():
    """
    Main function to run the game
    """
    cash = 0
    introduction()  
    start_game()
    question_two()
    question_three()
    question_four()
    question_five()
    question_six()
    question_seven()
    question_eight()
    question_nine()
    question_ten()


main()
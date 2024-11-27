import random

emoji = {'r' : '🪨', 's' : '✂️', 'p' : '📃'}
game = ("r", "p", "s")
win = 0

def GetChoice():
    while(1):
        Pick = input("Rock, paper, or scissors? (r/p/s): ")
        if Pick in game:
            return Pick
        else:
            print("Invalid choice!")

def display_choice(choice, Pick):
        print(f'You chose: {emoji[Pick]}')
        print(f'Computer chose: {emoji[choice]}')

def GamePlay(choice, Pick):
    # win = win
    if choice == Pick:
        print("Tie!")
    elif(    
        (choice == 'r' and Pick == 'p') or
        (choice == 'p' and Pick == 's') or 
        (choice == 's' and Pick == 'r')):
        print("You win!!")
        # win += 1
        # return win 
    else:
        print("You lose!")

def PlayTheGame():
    while(1):
        Pick = GetChoice()
        choice = random.choice(game)
        display_choice(choice, Pick)
        GamePlay(choice, Pick);

        Playing = input('Continue? (y/n): ').lower()
        if Playing == 'n':
            # print('You won : ' + str(win) + ' times!!')
            exit(0)

PlayTheGame()


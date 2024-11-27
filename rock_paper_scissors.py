import random
#Constant Variables
ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

#Initial declaration
emoji = {ROCK : '🪨', SCISSORS : '✂️', PAPER : '📃'}
game = (tuple(emoji.keys()))
win = 0

#Input Function
def GetChoice():
    while(1):
        Pick = input("Rock, paper, or scissors? (r/p/s): ")
        if Pick in game:
            return Pick
        else:
            print("Invalid choice!")

#Game setup
def display_choice(choice, Pick):
        print(f'You chose: {emoji[Pick]}')
        print(f'Computer chose: {emoji[choice]}')

#Game circuit
def GamePlay(choice, Pick):
    # win = win
    if choice == Pick:
        print("Tie!")
    elif(    
        (choice == ROCK and Pick == PAPER) or
        (choice == PAPER and Pick == SCISSORS) or 
        (choice == SCISSORS and Pick == ROCK)):
        print("You win!!")
        # win += 1
        # return win 
    else:
        print("You lose!")

#Game logic
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

#main function call
PlayTheGame()


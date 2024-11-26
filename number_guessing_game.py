import random

choice = input("Do you want to play with a random number? ")

if choice.lower() == 'y':
    myNumber = random.randint(1, 100)
else:
    myNumber = 5
while(1):
    guess = int(input("Guess the number between 1 and 100: "))
    if guess > myNumber:
        print("Too high!")
    elif guess < myNumber:
        print("Too low!")
    elif guess == myNumber:
        print("Congratulations! You guessed the number.")
        exit(0)
    else:
        print("Please enter a valid number")

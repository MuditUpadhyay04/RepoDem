import random
NumPlays = 0
while(1):
    choice = input("Roll the dice? (y/n): ")
    if choice.lower() == 'y':
        dieCount = int(input("How many die's do you want? "))
        i = 0
        die = []
        for i in range(0, dieCount):
            die.append(random.randint(1,6))
        print(die)
        NumPlays += 1
    elif choice.lower() == 'n':
        print("Thanks for playing!")
        print("You rolled " + str(NumPlays) + " times!")
        exit(0)
    else:
        print("Invalid choice!")
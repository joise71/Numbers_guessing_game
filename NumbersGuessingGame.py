import random
#Numbers guessing game
print("Welcome! This is a numbers guessing game")
tries = 10
while tries > 0:
    try:
        print("Tries left: " + str(tries))
        computer = random.randint(1, 51)
        player = int(input("Please guess the number from 1 to 50: "))
        if player >= 1 and player <= 50:
            tries -= 1
            if player == computer and tries > 7:
                print("Congratulations!")
                print("You won within " + str((11-tries)) + " time")
                print("You are very lucky")
            elif player == computer and tries > 4:
                print("Congratulations!")
                print("You won within " + str((11-tries)) + " time")
                print("You are kinda lucky")
            elif player == computer:
                print("Congratulations!")
                print("You won within " + str((11-tries)) + " time")
                print("You are lucky")
            elif player != computer and tries >0:
                print("You have " + str(tries) + " tries left")
            elif player != computer:
                print("No more tries left. Good luck!")
        else:
            print("Your input should be within 1 and 50")
    except ValueError:
        print("Your input should be a number")


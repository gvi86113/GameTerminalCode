import random

print("Hello there. Welcome to the game ""Terminal Code""!")
print("The player who guess the exact number is the winner/loser!(up to you.)")

def TerminalCode():

    lower_limit = int(input("Please set a lower limit: "))
    upper_limit = int(input("Please set a upper limit: "))
    members = int(input("How many players in this game?: "))
    
    print("Game Start!")
    code = random.randint(lower_limit, upper_limit+1)
    next = True

    while next:
        i = 1
        while i <= members:
            guess = int(input("Player {}'s turn! Please guess a number between {} and {} : ".format(str(i), str(lower_limit), str(upper_limit))))

            if guess >= upper_limit or guess <= lower_limit:
                print("Your guess is out of range!")
                continue
                
            elif guess == code:
                print("Bomb! You guess the exact number!")
                next = False
                break
            else:
                if guess > code:
                    upper_limit = guess
                    i = i + 1
                else:
                    lower_limit = guess
                    i = i + 1

    again = input("Do you want to play again?(y/n): ").lower().strip()

    if again == "y":
        TerminalCode()
    else:
        print("Thanks for your play. See you next time.")

TerminalCode()
    

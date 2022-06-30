print("Hello")
play = input("Would you like to play a game?")

number = 29

if play == "yes":
    play = True
else : play = False; print("You have chosen not to play!")

while play :
    guess = int(input("Please guess an integer:"))
    if guess < number:
        print(f"It appears to be higher than {guess}")
    elif guess > number :
        print(f"It appears to be lower than {guess}")
    else :
        print(f"Congratulations! - You have guessed the number -> {number}")
        play = False
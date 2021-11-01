import random
A=random.randrange(1,100)
I=int(input("Guess the number?:"))
Guesses=1
while I!=A and Guesses<=10:
    if I> A:
        print("THe number you guessed is higher than the actual guessing number")
    else:
        print("The number you guessed is smaller than the actual guessing number")
    I=int(input("Guess Again"))
    Guesses+=1
if I==A:
    print("You have guessed the wright number in",Guesses,"guesses")
else:
    print("You lose the game")

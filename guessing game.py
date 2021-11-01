import random
A=random.randrange(1,99)
D=int(input("Enter Number:"))
guesses=1
while guesses<10 and D!=A:
    guesses+=1
    if D>A:
        print("you have guessed a wrong number and the number is bigger than the actual number")
    else:
        print("You have guessed a wrong number and the number is smaller than the actual number ")
    D=int(input("Guesses again"))
if D==A:
    print("You have guessed the number in",guesses,"guesses")
else:
    print("You lose the game")

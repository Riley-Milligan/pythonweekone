import random

random.seed()

to_guess = random.randrange(1, 10)

guess = "10"

while int(guess) != to_guess:
    guess = input("Please guess a number 1-9")
    if int(guess) == to_guess:
        print("your guess was correct")
    elif int(guess) > 9:
        print("your guess was out of range")
    else:
        print("Your guess was not correct")

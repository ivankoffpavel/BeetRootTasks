#The Guessing Game.
#Write a program that generates a random number between 1 and 10 and lets the user guess what number was/
# generated. The result should be sent back to the user via a print statement.
import random
while "Good":
    num_quess=int(input('Input a number from 0 to 10  '))
    num_random=random.randint(0,10)
    if num_quess == num_random:
        print("You guessed right!!! Congratulations!!!")
    else:
        print("Not right,try again!")
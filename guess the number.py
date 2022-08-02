import random


comp_number = random.randrange(0 ,21)

guess_number = input("guess the cprrect the number ")
guess_number = int(guess_number)

if comp_number == guess_number:
    print(" the number entered is the correct number")

elif comp_number < guess_number:
    print("the number you have guessed is greater than the random number ")
elif comp_number > guess_number:
    print("the number you have guessed is lesser than the random number")

import random

def guess_number(x):
    hidden_number = random.randint(1,x)

    your_input = 0
    while your_input != hidden_number:
        your_input = int(input("Enter number : "))

        if your_input < hidden_number:
            print("Too low. Try again ")

        if your_input > hidden_number:
            print("Too high. Try again")

    print("You Won")

guess_number(20)
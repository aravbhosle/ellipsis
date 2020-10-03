import random


def guess_comp_num():
    comp_num = random.randint(1, 10)
    while True:
        guess = int(input("Pick a number from 1-10: "))
        if guess == comp_num:
            print("You guess it correctly!")
            break
        else:
            print("You didn't guess my number")


print(guess_comp_num())

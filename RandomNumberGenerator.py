import random


version = 0.01

i = 0
r = random.randint(0,10)

def lives():
    amt = input("How many lives do you want?")
    return amt

def guess():
    guess = 1int(input("What is your guess 0-10?"))
    return guess

def check(r, g, i):
    num = r
    live = i
    if g == num:
        print("You won!")
    elif g == "":
        print("seriously...?")
        i -= 1
        return i
    else:
        print("Wrong!")

l = int(lives())

while i < l:
    g = guess()
    check(g, r, i)
    i += 1
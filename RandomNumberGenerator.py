i = 0

def lives():
    amt = input("How many lives do you want?")
    return amt

def guess():
    guess = int(input("What is your guess?"))
    return guess

def check(g):
    num = 10
    if g == num:
        print("You won!")
    else:
        print("Wrong!")

l = int(lives())

while i < l:
    g = guess()
    check(g)
    i += 1
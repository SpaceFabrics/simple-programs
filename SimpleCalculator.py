version = 0.01

def numbers():
    n1 = int(input("What is the first number?"))
    n2 = int(input("What is the second number?"))
    return n1, n2

def addition(num1, num2):
    a1 = int(num1 + num2)1
    print("the result is:", a1)

num1, num2 = numbers()
addition(num1, num2)


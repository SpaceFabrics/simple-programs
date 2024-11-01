version = 0.01 #Work in progress

def getNumber():
    n1 = float(input("What is your number?"))
    return n1

def cal(num1):
    a1 = float(num1)
    
    if (a1 * 1) == 0:
        print("Number is Even")
    else:
        print("Number is odd")


num1 = getNumber()
cal(num1)
version = 0.01

def getTemps():
    temp = float(input("input temperature value"))
    unit = input("C or F?")
    return unit, temp

def tempSelect(unit, temp):
    if unit == "C":
        result = calc(temp)
        print(result)
    else:
        result = calf(temp)
        print(result)

def calc(temp):
    answr = float((temp * (9/5)) + 32)
    return answr

def calf(temp):
    answr = float((temp - 32) * (5/9))
    return answr

unit, temp = getTemps()
tempSelect(unit, temp)


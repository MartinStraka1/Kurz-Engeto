"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Martin Straka
email: martin.b.straka@gmail.com
discord: martinstraka_93260
"""
import random
print("Hi there!")
print("-"*50)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print("-"*50)
sortuj = str()
ranStr = str()
ranCelk = str("")
ranInt = int()
problem = bool(False)
while problem == False:
    problem = True
    for i in range (0, 4):
        ranInt = random.randrange(1,10)
        ranStr = str(ranInt)
        ranCelk = ranCelk + ranStr
    sortuj = ''.join(sorted(ranCelk))
    c = str("")
    for i in sortuj:
        if c == i:
            problem = False
            ranCelk = ""
            break
        else: problem = True
        c = i
problem = False
tip = str()
bulls = int
cows = int
poc = int(0)
str4 = "Inserted value doesn't have 4 characters."
number = "Inserted value is not a number."
same = "Inserted value has at least 2 characters equal."
first0 = "Inserted value has first character = 0."
mistake = "You have made following mistake(s):"
while bulls != 4:
    while problem == False:
        if poc == 0:
                print("Enter a number")
        tip = input(">>>")
        problem = True
        if len(tip) != 4:
            if problem == True:
                problem = False
                print(mistake)
            print(str4)
        if tip.isnumeric() == False:
            if problem == True:
                problem = False
                print(mistake)
            print(number)
        c = str(" ")
        sortuj = ''.join(sorted(tip))
        for i in sortuj:
            if c == i:
                if problem == True:
                    problem = False
                    print(mistake)
                print(same)
                break
            else: c = i
        if tip[0] == "0":
            if problem == True:
                problem = False
                print(mistake)
            print(first0)
        else: 
            if problem == True:
                poc += 1
    bulls = 0
    cows = 0
    for i in tip:
        for j in ranCelk:
            if i == j and tip.index(i) == ranCelk.index(j):
                bulls += 1
            if i == j and tip.index(i) != ranCelk.index(j):
                cows += 1
    if bulls < 4: 
        problem = False
        print(bulls," bulls, ",cows," cows")
        print("-"*50)
    else:
        print("Correct, you've guessed the right number\nin",poc,"guesses!!")
        print("-"*50)
        print("That's amazing!!")

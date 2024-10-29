"""
projekt_1_py: první projekt do Engeto Online Python Akademie

author: Martin Straka
email: martin.b.straka@gmail.com
discord: martinstraka_93260
"""
TEXTS = ['''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

uzivatele = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123"
}
jmeno = input("Insert username: ")
jmeno = jmeno.lower()
heslo = input("Insert password: ")
print("-"*45)
platne = jmeno in uzivatele
if platne == True:
    if heslo != uzivatele.get(jmeno):
        platne = False
if platne == False:
    print("Unregistered user or wrong password inserted. Terminating the program. ")
elif platne == True:
    print("Welcome to the app, ", jmeno,".")
    print("We have 3 texts to be analyzed. ")
    print("-"*45)
    vyberTextu = ("1", "2", "3")
    kteryText = input("Enter a number btw. 1 and 3 to select: ")
    print("-"*45)
    jeVseznamu = kteryText in vyberTextu
    if kteryText.isnumeric() == True and jeVseznamu == False:
        print("Inserted number out of range. Terminating the program. ")
    if kteryText.isnumeric() == False:
        print("Inserted value is not a number. Terminating the program. ")
    if kteryText.isnumeric() and jeVseznamu == True:
        kteryText = int(kteryText)-1
        textAn = TEXTS[kteryText]
        textAn = textAn.split()
        delkaT = len(textAn)
        capLet = int(0)
        capAll = int(0)
        smallAll = int(0)
        isNum = int(0)
        sumNum = int(0)
        maxLen = int(0)
        for i in textAn:
            if len(i)>maxLen:
                maxLen = len(i)
            if i[0].isupper():
                capLet +=1
            if i[:].isupper():
                capAll +=1
            if i[:].islower():
                smallAll +=1
            if i.isnumeric() == True:
                isNum +=1
            if i.isnumeric() == True:
                sumNum = sumNum + int(i)
        print("There are",delkaT,"words in the selected text.")
        print("There are",capLet,"titlecase words.")
        print("There are",capAll,"uppercase words.")
        print("There are",smallAll,"lowercase words.")
        print("There are",isNum,"numeric strings.")
        print("The sum of all the numbers",sumNum,".")
        print("-"*45)
        print("LEN|      OCCURRENCES      |NR.")
        print("-"*45)
        wordsCount = int(0)        
        for i in range(1, maxLen+1):
            for a in textAn:
                if len(a) == i:
                    wordsCount += 1
            print((2-len(str(i)))*" ",i,"\b|",wordsCount*"*",(20-wordsCount)*" ","|",wordsCount)
            wordsCount = 0
            



        










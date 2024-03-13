import sys
import random


print("-------------   Guess Number Game    -------------")
print("Please input two Number.One is minmum number , the Other is maximum number.")
print("This game is finding number which system creates between minimum number and maximum number")
print('''
      ''')

minNumber = input("Input Minimum Number : ")
maxNumber = input("Input Maximum Number : ")

if not minNumber.isdigit():
    print(minNumber, " is not Numeric. Finish this game!!")
    exit()

if not maxNumber.isdigit():
    print(maxNumber, " is not Numeric. Finish this game!!")
    exit()

if int(minNumber) > int(maxNumber):
    print("WrongNumber. You must input numbers that minimumNumber is smaller than maximumNumber. ")
    exit()

maxTryNumber = input("Max Guess Count : ")
while maxTryNumber.isdigit() is not True:
    print("Guess count is not Numeric. Please input again.")
    maxTryNumber = input("Max Guess Count : ")

expectedNumber = random.randint(int(minNumber),int(maxNumber))

i = 1

while i <= int(maxTryNumber):
    print("Try ", i , " Challenge. Guess Number : ")
    guessNumber = input() 

    if expectedNumber == guessNumber:
        print("Congratuation!! expectedNumber is " , expectedNumber)
        print("Finish game")
        exit() 
    else:
        print("Guess Number ", guessNumber , " is Wrong.Try again!")
    i += 1

print("Try count is Over. Right Number is " , expectedNumber , ".","Try again this game. Bye!")

########################################################################
##
## CS 101 Lab
## Program #3
## Name: Brady maes
## Email: bpmynv@umsystem.edu
##
## PROBLEM : The code must create a game called Flarsheim Guesser that finds out what number the user is thinking about (from the inclusive range of 1 to 100) from the remainders
##  when the user's number is divided by 3, 5, and 7. The game must also be within a loop that asks the user if they want to keep playing (Y or N?). If the user gives input besides
##  'Y' or 'N' (capitalization does not matter), then the program simply just asks them if they want to keep playing again. The program then quits if the user said 'N' or 'n' or it
##  plays another game if the user gave 'Y' or 'y'. Once the game is being played, it asks the user to think of a number between and including 1 and 100. The program then asks the
##  user for the remainders of said number when divided by 3, 5, and 7. The program then uses a for loop from 1 to 101 (1 to 101 does not include 101 itself) to find what number 
##  has the exact 3 same remainders and displays the result to the user. Finally, the game will ask them if they'd like to play again.
##
## ALGORITHM : 
##      1. Introduce the user to the game
##      2. Determine if to continue the game, end it, or ask the user again what to do.
##      3. Ask the user to think of a number between 1 and 100.
##      4. Ask the user for the remainders of dividing their number by 3, 5, and 7
##      5. Use a loop between 1 and 101 (not including 101 itself) to find the user's number by finding the number between 1 and 100 that has the same remainders when dividing
##         by 3, 5, and 7
##      6. Display the number that matched the same remainders as the user's number
##      7. Ask the user if they would like to play again and update the loop accordingly.
##      
## 
## ERROR HANDLING:
##      If the user does not give an integer for some of the inputs, a type error might occur. Additionally, the program will not work if the user does not select a number between
##      1 and 100.
##
## OTHER COMMENTS:
##      N/A
##
########################################################################
gameCondition = 'Y'
print('Welcome to the Flarsheim Guesser!')
while gameCondition !='N' and gameCondition != 'n':
    if gameCondition != 'Y' and gameCondition != 'y':
        gameCondition = input("Do you want to play again? Y to continue, N to quit ==> ")
        continue
    print()
    print('Please think of a number between and including 1 and 100\n')
    remainder1 = int(input("What is the remainder when your number is divided by 3? "))
    while remainder1 != 0 and remainder1 != 1 and remainder1 != 2:
        if remainder1 < 0:
            print("The value entered must be 0 or greater") 
            remainder1 = int(input("What is the remainder when your number is divided by 3? "))
        elif remainder1 > 2:
            print("The value entered must be less than 3") 
            remainder1 = int(input("What is the remainder when your number is divided by 3? "))
    print()
    remainder2 = int(input("What is the remainder when your number is divided by 5? "))
    while remainder2 != 0 and remainder2 != 1 and remainder2 != 2 and remainder2 != 3 and remainder2 != 4: 
        if remainder2 < 0:
            print("The value entered must be 0 or greater") 
            remainder2 = int(input("What is the remainder when your number is divided by 5? "))
        elif remainder2 > 4:
            print("The value entered must be less than 5") 
            remainder2 = int(input("What is the remainder when your number is divided by 5? "))
    print()
    remainder3 = int(input("What is the remainder when your number is divided by 7? "))
    while remainder3 != 0 and remainder3 != 1 and remainder3 != 2 and remainder3 != 3 and remainder3 != 4 and remainder3 != 5 and remainder3 != 6: 
        if remainder3 < 0:
            print("The value entered must be 0 or greater") 
            remainder3 = int(input("What is the remainder when your number is divided by 7? "))
        elif remainder3 > 6:
            print("The value entered must be less than 7") 
            remainder3 = int(input("What is the remainder when your number is divided by 7? "))
    for i in range(1, 101):
        DetermRemainder1 = i % 3
        DetermRemainder2 = i % 5
        DetermRemainder3 = i % 7
        if(remainder1 == DetermRemainder1) and (remainder2 == DetermRemainder2) and (remainder3 == DetermRemainder3):
            result = i
            break
    print("Your number was", result)
    print("How amazing is that?\n")
        
    gameCondition = input("Do you want to play again? Y to continue, N to quit ==> ")


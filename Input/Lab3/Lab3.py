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


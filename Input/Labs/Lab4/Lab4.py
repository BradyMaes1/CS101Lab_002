########################################################################
##
## CS 101 Lab
## Program #3
## Name: Brady maes
## Email: bpmynv@umsystem.edu
##
## PROBLEM : The code must create multiple different functions and combine them in order to make a slot machine game. The game will ask the user how many chips that they'd like to
##           start with and then ask them how much they'd like to wager (checking to make sure they wager more than 0 and no more than the chips that they have). The game then
##           generates 3 random numbers (1 to 10) and multiplies the users chips by 10 if all 3 of the random numbers are the same. If only two are the same their chips are
##           multiplied by 3. If none of the numbers are the same then the user loses the chips that they wagered. The program tells the user the 3 random numbers, how many matches
##           that they got, and much much they won/lost. It then repeats the wagering process until the user runs out of chips and then tells the user how many spins it took before
##           they ran out of chips. It also tells the user what the maximum amount of chips that they had at a time was. Finally, the program asks the user if they would like to
##           play again and loops accordingly.
##
## ALGORITHM : 
##      1. Import random
##      2. Create the play_again function
##      3. Create the get_wager function
##      4. Create the get_slot_results function
##      5. Create the get_matches function
##      6. Create the get_bank function
##      7. Create the get_payout functions
##      8. Create the slotsGame function that puts all of the other functions together to structure and run the game. This function also creates some variables and loops to make
##         the process work successfully.
##      9. Create the Slot_UnitTests function
##      
## 
## ERROR HANDLING:
##      If the user does not give an integer for some of the inputs, a type error might occur.
##
## OTHER COMMENTS:
##      N/A
##
########################################################################
import random
def play_again():
    ans = input('Do you want to play again?: ')
    while ans.upper() != 'Y' and ans.upper() != 'YES' and ans.upper() != 'N' and ans.upper() != 'NO':
        print('You must enter Y/YES/N/NO to continue. Please try again.')
        ans = input('Do you want to play again?: ')
    if ans.upper() == 'Y' or ans.upper() == 'YES':
        return True
    else:
        return False

def get_wager(bank):
    wager = int(input('How many chips would you like to bet?: '))
    while wager <= 0 or wager > bank:
        if wager <= 0:
            print('That is not enough chips. You must wager at least 1 chip.')
        elif wager > bank:
            print('That is too many chips. You cannot wager more chips than you have.')
        wager = int(input('How many chips would you like to bet?: '))
    return wager 

def get_slot_results():
    reel1 = random.randint(1,10)
    reel2 = random.randint(1,10)
    reel3 = random.randint(1,10)
    return reel1, reel2, reel3

def get_matches(reel1, reel2, reel3):
    if reel1 == reel2 and reel2 == reel3:
        return 3
    elif reel1 == reel2 or reel1 == reel3 or reel2 == reel3:
        return 2
    else:
        return 0
  
def get_bank():
    chips = int(input('How many chips would you like to start with?: '))
    while chips < 0 or chips > 100:
        if chips < 0:
            print('That is not enough chips. Please choose a value between 1 and 100 chips.')
        else:
            print('That is too many chips. Please choose a value between 1 and 100 chips.')
        chips = int(input('How many chips would you like to start with?: '))
    return chips

def get_payout(wager, matches):
    if matches == 3:
        pay = (10 * wager) - wager
    elif matches == 2:
        pay = (3 * wager) - wager
    else:
        pay = -wager
    return pay

def slotsGame():
    spins = 0
    maxChips = 0
    gameLoop = True
    while gameLoop == True:
        bank = get_bank()
        initialBet = bank
        while bank > 0:
            wager = get_wager(bank)
            slot = get_slot_results()
            slot1 = slot[0]
            slot2 = slot[1]
            slot3 = slot[2]
            matches = (get_matches(slot1, slot2, slot3))
            payout = get_payout(wager, matches)
            bank += payout
            spins += 1
            if bank > maxChips:
                maxChips = bank
            print('You spun:', slot1, slot2, slot3)
            print('You matched', matches, 'reels')
            print('You won/lost', payout, 'chips')
            print('Current bank:', bank)
            print()
        print('You lost your', initialBet, 'chips in', spins, 'spins')
        print('The most chips you had was', maxChips, 'chips')
        gameLoop = play_again()
        print()

def Slot_UnitTests():
    play_again()
    get_wager(random.randint(1,100))
    get_bank()
    get_slot_results()
    get_matches(random.randint(1,10), random.randint(1,10), random.randint(1,10))
    get_payout(random.randint(1,100), random.randint(1,3))
    print('All functions successfully run with random values')

slotsGame()
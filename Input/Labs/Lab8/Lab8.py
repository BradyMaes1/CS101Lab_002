"""
CS 101 Lab
    Program #3
    Name: Brady maes
    Email: bpmynv@umsystem.edu

    PROBLEM: The program must offer a menu to the user for adding/removing test scores, adding/removing assignment scores, completely clearing test/assignment scores, displaying the scores, and quitting the program. It must check that the user's input is valid and do the option that
    they select. The program will keep track of the scores and weight their averages to create a composite score. When asked to display, the program should display the scores in a neatly organized table with how many of each score were given, the minimum, maximum, average, and
    standard deviation for said scores. It should also return N/A for values that were not given or could not be found.


    1. import the math module
    2. Create the function grade
        1. Create the lists that will be used throughout the code
        2. Put the menu code into a loop that continues until the user says 'q' or 'Q'. Output the menu to the user and ask them for input
        3. If the user says '1'
            1. Ask the user for a test score to add, make sure it is valid, and add it to the tests list
        4. If the user says '2'
            1. Ask the user for a test score to remove, make sure it is valid, and remove it from the tests list
        5. If the user says '3'
            1. Clear the tests list and tell the user that it was cleared
        6. If the user says '4'
            1. Ask the user for an assignment score to add, make sure it is valid, and add it to the assigns list
        7. If the user says '5'
            1. Ask the user for an assignment score to remove, make sure it is valid, and remove it from the assigns list
        8. If the user says '6'
            1. Clear the assigns list and tell the user that it was cleared
        9. If the user says 'D' or 'd'
            1. Display the scores in a neatly organized table with how many of each score were given, the minimum, maximum, average, and
    standard deviation for said scores. It should also return N/A for values that were not given or could not be found.
        10. If says 'Q' or 'q'
            1. Exit the loop and end the function
    3. Run the grade function

    ERROR HANDLING:
    If the user gives a ridicously high score it could offset everything to not make a lot of sense (but still be mathematically correct). This could be caused by a type (i.e. they enter 1001 when they mean 101)

    OTHER COMMENTS:
    N/A

"""
import math
def grade():
    tests = []
    assigns = []
    choices = ['1', '2', '3', '4', '5', '6', 'D', 'Q']
    d = ''
    x1 = True
    x2 = True
    while d != 'Q':
        tests.sort()
        assigns.sort()
        testsAvg = (sum(tests) / len(tests)) if len(tests) > 0 else 'N/A'
        assignsAvg = (sum(assigns) / len(assigns)) if len(assigns) > 0 else 'N/A'
        weighted = (testsAvg * .6) + (assignsAvg * .4) if testsAvg != 'N/A' and assignsAvg != 'N/A' else 'N/A'
        try:
            testsMin = tests[0]
            testsMax = tests[-1]
            top1 = 0
            for i in tests:
                top1 += ((i - testsAvg) **2)
            testsSTD = round(math.sqrt(top1/len(tests)), 2)
        except IndexError:
            testsMin = 'N/A'
            testsMax = 'N/A'
            testsSTD = 'N/A'
        try:
            assignsMin = assigns[0]
            assignsMax = assigns[-1]
            top2 = 0
            for i in assigns:
                top2 += ((i - assignsAvg) **2)
            assignsSTD = round(math.sqrt(top2/len(assigns)), 2)
        except IndexError:
            assignsMin = 'N/A'
            assignsMax = 'N/A'
            assignsSTD = 'N/A'
        print()
        decision = input('{:^40}'.format('Grade Menu') + '\n1 - Add Test\n2 - Remove Test\n3 - Clear Tests\n4 - Add Assignment\n5 - Remove Assignment\n6 - Clear Assignments\nD - Display Scores\nQ - Quit\n\n')
        d = decision.upper()
        while d not in choices:
            print(decision, 'is not a valid option.\n')
            decision = input('{:^40}'.format('Grade Menu') + '\n1 - Add Test\n2 - Remove Test\n3 - Clear Tests\n4 - Add Assignment\n5 - Remove Assignment\n6 - Clear Assignments\nD - Display Scores\nQ - Quit\n\n')
            d = decision.upper()
        if d == '1':
            while x1 == True:
                tScore = input('Enter the new Test score 0-100: ')
                try:
                    t1 = float(tScore)
                    if t1 < 0:
                        print(t1, 'is less than 0 and therefore cannot be entered as a grade')
                        continue
                    else:
                        tests.append(t1)
                        print()
                        break
                except ValueError:
                    print(tScore, 'is not a number')
                    continue
        if d == '2':
            remove1 = input('Enter the Test to remove: ')
            try:
                r1 = float(remove1)
                if r1 in tests:
                    tests.remove(r1)
                    print()
                else:
                    print('Could not find that score to remove')
            except ValueError:
                print(remove1, 'is not a valid score to remove')
        if d == '3':
            tests.clear()
            print('The test scores were cleared')
        if d == '4':
            while x2 == True:
                aScore = input('Enter the new Assignment score 0-100: ')
                try:
                    a1 = float(aScore)
                    if a1 < 0:
                        print(a1, 'is less than 0 and therefore cannot be entered as a grade')
                        continue
                    else:
                        assigns.append(a1)
                        print()
                        break
                except ValueError:
                    print(aScore, 'is not a number')
                    continue
        if d == '5':
            remove2 = input('Enter the Assignment to remove: ')
            try:
                r2 = float(remove2)
                if r2 in assigns:
                    assigns.remove(r2)
                    print()
                else:
                    print('Could not find that score to remove')
            except ValueError:
                print(remove2, 'is not a valid score to remove')
        if d == '6':
            assigns.clear()
            print('The assignment scores were cleared')
        if d == 'D':
            roundedTestsAvg = round(testsAvg, 2) if testsAvg != 'N/A' else 'N/A'
            roundedAssignsAvg = round(assignsAvg, 2) if assignsAvg != 'N/A' else 'N/A'
            print()
            print('{:<15}{:<10}{:<10}{:<10}{:<10}{}'.format('Type', '#', 'min', 'max', 'avg', 'std'))
            print("=" * 60)
            print('{:<15}{:<10}{:<10}{:<10}{:<10}{}'.format('Tests', len(tests), testsMin, testsMax, roundedTestsAvg, testsSTD))
            print('{:<15}{:<10}{:<10}{:<10}{:<10}{}'.format('Assignments', len(assigns), assignsMin, assignsMax, roundedAssignsAvg, assignsSTD))
            print()
            print('The weighted score is:', round(weighted, 2))
            print()


grade()
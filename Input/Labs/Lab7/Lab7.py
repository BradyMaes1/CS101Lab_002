'''
    CS 101 Lab
    Program #3
    Name: Brady maes
    Email: bpmynv@umsystem.edu

    PROBLEM: The program must read a file and section off its text into lists in order to seperate different vehicles from the text into lists. The program will first ask for a mile per gallon (mpg) minimum that the user is interested in. It'll then ask for an input file and determine
    whether the file is valid or not. It'll then proceed to ask for an output file and determine if that file is a valid file or not. After making sure both files are valid, the program will then add all vehicles from the input file that satisfy the previous mpg standard to the 
    output file with a specific format (looks like a table). If the mpg paramater in the input file is invalid the program will say so and point out what vehicle the error occured on.

    ALGORITHIM:
    1. Creat mpg() function to correctly ask users for their
    '''
import csv
def mpg():
    x = True
    while x == True:
        try:
            minMPG = int(input('Enter the minimum mpg: '))
            if minMPG < 1:
                print('Fuel economy given must be greater than 0')
                continue
            elif minMPG >= 100:
                print('Fuel economy must be less than 100')
            else:
                x = False
        except ValueError:
            print("You must enter an integer for the fuel economy")
            continue
    return minMPG

def primary():
    minMPG = mpg()
    y = True
    x = True
    while y == True:
        try:
            l1 = []
            file1 = input('Enter the name of the input vehicle file: ')
            with open(file1, 'r') as cFile:
                read1 = csv.reader(cFile, delimiter='\t')
                for i in read1:
                    l1.append(i)
                    y = False
        except FileNotFoundError:
            print('Could not open file', file1)
        except OSError:
            print('Invalid input file (OS Error)', file1)
        except IOError:
            print('Invalid input file (IO Error)', file1)

    while x == True:        
        try:
            file2 = input('Enter the name of the file to output to: ')
            l2 = []
            with open(file2, 'w') as cFile:
                for i in l1[1:]:
                    try:
                        if int(i[7]) >= minMPG:
                            l2.append(i)
                    except ValueError:
                        print('Could not convert value', i[7], 'for vehicles', i[0], i[1], i[2])
                for x in l2:
                    year = x[0]
                    make = x[1]
                    model = x[2]
                    mileage = x[7]
                    print('{:<5}{:<20}{:<40}{}'.format(str(year), make, model, str(mileage)))
                    cFile.write(('{:<5}{:<20}{:<40}{}'.format(str(year), make, model, str(mileage))))
                x = False

                
        except FileNotFoundError:
            print('File Not Found')
        except OSError:
            print('Invalid output file (OS Error)', file2)
        except IOError:
            print('Invalid output file (IO Error)', file2)


primary()
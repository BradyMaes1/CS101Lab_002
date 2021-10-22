'''
Name: Brady Maes
Lab: Caesar Cipher

Summary: The program will give the user the option of encoding, decoding, or quitting the program. If they encode, it will ask the user for a message and a shift value and then proceed to shift their message alphabetically by said shift value. If they decode, it will ask them for a string to decode and a shift value and then proceed to decode their value by shifting it alphabetically by said shift value (backwards this time). If they decide to quit, the program will thank them and end.

Algorithim:
1. The program will ask the user what they would like to do (encode, decode, or quit)
2. The program will use if statements to go to the option that the user selects
3. If the user said to encode:
  1. The program will ask the user for a string to encode and a shift value
  2. The program will make sure that both inputs were valid and loop back and ask again if they weren't
  3. The program will encode the message based on their shift value
  4. The program will display the user's original and encoded message
  5. The program will ask the user what they would like to do (encode, decode, or quit)
4. If the user said to decode:
  1. The program will ask the user for a string to decode and a shift value
  2. The program will make sure that both inputs were valid and loop back and ask again if they weren't
  3. The program will decode the message based on their shift value
  4. The program will display the user's original and decoded message
  5. The program will ask the user what they would like to do (encode, decode, or quit)
5. If the user said to quit:
  1. The program will say 'Caesar Thanks You!'
  2. The program will exit
'''

#Function is defined
def EtTuBrute():
  #Asks user what they'd like to do
  inp = input("Say 'e' to encode, 'd' to decode, or 'q' to quit: ")
  #Sets c1 to 0 to later be used in a loop that makes sure that user satisfies the cipher requirements
  c1 = 0
  #Will loop continously until the user says 'q' or 'Q'
  while inp.upper() != 'Q':
    #Starts the encoding part of code if the user said 'e' or 'E'
    if inp.upper() == 'E':
      #Will keep looping until the user gives a valid message and shift
      while c1 < 2:
        c1 = 0
        #Asks the user for a message
        original = input('Enter the string to encode: ')
        #Checks that the message is letters only and will warn the user if it isn't
        if original.isalpha():
          c1+=1
        else:
          print("Please only enter a string made of letters to encode")
          print()
          continue
        #Checks that the shift is an integer between 1 and 25 (inclusive) and warns the user if it isn't
        try:
          shift = int(input('Enter the amount to shift: '))
          if shift >= 1 and shift <= 25:
            c1+=1
          else:
            print('Please enter a positive integer between 1 and 25 for the shift key')
            print()
            continue
        except:
          print('Please enter a positive integer between 1 and 25 for the shift key')
          print()
        #Creates a list from the user's original message to iterate through
        list1 = list(original)
        #Creates a placeholder string named 'encoded' to later be concatenated to
        encoded = ''
        #Iterates through the elements in the list made of characters from the user's message input
        for i in list1:
          #Sets lowerC to False by default to be later changed if the character is lowercase
          lowerC = False
          #If the user gives a lowercase character, it will be temporarily converted to an uppercase character
          if not(i.isupper()):
            temp = i.upper()
            #lowerC is set to True to later be used to convert the shifted character to lower case
            lowerC = True
          #If the character is upper case, no significant change is made besides setting temp (temporary) to i
          else:
            temp = i
          #asc is given the ascii value of the letter shifted by the shift variable. The % 26 part of the code will make it so that letters can wrap around the alphabet succesfully. asc will then be converted back to a letter with ord() so that it can be concatenated to 'encoded'
          asc = (ord(temp) + shift - 65) % 26 + 65
          asc = chr(asc)
          #If the letter was lowercase earlier, it is converted back to lowercase
          if lowerC == True:
            asc = asc.lower()
          #The shifted character is concatenated to the string 'encoded'
          encoded += asc
        #The messages are printed to the user with the original and encoded strings
        print('Original Message:', original)
        print('Encoded Message:', encoded)
        print()
      #The program asks the user what they would like to do again and sets c1 back to 0 to prevent logic errors
      inp = input("Say 'e' to encode, 'd' to decode, or 'q' to quit: ")
      c1 = 0
    #Starts the decoding part of code if the user said 'd' or 'D'
    #!!! This code is almost entirely the same to the code above for encoding string besides some minor variable name changes and output message changes (so that it doesn't confuse the user what it is doing). !!!
    # The only significant change in the deocoding block of code is on line 126, please refer to there.
    elif inp.upper() == 'D':
      while c1 < 2:
        c1 = 0
        original = input('Enter the string to decode: ')
        if original.isalpha():
          c1+=1
        else:
          print("Please only enter a string made of letters to decode")
          print()
          continue
        try:
          shift = int(input('Enter the amount to shift: '))
          if shift >= 1 and shift <= 25:
            c1+=1
          else:
            print('Please enter a positive integer between 1 and 25 for the shift key')
            print()
            continue
        except:
          print('Please enter a positive integer between 1 and 25 for the shift key')
          print()
        list1 = list(original)
        decoded = ''
        for i in list1:
          lowerC = False
          if not(i.isupper()):
            temp = i.upper()
            lowerC = True
          else:
            temp = i
          #This part of the code is different from the encoding block of code in that it subtracts the shift value instead of adding it. This will result in the code shifting backwards instead of forwards (as needed for decoding).
          asc = (ord(temp) - shift - 65) % 26 + 65
          asc = chr(asc)
          if lowerC == True:
            asc = asc.lower()
          decoded += asc

        print('Encoded Message:', original)
        print('Decoded Message:', decoded)
        print()
      inp = input("Say 'e' to encode, 'd' to decode, or 'q' to quit: ")
      c1 = 0
  #This else statement will warn the user if they do not say some form of 'e', 'd', or 'q' and ask them for input again (as well as continuing so that the code will skip to the beginning of the while loop)
    else:
      print('Invalid option')
      inp = input("Say 'e' to encode, 'd' to decode, or 'q' to quit: ")
      continue
  #Once the user says some form of 'q', the pgroams thanks them
  else:
    print('Caesar Thanks You!')

#Function is excecuted
EtTuBrute()

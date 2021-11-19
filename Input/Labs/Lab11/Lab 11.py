"""

    CS 101 Lab
    Program #3
    Name: Brady maes
    Email: bpmynv@umsystem.edu

    PROBLEM: A Clock class needs to be made to output a time based on the parameters of its' objects. A ClockProgram function also needs to be made
    that will use the Clock class and user input to create an object of the Clock class. The ClockProgram function will also ask the user for how many
    ticks that the time that they gave to tick up by. Using the time module, the program will output the time ticking up by 1 second (per second) until
    it fufills the amount of ticks.

    ALGORITHIM:
    1. import time
    2. Create Clock class
        1. Create the __init__ function to set the hours, minutes, seconds, and clock type
        2. Create the functions for individually displaying the hours, minutes, seconds, and clock_type (getter functions)
        3. Create the functions for individually changing the hours, minutes, seconds, and clock_type (setter functions)
        4. Create the tick function
            1. Add 1 to the seconds variable. 
            2. If seconds becomes 60 or greater, add 1 to the minutes varaible and set the seconds function to 0
            3. If minutes becomes 60 or greater, add 1 to the hours variable and set the minutes function to 0
        5. Create the __str__ function (for displaying the time)
            1. Create variable placeholders for hours, minutes, and seconds to be used later in the code for convience purposes
            2. If the type of clock is 0, return the time in the 00 format (using :02)
            3. If the type of clock is 1:
                1. Set timeMarker to 'PM' if dividing the hours by 12 results in something greater than or equal to 1. Else if the result of dividing hours
                by 12 results in something less than one, set timeMarker to 'AM'
                2. If the hours are greater than 12, set the placeholder standardHours to hours - 12
                3. If the hours are equal to 0, set the placeholder standardHours to 0
                4. Else, set the placeholder standardHours equal to hours
                5. Return the time in the 00 format using standardHours instead of hours and adding to timeMarker to the end (AM or PM)
            4. Else return 'Invalid clock type' (if the clock type wasn't 0 or 1)
        6. Create the ClockProgram function
            1. Get the user's input to determine the hours, minutes, seconds, type, and ticks. 
            2. Create an object of the Clock class (called 'clock1' in this instance) using the user's input for hours, minutes, seconds, and type
            3. Display clock1 to the user
            4. Create a for loop for the range of the ticks given by the previous user input
                1. Call the tick function from the Clock class on the object clock1 with clock1.tick()
                2. Use the time module to make the program wait for 1 second with time.sleep(1)
                3. Dispaly the updated version of clock1 to the user
        
    ERROR HANDLING: If the user gives invalid inputs for the hours, minutes, or seconds, the program might behave oddly and display non-existent times
    because the user gave non-existent times. This could also confuse the AM/PM math for standard time. Also if the user gives non-integer inputs it
    could raise errors.

    OTHER COMMENTS: N/A

"""
import time
class Clock():
    def __init__(self, hours = 0, minutes = 0, seconds = 0, type = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.type = type

    def hour(self):
        print(self.hours)

    def minute(self):
        print(self.minutes)

    def second(self):
        print(self.seconds)
    
    def clock_type(self):
        print(self.type)

    def changeHour(self, newHour):
        self.hours = newHour
    
    def changeMinute(self, newMinute):
        self.minutes = newMinute

    def changeSecond(self, newSecond):
        self.minutes = newSecond

    def change_clock_type(self, newType):
        self.type = newType

    def tick(self):
        self.seconds +=1
        if self.seconds >= 60:
            self.minutes += 1
            self.seconds = 0

        if self.minutes >= 60:
            self.hours +=1
            self.minutes = 0

    def __str__(self):
        h = int(self.hours)
        m = int(self.minutes)
        s = int(self.seconds)
        if self.type == 0:
            return("{:02}:{:02}:{:02}".format(h, m , s))
        elif self.type == 1:
            if self.hours / 12 >= 1:
                timeMarker = 'PM'
            elif self.hours / 12 < 1:
                timeMarker = 'AM'
            if self.hours > 12:
                standardHours = int(self.hours - 12)
            elif self.hours == 0:
                standardHours = 12
            else:
                standardHours = self.hours
            return("{:02}:{:02}:{:02}".format(standardHours, m , s) + ' ' +  str(timeMarker))
            
        else:
            return('Invalid clock type')
    
def ClockProgram():
    h1 = int(input('What is the current hour?: '))
    m1 = int(input('What is the current minute?: '))
    s1 = int(input('What is the current second?: '))
    t1 = int(input('Enter 0 for Military Time (24 hr) or enter 1 for Standard Time: '))
    ticks = int(input('How many ticks would you like to go up by?: '))
    clock1 = Clock(h1, m1, s1, t1)
    print(clock1)
    for i in range(ticks):
        clock1.tick()
        time.sleep(1)
        print(clock1)

ClockProgram()
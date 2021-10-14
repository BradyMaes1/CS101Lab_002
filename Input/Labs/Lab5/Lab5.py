import string
def get_school(s):
    school =''
    schools = ['School of Computing and Engineering SCE', 'School of Law', 'College of Arts and Sciences']
    if s >= 1 and s <= 3:
        school = schools[s-1]
    else:
        school = 'Invalid School'
    return school
def get_grade(g):
    grade =''
    grades = ['Freshmen', 'Sophmore', 'Junior', 'Senior']
    if g >= 1 and g <= 4:
        grade = grades[g-1]
    else:
        grade = 'Invalid Grade'
    return grade

def character_value(c):
    num = string.ascii_uppercase.index(c)
    return num

def get_check_digit(d):
    list1 = list(d)
    dig = 0
    for i in range(0, 5):
        dig += character_value(list1[i]) * (i +1)
    for i in range(5,9):
        dig += int(list1[i]) * (i+1)
    dig = dig % 10
    return dig

def verify_check_digit(n):
    message = ''
    check = True
    counter = 0
    counter1 = 7
    holder = True
    holder1 = True
    holder2 = True
    holder3 = True
    holder4 = True
    holder5 = True
    ls = 0
    ls1 = 0
    y = 0
    while y == 0:
        if len(n) != 10:
            check = False
            message = 'The length of the number given must be 10'
            holder = False
            y+=1
            break
        for i in n[:4]:
            counter += 1
            if (not(i.isalpha()) or i != i.upper()) and holder == True:
                check = False
                message = 'The first 5 characters must be A-Z, the invalid character is' + ' ' + str(i) + ' ' +  'at index' + ' ' + str(counter - 1)
                holder1 = False
                y+=1
                ls = 1
                break
        if ls == 1:
            break
        if not(int(n[5:6]) == 1 or int(n[5:6]) == 2 or int(n[5:6]) == 3) and holder == True and holder1 == True:
            check = False
            message = 'The sixth character must be 1, 2, or 3'
            holder2 = False
            y+=1
            break
        elif not(int(n[6:7]) == 1 or int(n[6:7]) == 2 or int(n[6:7]) == 3 or int(n[6:7]) == 4) and holder == True and holder1 == True:
            check = False
            message = 'The seventh character must be 1, 2, 3, or 4'
            holder3 = False
            y+=1
            break
        for i in n[7:10]:
            counter1 += 1
            if (not(i.isnumeric()) and holder == True and holder1 == True and holder2 == True and holder3 == True):
                check = False
                message = 'The last 3 characters must be 0-9, the invalid character is'+ ' ' +  str(i)+ ' ' +  'at index' + ' ' +  str(counter1 - 1)
                holder4 = False
                y+=1
                ls1 = 1
                break
        if ls1 == 1:
            break
        if(holder == True and holder1 == True and holder2 == True and holder3 == True and holder4 == True) and get_check_digit(n) != int(n[9:10]):
            check = False
            message = 'Check Digit'+ ' ' +  str(n[9:10])+ ' ' +  'does not match calculated value'+ ' ' +  str(get_check_digit(n))
            holder5 = False
            y+=1
            break
        if(holder == True and holder1 == True and holder2 == True and holder3 == True and holder4 == True and holder5 == True):
            check = True
            message = ''
            y+=1
            break
    return check, message

def card():
    print('{:^51}'.format('Linda Hall'))
    print('{:^51}'.format('Library Card Check'))
    print('=' * 51)
    print()
    loop = input('Enter Library Card. Hit Enter to Exit ==> ')
    while loop != '':
        val = verify_check_digit(loop)
        if val[0] == False:
            print('Library card is invalid')
            print(val[1])
        else:
            print('The Library card is valid')
            sch = loop[5:6]
            school = get_school(int(sch))
            gr = loop[6:7]
            grade = get_grade(int(gr))
            print('The card belongs to a student in', school)
            print('The card belongs to a', grade)
        print()
        loop = input('Enter Library Card. Hit Enter to Exit ==> ')

card()



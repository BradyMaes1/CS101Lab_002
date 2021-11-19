import csv

def month_from_number(x):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    try:
        month = months[x-1]
        return month
    except ValueError:
        return('Error, Month must be 1-12') 

def read_in_file(f):
    l1 = []
    with open(f, 'r', encoding='utf-8-sig') as cFile:
        read1 = csv.reader(cFile)
        for i in read1:
            l1.append(i)
    return l1

def create_reported_date_dict(list1):
    dates = {}
    del list1[0]
    for i in (list1):
        date = i[1]
        if date in dates:
            dates[date] +=1
        else:
            dates[date]= 1
    return dates

def create_reported_month_dict(list1):
    dates = {}
    del list1[0]
    for i in (list1):
        month = i[1][0:2]
        if month in dates:
            dates[month] +=1
        else:
            dates[month]= 1
    return dates
def create_offense_dict(list1):
    dates = {}
    del list1[0]
    for i in (list1):
        date = i[7]
        if date in dates:
            dates[date] +=1
        else:
            dates[date]= 1
    return dates

def create_offense_by_zip(list1):
    del list1[0]
    crimeList = []
    d1 = {}
    d2 = {}
    for x in list1:
        if x[7] not in crimeList:
            crimeList.append(x[7])
    
    for c in crimeList:
        for i in list1:
            if i[7] == c:
                if i[13] in d2:
                    d2[i[13]] +=1
                else:
                    d2[i[13]] = 1
        d1[c] = d2
        d2 = {}
    return d1
        


x1 = read_in_file('KCPD_Crime_Data_2019.csv')
print(create_offense_by_zip(x1))


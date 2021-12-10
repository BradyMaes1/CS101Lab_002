import math

def total(l1):
    count = 0
    for i in l1:
        count += i
    return count

def average(values1):
    c = total(values1)
    if len(values1) == 0:
        avg = math.nan
    else:
        avg = round(c/len(values1), 5)
    return avg

def median(l1):
    l2 = l1.copy()
    l2.sort()
    if len(l2) == 0:
        raise ValueError
    elif len(l2) % 2 == 0:
        middleIndex1 = (len(l2) // 2) - 1
        middleIndex2 = middleIndex1 + 1
        med = round((l2[middleIndex1] + l2[middleIndex2]) / 2, 2)
    else:
        middleIndex = len(l2) // 2
        med = l2[middleIndex]

    return med

#!/usr/bin/env python3.7

allGuests = {'Alice':{'Apples': 5, 'Apple Pie': 3, 'Pretzels': 3},
             'Bob':{'Ham Sandwiches': 17, 'Apples': 3},
             'Carol':{'Cups': 3, 'Apple Pie': 2 }
        }

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of items brought: ')
print(' - Apples          ' + str(totalBrought(allGuests, 'Apples')))
print(' - Apple Pie       ' + str(totalBrought(allGuests, 'Apple Pie')))
print(' - Pretzels        ' + str(totalBrought(allGuests, 'Pretzels')))
print(' - Ham Sandwiches  ' + str(totalBrought(allGuests, 'Ham Sandwiches')))
print(' - Cups            ' + str(totalBrought(allGuests, 'Cups')))
print(' - Apple Pie       ' + str(totalBrought(allGuests, 'Apple Pie')))

import random
from random import *



#list creator
def createList(x):
    for i in range (0,listLength):
        rand = randint(0,1000)
        #print(rand)
        randomList.append(rand)
    randomList.sort()
    print(f'Here is your list: {randomList}')

def binarySearch(list, low, high, num):
    #declare variables to compare
    
    #print high low mid and number
    print(f'The number you chose to search for is: {num}')

    mid = round((low+high)/2)

    print(mid)
    if high>=low:
        if list[mid] == num:
            return num
        elif list[mid] < num:
            return binarySearch(randomList, mid+1, high, number)
        else:
            return binarySearch(randomList, low, mid-1, number)
    else:
        return -1

   
        


        


#list Declarationa
randomList = []

#input gather list
try:
    listLength = int(input('Insert how long you want your list to be: '))
    createList(listLength)
except:
    print('need to enter a number!')
    

#Input for number to search for in list
try:
    number = int(input('Insert a number to search for in our random list: '))
except:
    print('Must enter a number!')

result = binarySearch(randomList, 0, len(randomList)-1, number)

if result != -1:
    print('The number is found! At index ' + str(randomList.index(result)))
else:
    print('number not found')



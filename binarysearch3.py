import random
from random import *
import tkinter
from tkinter import messagebox
from tkinter import *


randomList = []


def main():
    global listSize
    global number
    listSize = int(input('Enter a size for your list: '))
    number = int(input('Enter a number to search for! '))
    

    createList(listSize)
    print(randomList)

    result = binarySearch(randomList, number)

    if result != -1:
        print('found')
    else:
        print('not found')


def createList(x):
    for i in range(0,listSize):
        rand = randint(0,100)
        randomList.append(rand)
    randomList.sort()

        
def binarySearch(listvar,num):
    l = 0
    h = len(randomList) - 1
    
    
    numConvert = int(num)
    while h >= l:
        mid = round((l+h)/2)


        if listvar[mid] == numConvert:
            return num
            break
        elif listvar[mid] > numConvert:
            h = mid - 1
        elif listvar[mid]< numConvert:
            l = mid +1
    if h<l:
        return -1

    


if __name__ == '__main__':
    main()
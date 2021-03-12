import random
from random import *
#from search.random import *

def search(alist, x):
    for i in range(len(alist)):
        if alist[i] == x:
            return True
    return False



xinput = int(input('Enter a number'))


randomList = []

for i in range (0,50):
    rand = randint(0,100)
    #print(rand)
    randomList.append(rand)

if search(randomList, xinput):
    print('Success')
else:
    print('no sucess')

print(len(randomList))




    

#for i in randomList:
        #if i == randomList[i]:
        #print('Number is in list!')
        #break
    #else:
        #print('does not exist in list')



print(randomList)
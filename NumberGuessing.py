from random import *

n = randint(0,10)
tries = 10
print('you get 10 tries to figure it out.')
numberGuess = int(input('Guess what the number is here: '))

while n != 'numberGuess':
    if (tries > 1):
        if numberGuess <= 100:
            if (numberGuess < n):
                tries += -1
                print('Number is too low! Try again! You now have ' + str(tries) + ' left')
                numberGuess = int(input('Guess what the number is here: '))
            elif (numberGuess > n):
                tries += -1
                print('Number is too high! Try again! You now have ' + str(tries) + ' left')
                numberGuess = int(input('Guess what the number is here: '))
            else:
                break
        else:
            print('cannnot be over 100! Try again.')
            numberGuess = int(input('Guess what the number is here: '))
    else:
        print('You could not guess! Start over...')
        exit()




print('you did it! You guessed the number ' + str(n))

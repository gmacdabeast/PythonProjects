import colorama
from colorama import Fore, Style, init

#Intro Instructions
init(autoreset=True)
print(Fore.CYAN + 'Welcome to my Text Based Adventure Game!' )
print(Fore.RED + 'You are playing in a virtual Clue Board')
print(Fore.CYAN + 'You have two goals to obtain, either find the key and escape through the ballroom')
print(Fore.RED + 'OR locate 3 artifacts')
print(Fore.CYAN + 'A player can move North, South, East, and West')
print(Fore.RED + 'You cannot move outside the confines of the of the board.')
print(Fore.CYAN + 'The only way to move out of the confines is finding the key and going to the ballroom')
print(Fore.RED + 'You have 15 turns to achieve one of the two goals.')

#Variables we need t consider
turns = 15
artifacts = 0
key = 0
completeRiddle = False
chestOpened = False
chestOpened2 = False
obtainedKey = False

def checkartifacts(x):
    if x == 3:
        return True
    else:
        return False

#check turn function
def minusturn(x):
    x += -1
    global turns
    turns = x
    return turns

def cellar(x):
    global artifacts
    global chestOpened2
    #take one off turns
    minusturn(x)
    #checkartifacts(artifacts)
    if checkartifacts(artifacts) == True:
        print('You have 3 artifacts! You have won! Game is ending now.')
        exit()

    print('Da CELLAR')
    print('*****')
    print('HOME OF ONE MORE CHEST')
    print('*****')
    print('HOWEVER, There a note that says OPEN WILL END GAME.' )
    print('*****')
    print('Current number of turns ' + str(x))
    print('*****')

    #loop to open chest
    while True:
        if chestOpened2 == False:
            chestinput = input('Knowing that this chest could lose you the game, what od you want to do? Answer Y or N...')
            #global artifacts
            if chestinput in ['Y','N']:
                if chestinput in 'Y':
                    print('You have found a new artifact! The holy grail!!!')
                    print('Another step closer to a win!')
                    artifacts += 1
                    print('You now have ' + str(artifacts) + ' artifacts.')
                    chestOpened2 = True
                    break
                else:
                    print('No worries, keep it movin!')
                    break
            else:
                print('not a valid input try again!')
        else:
            print('You already opened the chest! Keep it moving.')
            break

    #next turn
    while True:
        move = str(input('Enter which way you would like to go: N, S, E, W: '))
        print('*****')
        if move in 'W':
            mainroom(turns)
            break
        elif move in 'N':
            study(turns)
            break
        else:
            print('Cannot go that way! You have a wall, try again.')

def study(x):
    #take one off turns
    minusturn(x)
    #checkartifacts(artifacts)
    if checkartifacts(artifacts) == True:
        print('You have 3 artifacts! You have won! Game is ending now.')
        exit()

    print('A Quiet Room')
    print('*****')
    print('This is the study!')
    print('*****')
    print('Enjoy your stay here, nothing to find.')
    print('*****')
    print('Current number of turns ' + str(x))
    print('*****')
    
    while True:
        move = str(input('Enter which way you would like to go: N, S, E, W: '))
        print('*****')
        if move in 'N':
            dungeon(turns)
            break
        elif move in 'S':
            cellar(turns)
            break
        else:
            print('Cannot go that way! You have a wall, try again.')

def basement(x):
    #take one off turns
    minusturn(x)
    #checkartifacts(artifacts)
    if checkartifacts(artifacts) == True:
        print('You have 3 artifacts! You have won! Game is ending now.')
        exit()
    
    print('A boring room... the Basement')
    print('*****')
    print('Absolutely nothing to see here')
    print('*****')
    print('Unless of course there\'s something in storage you need?')
    print('*****')
    print('Current number of turns ' + str(x))
    print('*****')

    #next turn
    while True:
        move = str(input('Enter which way you would like to go: N, S, E, W: '))
        print('*****')
        if move in 'N':
            cellar(turns)
            break
        elif move in 'W':
            kitchen(turns)
            break
        else:
            print('Cannot go that way! You have a wall, try again.')

def dungeon(x):
    global obtainedKey
    global key
    #take one off turns
    minusturn(x)
    #checkartifacts(artifacts)
    if checkartifacts(artifacts) == True:
        print('You have 3 artifacts! You have won! Game is ending now.')
        exit()
    
    print('Possibly the most important room in the game! THE DUNGEON')
    print('*****')
    print('Here lies one of the biggest tests yet')
    print('*****')
    print('You are going to get one chance to answer one more riddle.')
    print('*****')
    print('Get it right, you find the key. Get it wrong, lose all your artifacts and look for more.')
    print('*****')
    print('Current number of turns ' + str(x))
    print('*****')
    keyQuestion = input('I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?')


    while obtainedKey == False:
        
        if keyQuestion in ['echo', 'Echo','an Echo', 'An Echo', 'an echo']:
            print('YOU DID IT. HERE IS THE KEY! GET TO THE BALLROOM NOW TO WIN')
            key += 1 
            obtainedKey = True
            break
        else:
            print('Failure... You have ' + str(x) + ' to find 3 artifacts, get looking!')
            break

    while True:
        move = str(input('Enter which way you would like to go: N, S, E, W: '))
        print('*****')
        if move in 'S':
            study(turns)
            break
        else:
            print('Cannot go that way! You have a wall, try again.')

#kitchen function
def kitchen(x):
    #take one off turns
    minusturn(x)
    #checkartifacts(artifacts)
    if checkartifacts(artifacts) == True:
        print('You have 3 artifacts! You have won! Game is ending now.')
        exit()
    
    print('Soups on! Here is the kitchen!')
    print('*****')
    print('Need to stay hungry in the kitchen always.')
    print('*****')
    print('Current number of turns ' + str(x))
    print('*****')
    print('You take three steps and notice a cook hanging off the kitchen Desk.')
    print('*****')

    #take the tunnel?
    while True:
        tunnel = input('Upon pulling it you find a secret tunnel! WHo knows where it leads?? Want to enter? Y or N: ')
        if tunnel in ['Y','N']:
            if tunnel in 'Y':
                dungeon(turns)
                break
            else:
                print('No worries, keep it movin!')
                break
        else:
            print('Not a valid input! Try again!')
    

    #next move
    #next turn
    while True:
        move = str(input('Enter which way you would like to go: N, S, E, W: '))
        print('*****')
        if move in 'N':
            mainroom(turns)
            break
        elif move in 'E':
            basement(turns)
            break
        elif move in 'W':
            lounge(turns)
            break
        else:
            print('Cannot go that way! You have a wall, try again.')


#lounge function
def lounge(x):
    global artifacts
    global completeRiddle
    #take one off turns
    minusturn(x)
    #checkartifacts(artifacts)
    if checkartifacts(artifacts) == True:
        print('You have 3 artifacts! You have won! Game is ending now.')
        exit()
    #intro to lounge
    print('Here we come, it\'s is the lounge')
    print('*****')
    print('One thing that we can do here is chill here')
    print('*****')
    print('Current number of turns ' + str(x))
    print('*****')

    while True:
        if completeRiddle == False:
            print('We have a treat, if you can answer the riddle, you get one artifact!')
            riddle = input('You have three stoves: a gas, wood, and coal stove, but only one match. Which do you light first?\nAnswer in 1 word:')
            #global artifacts
            if str(riddle) in ['Match','match']:
                print('Wow! You did it! You have received the gold watch artifact!')
                artifacts += 1
                print('*****')
                print('You now have ' + str(artifacts) + ' artifacts!')
                completeRiddle = True
                break
            else:
                print('Incorrect!! Keep guessing...')
        else:
            print('Looks like you already completed your artifact quest here, keep it movin!')
            break
        

    #next turn
    while True:
        move = str(input('Enter which way you would like to go: N, S, E, W: '))
        print('*****')
        if move in 'N':
            boilerroom(turns)
            break
        elif move in 'E':
            kitchen(turns)
            break
        else:
            print('Cannot go that way! You have a wall, try again.')

#boilerroom function
def boilerroom(x):
    #take one off turns
    minusturn(x)
    #checkartifacts(artifacts)
    if checkartifacts(artifacts) == True:
        print('You have 3 artifacts! You have won! Game is ending now.')
        exit()
     

    #Intro to boiler room
    print('Eyyy! Welcome to the Boiler Room!')
    print('*****')
    print('Lots of fun to be had here, there are rooms above and below, check each one out.')
    print('*****')
    print('Current number of turns ' + str(x))

    #artifact check
    print('You currently have ' + str(artifacts) + ' artifacts and need 3, keep it moving!')


    #what's the next move!
    while True:
        move = str(input('Enter which way you would like to go: N, S, E, W: '))
        print('*****')
        if move in 'N':
            gameroom(turns)
            break
        elif move in 'S':
            lounge(turns)
            break
        elif move in 'E':
            mainroom(turns)
        else:
            print('Cannot go that way! You have a wall, try again.')
    
#game room
def gameroom(x):
    global artifacts
    global chestOpened
    #take a turn off
    minusturn(x)
    if checkartifacts(artifacts) == True:
        print('You have 3 artifacts! You have won! Game is ending now.')
        exit()

    #intro
    print('Welcome to the Game Room!')
    print('*****')
    print('Where legends are born')
    print('*****')

    #loop to open chest
    while True:
        if chestOpened == False:
            chestinput = input('There appears to be a chest! Would you like to open it? Answer Y or N...')
            #global artifacts
            if chestinput in ['Y','N']:
                if chestinput in 'Y':
                    print('You found the heralded PS2! One of the finest consoles ever crafted')
                    print('This is a worthy artifact, congrats on the find')
                    artifacts += 1
                    print('You now have ' + str(artifacts) + ' artifacts.')
                    chestOpened = True
                    break
                else:
                    print('No worries, keep it movin!')
                    break
            else:
                print('not a valid input try again!')
        else:
            print('You already opened the chest! Keep it moving.')
            break


 #what's the next move!
    while True:
        move = str(input('Enter which way you would like to go: N, S, E, W: '))
        print('*****')
        if move in 'S':
            boilerroom(turns)
            break
        else:
            print('Cannot go that way! You have a wall, try again.')

#Main room function
def mainroom(x):
    #minus turn
    minusturn(x)
    if checkartifacts(artifacts) == True:
        print('You have 3 artifacts! You have won! Game is ending now.')
        exit()
    #intro
    print('*****')
    print('Welcome back to the main room! Nothing here to see, make a new move!')
    print('*****')
    print('Current number of turns ' + str(x))
    print('*****')

    #artifact check
    print('You currently have ' + str(artifacts) + ' artifacts and need 3, keep it moving!')
    
    #Input to start out and get directions
    while True:
        move = str(input('Enter which way you would like to go: N, S, E, W: '))
        if move in ['N', 'S', 'E', 'W']:
            print('we good')
        #directions for moving NSEW to start
            if move in 'N':
                ballroom(turns)
            elif move in 'W':
                boilerroom(turns)
                break
            elif move in 'S':
                kitchen(turns)
                break
            elif move in 'E':
                cellar(turns)
                break
            else:
                print('This is not a valid input! Try again...')

#ballroom
def ballroom(x):
    #take a turn off
    #x += -1
    #turns = x
    minusturn(turns)
    if checkartifacts(artifacts) == True:
        print('You have 3 artifacts! You have won! Game is ending now.')
        exit()


    #print out welcome & #of turns
    print('*****')
    print('welcome to the ballroom')
    print('*****')
    print('Current number of turns ' + str(x))
    print('*****')

    #Does anything happen in the ballroom?
    if key == 1:
        print('You have won the game! I am so proud, later.')
        exit()
    else:
        print('I see you still have not found the key, no worries come back when you have it.')


    #space
    print('*****')

    #artifact check
    print('Current Artifact count stands at ' + str(artifacts))


    #keep it moving if they haven't found the key or three artifacts
    while True:
        move = str(input('Enter which way you would like to go: N, S, E, W: '))
        print('*****')
        if move in 'S':
            mainroom(turns)
            break
        else:
            print('Cannot go that way! You have a wall, try again.')
            
    


#Input to start out and get directions
while True:
    move = str(input('Enter which way you would like to go: N, S, E, W: '))
    if move in ['N', 'S', 'E', 'W']:
        print('we good')
#directions for moving NSEW to start
        if move in 'N':
            ballroom(turns)
            break
        elif move in 'W':
            boilerroom(turns)
            break
        elif move in 'S':
            kitchen(turns)
            break
        elif move in 'E':
            cellar(turns)
            break
    else:
        print('This is not a valid input! Try again...')


